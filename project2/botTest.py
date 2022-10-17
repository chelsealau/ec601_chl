import botometer

rapidapi_key = '6134034ec1msh847d9287935dd64p17f4c6jsn9e4882720bc8'
twitter_app_auth = {
    'consumer_key' : 'DCJffcKxsoeuaLwulTaqG3EK2',
    'consumer_secret' : '7hzEtMYxloxQaLP7bs4vi0JvSBgxLFOr7e3ykzVVvCSUCMQg4G',
    'access_token' : '1519865372945571841-h6htwtFx2fgRIrsczdQH2qVMmLlDCd',
    'access_token_secret' : 'QaBYl0CNz2IipkFkfatybYd37DC1YpevQrEomvM0hMjI0'
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

result = bom.check_account('@OprahDaily')

print(result)
