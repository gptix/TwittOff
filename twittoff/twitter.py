import tweepy
import basilica
import decouple
from decouple import config
from .models import DB, Tweet, User

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'), config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(config("BASILICA_KEY"))


def add_or_update_user(name):
    """
    Add or update a user and their Tweets.
    Throw an error if user doesn't exist or is private.
    """
    try:
        twitter_user = TWITTER.get_user(name)
        db_user = (User.query.get(twitter_user.id) or User(id=twitter_user.id, name=name))
        DB.session.add(db_user)
        tweets = twitter_user.timeline(count=200,
                                       exclude_replies=True,
                                       include_rts=False,
                                       since_id=db_user.newest_tweet_id)
        if tweets:
            db_user.newest_tweet_id = tweets[0].id

        for tweet in tweets:
            emb = BASILICA.embed_sentence(tweet.text, model='twitter')
            db_tweet = Tweet(id=tweet.id, text=tweet.text, embedding=emb)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)

    except Exception as e:
        print(f"Encountered error in add_or_update while processing {name}: {e}")
        raise e

    else:
        DB.session.commit()