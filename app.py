from flask import Flask, render_template
import tweepy
import key

app = Flask(__name__)

@app.route("/")

def index():
    result =tweet_data()
    symbol =result[0]
    tweet = result[1]





    return render_template('home.html',symbol_html=symbol,tweet_html=tweet)

@app.route("/hi/")

def tweet_data():
    auth = tweepy.OAuth1UserHandler(consumer_key=key.consumer_key, consumer_secret=key.consumer_secret)
    api = tweepy.API(auth)
    username = 'TheCoinMonitor_'
    tweets_list = api.user_timeline(screen_name=username, count=2)
    tweet_last = tweets_list[0]
    tweet = tweets_list[1]
    x = tweet_last.text
    n = x.split()
    print(n)
    symbol_tweet = n[1]
    position_side = n[2]
    return [symbol_tweet,x]
