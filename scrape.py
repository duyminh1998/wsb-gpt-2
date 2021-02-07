# print("Hello World");

import praw

reddit = praw.Reddit(
    client_id="vvduT3kVaQ7tqQ",
    client_secret="oWHlCFPkRROIOfAlF12duFXrKGvEaw",
    user_agent="pc:https://github.com/duyminh1998/wsb-gpt-2:v1 (by /u/duyminh1998)",
)

# print(reddit.read_only)  # Output: True

wsb = reddit.subreddit("wallstreetbets")

for submission in wsb.hot():
	if submission.link_flair_text == "DD":
		print(submission.title)