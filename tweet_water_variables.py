from datetime import datetime
import requests
import tweepy
import time
import subprocess
import urllib.request

api_key = '8DQxgcyh6aFC8DCkZXUrBmxI8'
api_secret = 'Nxe3ZSGW33STxBJ5Rq0tF88OVWMbNXDwYCC2KCznPgSgTQjLJq'
access_token = '1619107870234054656-vMG8756pAHPcVwy2gQGmZobluAgCWI'
access_token_secret = 'a1Grufanwa6WwG6pnMa5NaGodtM7fXsxXDvRpvBkAO555'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAACjylQEAAAAANVRa4jevRsxiTlZ4dTeyQridFhI%3D7qZAJ31Rb2ENsDo4sAHJWi5BTvhnQEYqQoa2llQjcV4cHfeYp2'


# Tides Info
tides_info = "https://servizos.meteogalicia.gal/apiv4/getTidesInfo?coords=-8.80,42.19&API_KEY=8yH8K2ot78sls8LJ7V1fLXNf31x370Y730V360Dru8036Uk234yDD25a3Pk9f94v"

# Data extraction from buoyancies
#data = requests.get(url_boya).json()
#print (data)
#auth = tweepy.OAuthHandler(api_key, api_secret)
#auth.set_access_token(access_token, access_token_secret)
# Create API object
#api = tweepy.API(auth)
# Create a tweet
#api.update_status(tweet)

url = "https://www.meteogalicia.gal/datosred/satelite/ULTIMOS_30_DIAS/VIDEOS/20230213Geocolor24h.mp4"



name="prueba"+".mp4"
try:
    print("Downloading starts...\n")
    urllib.request.urlretrieve(url, name)
    print("Download completed..!!")
except Exception as e:
    print(e)