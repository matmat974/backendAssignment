import configparser


def getConfig():

    config = configparser.ConfigParser()  # config parser is a class that will read a basic configuration
    config.read('utilities/properties.ini')

    return config

def env(envUrl):
    if envUrl == "prod" :
        url = getConfig()['envAPI']['prod']
    elif envUrl == "staging" :
        url = getConfig()['envAPI']['staging']
    else:
        url = getConfig()['envAPI']['dev']
    return url


#
# def account():
#     if acc =="prod"