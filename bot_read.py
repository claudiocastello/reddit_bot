import praw

# Create Reddit instance
reddit = praw.Reddit('bot1')

# Define the subreddit to work on
subreddit = reddit.subreddit("FibonacciAsFuck")

# Read the first five hot posts on the defined subreddit
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")