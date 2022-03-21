def headers_login():
    headers = {
        'Device-Type': 'ios',
        'Device-Id': 'FDFDC90250F147D1830B4FE0C2542F9F',
        'Version-Code': '1224',
        'Content-Type': 'application/json'
    }
    return headers

def login_extended_headers(context):
    headers = {
        'X-kumu-Token': context.loginToken,
        'Device-Id': 'D90E03B9B2B64F7A9502BF2A4C41FE79',
        'Device-Type': 'ios',
        'Version-Code': '1237',
        'X-kumu-UserId': context.guid,
        'Content-Type': 'application/json'
    }
    return headers

def livestream_paylaods():
    payloads = {
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
    return payloads
