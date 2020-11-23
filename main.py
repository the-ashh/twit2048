import tweepy
import numpy as np
from numpy import array
import logic2048

def readFile(path):
    contents = ""
    with open(path) as f:
        for line in f.readlines():
            contents += line
    return contents

game = logic2048.board_2048()
logic2048.fill_cell(game.board)
logic2048.fill_cell(game.board)


api_key = readFile("./api.key")
api_secret = readFile("./api.secret")
access_key = readFile("./access.key")
access_secret = readFile("./access.secret")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)


api = tweepy.API(auth)

# recent_tweet = api.user_timeline(count = 1)[0]

# like_count = recent_tweet.favorite_count
# retweet_count = recent_tweet.retweet_count


# print("number of likes: " + str(like_count))
# print("number of retweets: " + str(retweet_count))
print(game.board)
for i in range(4):
    print(logic2048.move(game.board, i), '\n')