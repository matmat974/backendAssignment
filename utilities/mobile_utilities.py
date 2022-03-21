import os
import requests
from dotenv import load_dotenv, find_dotenv
from utilities.resources import *
from utilities.payload import *



load_dotenv(find_dotenv())

def login_function(context, account):
    login_header = headers_login()





    # 1. FOR SENDING THE OTP CODE
    sendVerifysms = requests.post(context.url + apiResources.sendOTP,
                                          headers=login_header,
                                          json={"cellphone": account, "country_code": "+63"})
    print(sendVerifysms.json())
    assert sendVerifysms.status_code == 200, "Cannot send an Otp code"

    # 2. FOR GETTING THE OTP CODE
    getOtpresponse = requests.get(context.url + apiResources.getOtp,
                            params={'cellphone': account, 'country_code': '63', 'rate_limit': '2'},
                            headers={'otp-secret-key': context.otp_tkn})


    assert getOtpresponse.status_code == 200, "Cannot get the Otp code"
    getOTP = getOtpresponse.json()
    print(getOTP)
    listData = getOTP['data'][0]
    otpCode = listData['verification_code']

    # 3.LOGIN MY ACCOUNT
    context.loginResponse = requests.post(context.url + apiResources.postLogin,
                                          headers=login_header,
                                          json={"country_code": "+63", "cellphone": account,
                                                "verification_code": otpCode})


    assert context.loginResponse.status_code == 200, "Cannot Login"

    context.res_login = context.loginResponse.json()
    print(context.res_login)
    context.get_data = context.res_login['data']
    context.loginToken = context.get_data['token']
    context.guid = context.get_data['guid']
    login_headers = login_extended_headers(context)
    return login_headers




def matthew_test_account(context, account_type):
    num = ""
    if context.url == "https://dev-api.kumuapi.com/" and account_type == "main":
        num = os.getenv("Matthew_Dev_CellNum")
    elif context.url == "https://dev-api.kumuapi.com/" and account_type == "alt":
        num = os.getenv("Matthew_Dev_alt")
    elif context.url != "https://dev-api.kumuapi.com/" and account_type == "main":
        num = os.getenv("Matthew_Prod_CellNum")
    elif context.url != "https://dev-api.kumuapi.com/" and account_type == "alt":
        num = os.getenv("Matthew_Prod_alt")

    return num