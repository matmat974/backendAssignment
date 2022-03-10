from utilities.configaration import *
from utilities.mobile_utilities import *



def before_all(context):
    context.environment = context.config.userdata.get("envUrl")
    context.url = env(context.environment)
    context.otp_tkn = context.config.userdata.get("otp_api_key")



def before_feature(context, feature):
    context.log_account_main = login_function(context, matthew_test_account(context, account_type="main"))
    context.log_account_alt = login_function(context, matthew_test_account(context, account_type="alt"))

