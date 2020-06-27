import os
import tweepy
import re
import json

users = ["samekan822"]

auth = tweepy.OAuthHandler(os.environ["TWITTER_CK"],
                           os.environ["TWITTER_CS"])
auth.set_access_token(os.environ["TWITTER_AT"],
                      os.environ["TWITTER_ATS"])

api = tweepy.API(auth)

tweets = []

for sn in users:
    max_id = None

    while True:
        if max_id:
            tw = api.user_timeline(
                screen_name=sn, trim_user=True, include_rts=False, count=200, max_id=max_id)
        else:
            tw = api.user_timeline(
                screen_name=sn, trim_user=True, include_rts=False, count=200)

        if len(tw) < 1:
            break
        max_id = tw[-1].id - 1

        [tweets.append(tweet.text)
            for tweet in tw if "http" not in tweet.text and "@" not in tweet.text]
    print(f"{sn} done")

print(f"{len(tweets)}tweets")

with open("tweets.txt", "w") as f:
    f.write("\n".join(tweets))
