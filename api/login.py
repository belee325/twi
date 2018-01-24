import constants
import oauth2
import urllib.parse as urlparse
from twitter_utils import consumer, get_request_token, get_oauth_verifier, get_access_token
from database import Database
from user import User

Database.initialize(database=constants.DATABASE, user=constants.USER,
                    password=constants.PASSWORD, host=constants.HOST)
user_email = input('input email : ')
user = User.load_from_db_by_screen_name(user_email)

# if user doesnt exist go thru getting new tokens and save user
if not user:
    request_token = get_request_token()
    oauth_verifier = get_oauth_verifier(request_token)
    access_token =  get_access_token(request_token, oauth_verifier)
    #save user to db
    first_name = input('input first name')
    last_name = input('input last name')
    user = User(user_email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
    user.save_to_db()

tweets = (user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images'))

for tweet in tweets['statuses']:
    print(tweet['text'])