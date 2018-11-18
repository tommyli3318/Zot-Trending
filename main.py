from flask import Flask, render_template
import json
import reddit
import youtube


app = Flask(__name__)

@app.route('/')
def index():
    #reddit
    subreddit_name = 'UCI'
    reddit_instance = reddit.create_reddit_instance(read_only=True)
    reddit_posts = []
    for p in reddit.ten_top_posts(reddit_instance,subreddit_name):
        reddit_posts.append(p)


    #twitter

    #youtube
    titles, descs, links = youtube.results()


    
    return render_template('index.html',redditPosts = reddit_posts, name = subreddit_name,
                            yt_titles=titles, yt_descs=descs, yt_links=links)

if __name__ == "__main__":
    
    app.run(debug = True) #Set debug = False in a production environment
    