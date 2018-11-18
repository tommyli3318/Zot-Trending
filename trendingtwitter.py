import twitter
import json
from urllib import request


def create_twitter_instance():
    credentials = None

    with open('credentialstwitter.json') as creds:
        credentials = json.load(creds)
        api = twitter.Api(consumer_key=credentials['consumer_key'],
                      consumer_secret=credentials['consumer_secret'],
                      access_token_key=credentials['access_token_key'],
                      access_token_secret=credentials['access_token_secret'])
    return api


def four_trending(api):
    return api.GetTrendsCurrent()[:4]

if __name__ == '__main__':
    '''Experiment with your reddit function here. Examine the output on the console.'''

    t_api = create_twitter_instance()
    print(five_trending(t_api))
