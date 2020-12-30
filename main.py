import tweepy
import time
from py_imessage import imessage
import pymsteams

myTeamsMessage = pymsteams.connectorcard("<Microsoft Webhook URL>")
myTeamsMessage.text("this is my text")
myTeamsMessage.send()

phone = ""


guid = imessage.send(phone, "Hello World!")

# Let the recipient read the message
time.sleep(5)
resp = imessage.status(guid)

print(f'Message was read at {resp.get("date_read")}')


# Your twitter API credentials
api_key = ''
api_secret = ''
access_token_secret = ''
access_token = ''

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


user = api.get_user("p2ktwtacc")

print("User details:")
print(user.name)
print(user.description)
print(user.location)
status_count = user.statuses_count
while(1):
    user = api.get_user("p2ktwtacc")
    if (user.statuses_count!=status_count):
        print(1)



