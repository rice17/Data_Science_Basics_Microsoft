# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:24:27 2016

@author: abhishar
"""

import oauth2 as oauth
import urllib2 as urllib

# See assignment1.html instructions or README for how to get these credentials

api_key = "A3fTaIxGwYSttasAJm58B0p6O"
api_secret = "E8jLWDDIpg1vtxQAdU99BehWIL6HCsUPZ9YbOKn0nfigkfa4R6"
access_token_key = "533253262-dReFjhaqT4omSUEfhBfGGV3cIIzWReAsYV9GS8WE"
access_token_secret = "UCTbI8NReyR2iKha6LRtaVbuQShMVmT0XnZicf9YCPWPW"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer, token=oauth_token, http_method=http_method, http_url=url, parameters=parameters)
    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
    headers = req.to_header()
    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()
    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)
    response = opener.open(url, encoded_post_data)
    return response

def fetchsamples():
  #url = "https://api.twitter.com/1.1/search/tweets.json?q=demonetization"
  url = 'https://api.twitter.com/1.1/search/tweets.json?q="demonetization"%20OR%20"note%20OR%20ban"%20OR%20"demonetisation"%20since%3A2016-11-09%20until%3A2016-11-12'
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchsamples()
