#!/usr/bin/env python

import tweepy
from working_files.app_keys import keys
from working_files.hrc_tweets import tweets
import random


CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#print api.rate_limit_status()

statuses = []

already_following = []

#follow_others is not currently working
def follow_others(requester):

    if str(requester) in already_following:
        pass
    else:
        time.sleep(.5)
        api.create_friendship(id=requester.author.id)
        already_following.append("{0}".format(requester))

# checks last status posted by iHillaBot
for status in api.user_timeline():
    if status not in statuses:
        #If there is a new status, append it to statuses list
        statuses.append(status.id)   
    else:
        pass
        
# writes the status list to a file
with open('status_id_list.txt', 'w') as f:
    f.write(str(statuses))

#most_recent is the id of the last status posted by iHillaBot
most_recent = statuses[0]
#mentions = api.mentions_timeline(since_id=most_recent)

# checks to see @mentions posted to iHillabot since the most recent status
if most_recent:
    mentions = api.mentions_timeline(since_id=most_recent)  
else:
    mentions = ()
    print 'no mentions, early end.'

#If there are more recent mentions. The Bot returns a tweet randomly selected from a list of tweets
for mention in mentions:
    request = mention.text
    requester = mention.user.screen_name
    print 'the requester is: {0}'.format(requester)
    print 'the request is: {0}'.format(request)
    random_tweet = random.choice(tweets)
    random_tweet = random_tweet.strip('\n')
    message = ".@{0} {1} -#iHillaBot".format(requester, random_tweet) 
    reply = api.update_status(status = message)
    print "reply posted: {0}".format(message)
    #follow_others(requester)
