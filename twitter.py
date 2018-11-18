import twitter
import json
from urllib import request


def create_twitter_instance():
    credentials = None

    with open('credentialstwitter.json') as creds:
        credentials = json.load(creds)
        api = twitter.api(consumer_key=credentials['consumer_key'],
                      consumer_secret=credentials['consumer_secret'],
                      access_token_key=credentials['access_token_key'],
                      access_token_secret=credentials['access_token_secret'])
    return api


def five_trending(api):
    return api.GetTrendsCurrent()

if __name__ == '__main__':
    '''Experiment with your reddit function here. Examine the output on the console.'''

    t_api = create_twitter_instance()
    print(five_trending(t_api))
    #posts = ten_top_posts(reddit_instance, subreddit_name)

    #for post in posts:
    #    print(post.title)
    #    print(post.author)
