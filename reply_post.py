#!/usr/bin/python3
import praw, re, os, pdb, random

bot_answers = [
                'Awesome Fibonacci!',
                'Great picture.',
                'Yeahh, nice!',
                'Great one!!',
                'Amazing, keep posting!',
                'That is fine work.'
            ]

bot_comments = [
                'Agreed!',
                'Yep, agree.',
                'Yeahh!',
                'For sure!'
            ]

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# Create an empty list if it's the first time we ran this code
if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []

# If it's not the first time we run this code, load the list of posts we've replied to
else:
    with open('posts_replied_to.txt', 'r') as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split('\n')
        posts_replied_to = list(filter(None, posts_replied_to))


# Defeine the subreddit to work on
subreddit = reddit.subreddit("FibonacciAsFuck")

# Look for the first five posts on the subreddit to reply to
for submission in subreddit.hot(limit=5):
    
    # Upvote every submission
    submission.upvote()
    print('Bot upvoting: ', submission.title)
    
    # If the bot didn't replied to the post
    if submission.id not in posts_replied_to:
        
        # Look for the word 'fibonacc' in the post titles (case insensitive)
        if re.search('fibonacc', submission.title, re.IGNORECASE):
           
            # If 'fibonacc' is found, reply to the post with a random choice from the list bot_answers
            submission.reply(random.choice(bot_answers))
            print('Bot answering to post: ', submission.title)
           
            # Store the ID into the replied to list
            posts_replied_to.append(submission.id)

            # Write the updated list in the ID file
            with open('posts_replied_to.txt', 'w') as f:
                for post_id in posts_replied_to:
                    f.write(post_id + '\n')


# Navigate through the stream of comments in the subreddit
for comment in subreddit.stream.comments():

    # Look for the word 'fibonacc' in the post comments (case insensitive)
    if re.search('fibonacc', comment.body, re.IGNORECASE):

        # If 'fibonacc' is found, reply to the comment with a random choice from the list bot_comments
        bot_reply = random.choice(bot_comments)
        comment.reply(bot_reply)
        print('Bot replying to a comment.')