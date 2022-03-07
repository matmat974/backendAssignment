import requests
from behave import *
from utilities.resources import *


@given('you already login')
def step_livestream(context):
    assert context.loginToken is not None

    context.headers = {
        'X-kumu-Token': context.loginToken,
        'Device-Id': 'D90E03B9B2B64F7A9502BF2A4C41FE79',
        'Device-Type': 'ios',
        'Version-Code': '1237',
        'X-kumu-UserId': context.guid,
        'Content-Type': 'application/json'
    }

    context.payloads = {
        "channel_title": "Sample create live stream",
        "category": "",
        "description": "test",
        "time": "",
        "language": "",
        "landscape": 0,
        "cover_image": "",
        "rtmp": 0,
        "default_setting": "[\n '1',\n '3'\n]",
        "video": 101,
        "hashtag": ""
    }

@when('creating a livestream')
def step_livestream(context):
    context.createLive = requests.post(context.url+apiResources.createLivestream, headers=context.headers, json=context.payloads)
    # print(context.createLive.json())
    context.channelId = context.createLive.json()['data']['channel_id']
    assert context.channelId is not None

@then('you need to execute the start livestream api')
def step_livestream(context):
    try:
        context.startLive = requests.post(context.url+apiResources.startLivestream, headers=context.headers,
                                          json={'channel_id': context.channelId})
        # print(context.startLive.json())
        startMessage = context.startLive.json()['message']
        assert startMessage == "Success", startMessage
        print(startMessage)
        StartChannelId = context.startLive.json()['data']['channel_id']
        assert context.channelId == StartChannelId


    except AssertionError:

        context.endLive = requests.post(context.url + apiResources.endLivestream, headers=context.headers,
                                        json={'channel_id': context.channelId})

        # print(context.endLive.text)
        print(context.endLive.status_code)
        endMessage = context.endLive.json()['message']
        endChannelId = context.endLive.json()['data']['channel_id']
        assert endMessage == 'Success'
        assert context.channelId == endChannelId
        raise AssertionError

@then('end the livestream')
def step_livestream(context):
    context.endLive = requests.post(context.url+apiResources.endLivestream, headers=context.headers,
                                    json={'channel_id': context.channelId})

    print(context.endLive.text)
    print(context.endLive.status_code)
    endMessage = context.endLive.json()['message']
    endChannelId = context.endLive.json()['data']['channel_id']
    assert endMessage == 'Success'
    assert context.channelId == endChannelId
