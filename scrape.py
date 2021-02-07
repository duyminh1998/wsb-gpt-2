# print("Hello World");

import praw
import io

# file1 = open("data.txt","a", encoding="utf-8") 

reddit = praw.Reddit(
    client_id="vvduT3kVaQ7tqQ",
    client_secret="oWHlCFPkRROIOfAlF12duFXrKGvEaw",
    user_agent="pc:https://github.com/duyminh1998/wsb-gpt-2:v1 (by /u/duyminh1998)",
)

# print(reddit.read_only)  # Output: True

wsb = reddit.subreddit("wallstreetbets")

with io.open("data.txt", "a", encoding="utf-8") as f:
	for submission in wsb.top(limit=None):
		if submission.link_flair_text == "DD":
			print(submission.title)
			f.write(submission.selftext) 
			#print(submission.selftext)

f.close()