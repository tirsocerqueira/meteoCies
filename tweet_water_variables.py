import requests
import tweepy

api_key = 'sx2k9Hf6CGrqeiAGkTSF2N5fG'
api_secret = '2rdovbtb3m4Gwd2aZlwdfWtkfOrZLYzjzXFYIj6VLoTVQDJ136'
access_token = '1619107870234054656-LYlIPmGVTUpTo5Oqsb6kBYQrZHdNwz'
access_token_secret = 'wdE57hblXOumLXD5UUsDflHewqUgQFetxB5tBgLfwlduI'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAP57ogEAAAAAMvsnLe8L36qsN1cpDdfGuKiYv0w%3DesKHhH238WEUBWniDBOHyzGaUJbFliH5q78Uz8BatsoBqbeyOi'


# Tides Info
tides_info = "https://servizos.meteogalicia.gal/apiv4/getTidesInfo?coords=-8.80,42.19&API_KEY=8yH8K2ot78sls8LJ7V1fLXNf31x370Y730V360Dru8036Uk234yDD25a3Pk9f94v"

# Data extraction from buoyancies
data = requests.get(tides_info).json()
all_tides = data['features'][0]['properties']['days'][0]['variables'][0]
tweet = "TABLA DE MAREAS "+ all_tides['summary'][0]['timeInstant'][:10] + "\n" + all_tides['summary'][0]['timeInstant'][11:-6] + " : " + all_tides['summary'][0]['state'] + "\n" +\
      all_tides['summary'][1]['timeInstant'][11:-6] + " : " + all_tides['summary'][1]['state'] + "\n" +\
      all_tides['summary'][2]['timeInstant'][11:-6] + " : " + all_tides['summary'][2]['state'] + "\n" +\
      all_tides['summary'][3]['timeInstant'][11:-6] + " : " + all_tides['summary'][3]['state'] + "\n"



auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
# Create API object
api = tweepy.API(auth)
# Create a tweet
client=tweepy.Client(bearer_token=bearer_token,consumer_key=api_key,consumer_secret=api_secret,access_token=access_token,access_token_secret=access_token_secret)
client.create_tweet(text=tweet)
