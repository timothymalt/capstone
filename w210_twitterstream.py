# This has excellent documentation and instructions:
# http://socialmedia-class.org/twittertutorial.html


# Import the necessary packages to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# My OAuth info
access_token = '872491214-nHbmQQEH40ElL3dngveAiJ4SIqDZ7rkAI0N5L48n'
access_token_secret = 'vYrdfhOyurBZGo1G4uV0tMz3PCs99YQqvEmLNbRlOYzfv'
consumer_key = 'Kv0wNNfjWe1DklisJ80s3nsxy'
consumer_secret = 'esRTmsNkf6BrkD6ACCsTnb2i9k9zL6os4UdslI4kmhlzx3sq1v'

# Imports and configures twitter
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
oauth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="a", language="en")

# To steam endlessly until Control-C
for tweet in iterator:
        print json.dumps(tweet)
