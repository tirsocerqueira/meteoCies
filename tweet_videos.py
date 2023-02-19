from datetime import datetime
import tweepy
import urllib.request

api_key = '8DQxgcyh6aFC8DCkZXUrBmxI8'
api_secret = 'Nxe3ZSGW33STxBJ5Rq0tF88OVWMbNXDwYCC2KCznPgSgTQjLJq'
access_token = '1619107870234054656-vMG8756pAHPcVwy2gQGmZobluAgCWI'
access_token_secret = 'a1Grufanwa6WwG6pnMa5NaGodtM7fXsxXDvRpvBkAO555'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAACjylQEAAAAANVRa4jevRsxiTlZ4dTeyQridFhI%3D7qZAJ31Rb2ENsDo4sAHJWi5BTvhnQEYqQoa2llQjcV4cHfeYp2'

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
path="/Users/tirsocerqueira/PycharmProjects/pythonProject/"+name
upload_result = api.media_upload(path,chunked=True, media_category="tweet_video")
api.update_status(status="24 últimas horas de satélite para el día " + now.strftime('%d') + "/" + now.strftime('%m') +"/" + str(now.year) , media_ids=[upload_result.media_id_string])