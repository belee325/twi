import oauth2
import urllib.parse as urlparse
import constants
# create consumer using CONSUMER_KEY and CONSUMER_KEY_SECRET to id app uniquely
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)


def get_request_token():
    client = oauth2.Client(consumer)
    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
        print('an error occurred getting the req token from twitter')
    else:
        return dict(urlparse.parse_qsl(content.decode('utf-8')))

def get_oauth_verifier(request_token):
    # ask user to auth app and give PIN
    print('go to the following:')
    print(get_oauth_verifier(request_token))
    return input('what is pin?')

def get_oauth_verifier_url(request_token):
    return '{}?oauth_token={}'.format(constants.AUTHORIZATION_URL, request_token['oauth_token'])

def get_access_token(request_token, oauth_verifier):
    # create token obj containig the request toke and verifier
    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)
    # create client with consumer and the newly created and verified token
    client = oauth2.Client(consumer, token)
    # ask twitter for access token
    response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
    return dict(urlparse.parse_qsl(content.decode('utf-8')))