from datetime import datetime
import tweepy
import urllib.request

api_key = 'sx2k9Hf6CGrqeiAGkTSF2N5fG'
api_secret = '2rdovbtb3m4Gwd2aZlwdfWtkfOrZLYzjzXFYIj6VLoTVQDJ136'
access_token = '1619107870234054656-LYlIPmGVTUpTo5Oqsb6kBYQrZHdNwz'
access_token_secret = 'wdE57hblXOumLXD5UUsDflHewqUgQFetxB5tBgLfwlduI'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAP57ogEAAAAAMvsnLe8L36qsN1cpDdfGuKiYv0w%3DesKHhH238WEUBWniDBOHyzGaUJbFliH5q78Uz8BatsoBqbeyOi'

# Set local day
now = datetime.now()

# URL changes depending on the day, month and year
url = "https://www.meteogalicia.gal/datosred/satelite/ULTIMOS_30_DIAS/VIDEOS/"+ str(now.year) + now.strftime('%m') + now.strftime('%d') + "Geocolor24h.mp4"

#VIDEO FILE OF NUBOSITY OF THE PAST 24 HOURS
# Download of the file
name=str(now.day)+str(now.month)+str(now.year)+"last24hour"+".mp4"
try:
    print("Downloading starts...\n")
    urllib.request.urlretrieve(url, name)
    print("Download completed..!!")
except Exception as e:
    print(e)

# Uploading media file and posting the tweet
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
# Create API object
api = tweepy.API(auth)

# Uploading the video
path="/Users/tirsocerqueira/Documents/Proyectos/meteoCies/"+name
upload_result = api.media_upload(path,chunked=True, media_category="tweet_video")
#api.update_status(status="24 últimas horas de satélite para el día " + now.strftime('%d') + "/" + now.strftime('%m') +"/" + str(now.year) , media_ids=[upload_result.media_id_string])

client=tweepy.Client(bearer_token=bearer_token,consumer_key=api_key,consumer_secret=api_secret,access_token=access_token,access_token_secret=access_token_secret)
client.create_tweet(text="24 últimas horas de satélite para el día " + now.strftime('%d') + "/" + now.strftime('%m') +"/" + str(now.year), media_ids=[upload_result.media_id_string])
