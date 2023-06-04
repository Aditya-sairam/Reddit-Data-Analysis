from socialreaper import Reddit
from socialreaper.tools import flatten

rdt = Reddit("hyVUgX-Bs0auFFH7DSS0ig", "V0Trr9v1hRlzW2VsZXqecbYP-YCkFg")

comments = rdt.subreddit_thread_comments("all", thread_count=50,
                                         comment_count=500, thread_order="top", comment_order="top",
                                         search_time_period="all")

# Convert nested dictionary into flat dictionary
comments = [flatten(comment) for comment in comments]

# Sort by comment score
comments = sorted(comments, key=lambda k: k['data.score'], reverse=True)

# Print the top 10
for comment in comments[:9]:
    print("###\nUser: {}\nScore: {}\nComment: {}\n".format(comment['data.author'], comment['data.score'],
                                                           comment['data.body']))