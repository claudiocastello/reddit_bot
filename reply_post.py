import praw, re, os

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

# Look the first five posts on the subreddit to reply to
for submission in subreddit.hot(limit=5):
    
    # If the bot didn't replied to the post
    if submission.id not in posts_replied_to:
        
        # Look for the word Fibonacci in the post titles (case insensitive)
        if re.search('fibonacci', submission.title, re.IGNORECASE):
           
            # If 'fibonacci' is found, reply to the post
            submission.reply('FiboBot says: Awesome Fibonacci!')
            print('Bot replying to: ', submission.title)
           
            # Store the ID into the replied to list
            posts_replied_to.append(submission.id)

            # Write the updated list in the ID file
            with open('posts_replied_to.txt', 'w') as f:
                for post_id in posts_replied_to:
                    f.write(post_id + '\n')