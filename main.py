# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import tweepy
import tweet

api_key = '8DQxgcyh6aFC8DCkZXUrBmxI8'
api_secret = 'Nxe3ZSGW33STxBJ5Rq0tF88OVWMbNXDwYCC2KCznPgSgTQjLJq'
access_token = '1619107870234054656-vMG8756pAHPcVwy2gQGmZobluAgCWI'
access_token_secret = 'a1Grufanwa6WwG6pnMa5NaGodtM7fXsxXDvRpvBkAO555'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAACjylQEAAAAANVRa4jevRsxiTlZ4dTeyQridFhI%3D7qZAJ31Rb2ENsDo4sAHJWi5BTvhnQEYqQoa2llQjcV4cHfeYp2'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status(tweet.tweet)