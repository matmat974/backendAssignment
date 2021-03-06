import requests
from behave import *
from utilities.resources import *
from utilities.payload import *


@given('you already login')
def step_livestream(context):
    assert context.loginToken is not None

    context.login_extend_headers = context.log_account_main
    context.livestream_payloads = livestream_paylaods()

@when('creating a livestream')
def step_livestream(context):
    context.createLive = requests.post(context.url+apiResources.createLivestream, headers=context.login_extend_headers, json=context.livestream_payloads)
    # print(context.createLive.json())
    context.channelId = context.createLive.json()['data']['channel_id']
    assert context.channelId is not None

@then('you need to execute the start livestream api')
def step_livestream(context):
    try:
        context.startLive = requests.post(context.url+apiResources.startLivestream, headers=context.login_extend_headers,
                                          json={'channel_id': context.channelId})
        # print(context.startLive.json())
        start_message = context.startLive.json()['message']
        assert start_message == "Success", start_message
        print(start_message)
        start_channel_id = context.startLive.json()['data']['channel_id']
        assert context.channelId == start_channel_id


    except AssertionError:

        context.endLive = requests.post(context.url + apiResources.endLivestream, headers=context.login_extend_headers,
                                        json={'channel_id': context.channelId})

        # print(context.endLive.text)
        print(context.endLive.status_code)
        end_message = context.endLive.json()['message']
        end_channel_id = context.endLive.json()['data']['channel_id']
        assert end_message == 'Success'
        assert context.channelId == end_channel_id
        raise AssertionError

@then('end the livestream')
def step_livestream(context):
    context.endLive = requests.post(context.url+apiResources.endLivestream, headers=context.login_extend_headers,
                                    json={'channel_id': context.channelId})

    print(context.endLive.text)
    print(context.endLive.status_code)
    end_message = context.endLive.json()['message']
    end_channel_id = context.endLive.json()['data']['channel_id']
    assert end_message == 'Success'
    assert context.channelId == end_channel_id
