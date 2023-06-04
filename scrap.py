import datetime
import praw
import pandas as pd
from textblob import TextBlob

# Acessing the reddit api

reddit = praw.Reddit(client_id="",      # your client id
                     client_secret="",  #your client secret
                     user_agent="", #user agent name
                     username = "",     # your reddit username
                     password = "")

subreddit = reddit.subreddit("Oscars")

posts = subreddit.top(limit=500)
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": [],"date":[],"sentiment":[]
              }

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)

    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)

    # Unique ID of each post
    posts_dict["ID"].append(post.id)

    # The score of a post
    posts_dict["Score"].append(post.score)

    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)

    # URL of each post
    posts_dict["Post URL"].append(post.url)

    posts_dict["date"].append(datetime.datetime.fromtimestamp(post.created))

    posts_dict['sentiment'].append(float(TextBlob(post.selftext).sentiment.polarity))


# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts.to_csv('reddit_data.csv')
top_posts.to_csv('reddit_data.csv')
print(top_posts)
