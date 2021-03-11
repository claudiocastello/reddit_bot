import praw, pdb, re, os

# Create the Reddit instance
reddit = praw.reddit('bot1')

if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []

    else:
        with open('posts_replied_to.txt', 'r') as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split('\n')
            posts_replied_to = list(filter(None, posts_replied_to))


subreddit = reddit.subreddit("FibonacciAsFuck")

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search('fibonacci'), submission.title, re.IGNORECASE):
            submission.reply('FiboBot says: Awesome Fibonacci!')
            print('Bot replying to: ', submission.title)
            posts_replied_to.append(submission.id)

            with open('posts_replied_to.txt', 'w') as f:
                for post_id in post posts_replied_to:
                    f.write(post_id + '\n')