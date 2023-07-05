import requests
import tweepy

api_key = 'sx2k9Hf6CGrqeiAGkTSF2N5fG'
api_secret = '2rdovbtb3m4Gwd2aZlwdfWtkfOrZLYzjzXFYIj6VLoTVQDJ136'
access_token = '1619107870234054656-LYlIPmGVTUpTo5Oqsb6kBYQrZHdNwz'
access_token_secret = 'wdE57hblXOumLXD5UUsDflHewqUgQFetxB5tBgLfwlduI'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAP57ogEAAAAAMvsnLe8L36qsN1cpDdfGuKiYv0w%3DesKHhH238WEUBWniDBOHyzGaUJbFliH5q78Uz8BatsoBqbeyOi'




# STATION ID
# Cangas => 10906
# Cies Alto => 10125
# Puerto Vigo => 14001
# Cies Boya => 15002

# URL Data for buoyancy
url_boya = "https://servizos.meteogalicia.gal/mgrss/observacion/ultimos10minPlataformas.action?idEst=15002"

# Data extraction from buoyancies
data = requests.get(url_boya).json()
estacion = data['listUltimos10min'][0]['estacion']
viento = data['listUltimos10min'][0]['listaMedidas'][10]['valor']
dir_viento = data['listUltimos10min'][0]['listaMedidas'][3]['valor']
racha = data['listUltimos10min'][0]['listaMedidas'][4]['valor']
dir_racha = data['listUltimos10min'][0]['listaMedidas'][2]['valor']
temperatura = data['listUltimos10min'][0]['listaMedidas'][9]['valor']
# Data convertion m/s to kn
viento = viento * 1.94384
racha = racha * 1.94384

#Tweet format
tweet = " "
tweet = tweet + "Cies" + "\n" + "Wind: " + str(round(viento, 2)) + "\n" + "Dir: " + str(dir_viento) + "\n" + "Shift: " + str(round(racha,2)) + "\n" + "Shift-dir: " + str(dir_racha) + "\n" + "Tª agua: " + str(round(temperatura,2)) +"\n\n"

# Data extraction from static stations
# First station
url_estaciones = "https://servizos.meteogalicia.gal/mgrss/observacion/ultimos10minEstacionsMeteo.action?idParam=VV_AVG_10m,VV_RACHA_10m,DV_AVG_10m,DV_CONDICION_10m&idEst=10906"
data = requests.get(url_estaciones).json()
estacion = data['listUltimos10min'][0]['estacion']
viento = data['listUltimos10min'][0]['listaMedidas'][2]['valor']
dir_viento = data['listUltimos10min'][0]['listaMedidas'][0]['valor']
racha = data['listUltimos10min'][0]['listaMedidas'][3]['valor']
dir_racha = data['listUltimos10min'][0]['listaMedidas'][1]['valor']
# Data convertion m/s to kn
viento = viento * 1.94384
racha = racha * 1.94384
tweet = tweet + estacion + "\n" + "Wind: " + str(round(viento, 2)) + "\n" + "Dir: " + str(
    dir_viento) + "\n" + "Shift: " + str(round(racha, 2)) + "\n" + "Shift-dir: " + str(
    dir_racha) + "\n\n"

# Second station
url_estaciones = "https://servizos.meteogalicia.gal/mgrss/observacion/ultimos10minEstacionsMeteo.action?idParam=VV_AVG_10m,VV_RACHA_10m,DV_AVG_10m,DV_CONDICION_10m&idEst=10125"
data = requests.get(url_estaciones).json()
estacion = data['listUltimos10min'][0]['estacion']
viento = data['listUltimos10min'][0]['listaMedidas'][3]['valor']
dir_viento = data['listUltimos10min'][0]['listaMedidas'][1]['valor']
racha = data['listUltimos10min'][0]['listaMedidas'][2]['valor']
dir_racha = data['listUltimos10min'][0]['listaMedidas'][0]['valor']
# Data convertion m/s to kn
viento = viento * 1.94384
racha = racha * 1.94384
tweet = tweet + estacion + "\n" + "Wind: " + str(round(viento, 2)) + "\n" + "Dir: " + str(
    dir_viento) + "\n" + "Shift: " + str(round(racha, 2)) + "\n" + "Shift-dir: " + str(
    dir_racha) + "\n\n"


# Third station
url_estaciones = "https://servizos.meteogalicia.gal/mgrss/observacion/ultimos10minEstacionsMeteo.action?idParam=VV_AVG_10m,VV_RACHA_10m,DV_AVG_10m,DV_CONDICION_10m&idEst=14001"
data = requests.get(url_estaciones).json()
estacion = data['listUltimos10min'][0]['estacion']
viento = data['listUltimos10min'][0]['listaMedidas'][2]['valor']
dir_viento = data['listUltimos10min'][0]['listaMedidas'][0]['valor']
racha = data['listUltimos10min'][0]['listaMedidas'][3]['valor']
dir_racha = data['listUltimos10min'][0]['listaMedidas'][1]['valor']
# Data convertion m/s to kn
viento = viento * 1.94384
racha = racha * 1.94384
tweet = tweet + estacion + "\n" + "Wind: " + str(round(viento, 2)) + "\n" + "Dir: " + str(
    dir_viento) + "\n" + "Shift: " + str(round(racha, 2)) + "\n" + "Shift-dir: " + str(
    dir_racha) + "\n\n"


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
# Create API object
api = tweepy.API(auth)
# Create a tweet
#api.create_tweet(tweet)
client=tweepy.Client(bearer_token=bearer_token,consumer_key=api_key,consumer_secret=api_secret,access_token=access_token,access_token_secret=access_token_secret)
client.create_tweet(text=tweet)

