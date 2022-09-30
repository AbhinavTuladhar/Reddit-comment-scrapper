import praw
from time import perf_counter
import winsound


# Initialise a reddit instance.
# Look up PRAW documentation to substitute REDACTED because I'm not giving my details away >:-D
reddit = praw.Reddit(
    client_id='REDACTED',
    client_secret='REDACTED',
    user_agent='REDACTED',
    username='REDACTED',
    password='REDACTED'
)

url = 'https://www.reddit.com/r/Jokes/comments/xr2gav/whats_the_best_chuck_norris_joke_youve_ever_heard/'

# For time-keeping purposes.
start_time = perf_counter()

# Retrieve the post
submission = reddit.submission(url=url)

# When 'more comments' is encountered, click it `limit` number of times. 
# limit=None means that ALL the top-level comments are fetched.
submission.comments.replace_more(limit=0)

# open a file to save the comments.
with open('Chuck Norris comments.txt', 'w', encoding="utf-8") as file:
    index = 1           # Numbering purposes.
    for top_level_comment in submission.comments:
        # Don't consider stickied comments.
        if top_level_comment.stickied:
            continue
        output = f'({index}) {top_level_comment.body}'
        print(output)
        print()
        index += 1
        file.write(f'{output}\n\n')
    
end_time = perf_counter()
time_taken = end_time - start_time
print(f'It took {time_taken:.2f} seconds to execute.')

# play a freq HZ sound for duration milliseconds to indicate the end of the program.
# It took 397.51 seconds to execute the first time, with limit set to None.
duration = 5000
freq = 2000
winsound.Beep(freq, duration)