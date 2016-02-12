import twitter

__author__ = 'johnfulgoni'

# Python Twitter API wrapper provided by Bear
# https://github.com/bear/python-twitter

consumer_key = 'rMRsufFmWu671SA7M4ucWyfcN'
consumer_secret = 'vOOyNUfsP4HafRHzjIASH66jNUiuRSWlTmV4EdCZebc7cLDBfS'
access_token = '260053041-iTAa5wLXnfJWxYFQpuW25U5prsLx6nh511MlpvqQ'
access_secret = 'M3vpYFcoa2bMOfkvV7IoMI1IdpHEPOeoezvHNcmMNmUlB'

# this function takes the user key (mine) and gets a list of friends that I have on twitter
def get_friends():
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)
    try:
        # currently the error is "RATE LIMIT EXCEEDED"
        # not really sure what to do about this at the moment
        # just going to wait for now and see what we get
        # because the first time it ran, it actually worked
        users = api.GetFriends()
        # probably run it once, and save the data for later I suppose
        print [u.name for u in users]
    except twitter.error.TwitterError, e:
        print 'Twitter Error: ' + str(e)