import praw #This module is used to create Reddit instances
import json
from urllib import request

'''The reddit_instance object will contain the reddit instance we will create to handle all API calls. 
   Read the Python Reddit API Wrapper(PRAW) documentation for further details'''


def create_reddit_instance(read_only = False):
    '''This function reads the crendentials from credentials.json and creates a Reddit instance.
        You will use this instance to retrieve further information. Before you complete this 
        function, be sure to create your credentials on the Reddit website, update 
        credentials_template.json and rename it to credentials.json
    '''
    credentials = None
    
    '''The read only parameter determines whether a read-only object,i.e, no login required, 
    or an OAuth2 authenticated object should be created
    '''

    with open('credentials.json') as creds:
        credentials = json.load(creds)


    if(not read_only):
        reddit_instance = praw.Reddit(client_id = credentials['client_id'],
                                    client_secret=credentials['client_secret'],
                                    username=credentials['username'],
                                    password=credentials['password'],
                                    user_agent=credentials['user_agent'])
    else:
        reddit_instance = praw.Reddit(client_id = credentials['client_id'],
                                      client_secret=credentials['client_secret'],
                                      user_agent=credentials['user_agent'])

    return reddit_instance
    
    
def ten_top_posts(reddit_instance, subreddit_name):
    '''This function takes a subreddit name as a string and prints out ten posts
    under the top category'''

    subreddit = reddit_instance.subreddit(subreddit_name)

    return subreddit.top(limit=4)

if __name__ == '__main__':
    '''Experiment with your reddit function here. Examine the output on the console.'''

    subreddit_name = 'UCI' 

    reddit_instance = create_reddit_instance()

    posts = ten_top_posts(reddit_instance, subreddit_name)

    for post in posts:
        print(post.title)
        print(post.author)



    


    