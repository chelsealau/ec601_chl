import botometer

rapidapi_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
twitter_app_auth = {
    'consumer_key' : 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'consumer_secret' : 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'access_token' : 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'access_token_secret' : 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

result = bom.check_account('@OprahDaily')

print(result)
