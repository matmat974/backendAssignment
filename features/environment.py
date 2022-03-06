import requests
from utilities.configaration import *
from utilities.resources import *


def before_all(context):
    context.environment = context.config.userdata.get("envUrl")
    context.url = env(context.environment)
    context.otp_tkn = context.config.userdata.get("otp_api_key")
    context.account = context.config.userdata.get("cp_number")


def before_feature(context, feature):
    # 1. FOR SENDING THE OTP CODE
    sendVerifysms = requests.post(context.url + apiResources.sendOTP,
                                          headers={
                                              'Accept': '*/*',
                                              'Device-Id': 'BF96B46970CB42CD970C9C1879ABA65E',
                                              'Device-Type': 'ios',
                                              'Version-Code': '1224',
                                              'Content-Type': 'application/json'
                                          },
                                          json={"cellphone": context.account, "country_code": "+63"})
    assert sendVerifysms.status_code == 200, "Cannot send an Otp code"

    # 2. FOR GETTING THE OTP CODE
    getOtpresponse = requests.get(context.url + apiResources.getOtp,
                            params={'cellphone': context.account, 'country_code': '63', 'rate_limit': '2'},
                            headers={'otp-secret-key': context.otp_tkn})

    assert getOtpresponse.status_code == 200, "Cannot get the Otp code"
    getOTP = getOtpresponse.json()
    listData = getOTP['data'][0]
    otpCode = listData['verification_code']

    # 3.LOGIN THE MY ACCOUNT
    context.loginResponse = requests.post(context.url + apiResources.postLogin,
                                          headers={
                                              'Device-Type': 'ios',
                                              'Device-Id': 'FDFDC90250F147D1830B4FE0C2542F9F',
                                              'Version-Code': '1224',
                                              'Content-Type': 'application/json'
                                          },
                                          json={"country_code": "+63", "cellphone": context.account,
                                                "verification_code": otpCode})

    assert context.loginResponse.status_code == 200, "Cannot Login"

    context.getData = context.loginResponse.json()
    context.loginToken = context.getData['data']['token']
    context.guid = context.getData['data']['guid']
    # print(guid)
    # print(type(loginToken))
