import requests
import tweepy

api_key = '8DQxgcyh6aFC8DCkZXUrBmxI8'
api_secret = 'Nxe3ZSGW33STxBJ5Rq0tF88OVWMbNXDwYCC2KCznPgSgTQjLJq'
access_token = '1619107870234054656-vMG8756pAHPcVwy2gQGmZobluAgCWI'
access_token_secret = 'a1Grufanwa6WwG6pnMa5NaGodtM7fXsxXDvRpvBkAO555'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAACjylQEAAAAANVRa4jevRsxiTlZ4dTeyQridFhI%3D7qZAJ31Rb2ENsDo4sAHJWi5BTvhnQEYqQoa2llQjcV4cHfeYp2'


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
api.update_status(tweet)
