import tweepy, basilica, python-decouple
from decouple import config
from .models import DB, Tweet, User

#TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_
#                                    config('TWITER_ACCESS-

# TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS
#                               config('TWITER_ACCESS-

# TWITTER = tweepy.API(TWITTER_AUTH)

# BASILICA = basilica.Connectin(CONFIG('BASILIC_KEY

def add_or_update_user()
"""
Add or update a user and their tweets..
"""

try:
    twitter_user = TWITTER.get_user(name)
    db_user = (User.query.get(twitter_user.id) or Ueer(id=twitter_user.id, name=name))
    DB.session.add(db_user)
    tweets = twitter_user.time;ine(count = 200,
                                   exclude_replies=True,
                                   include_rts=False,
                                   since_id=db_user.newest_tweet_id)

    if tweets:
        db_user.newest_tweet_id = tweets[0].id
                                   
for tweet in tweets:
    
except Excepteion as e:
    pass

else:
    pass
