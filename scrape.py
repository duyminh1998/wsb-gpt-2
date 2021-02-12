# import praw
# import io

# # file1 = open("data.txt","a", encoding="utf-8") 

# reddit = praw.Reddit(
#     client_id="vvduT3kVaQ7tqQ",
#     client_secret="oWHlCFPkRROIOfAlF12duFXrKGvEaw",
#     user_agent="pc:https://github.com/duyminh1998/wsb-gpt-2:v1 (by /u/duyminh1998)",
# )

# # print(reddit.read_only)  # Output: True

# wsb = reddit.subreddit("wallstreetbets")

# with io.open("data.txt", "a", encoding="utf-8") as f:
# 	for submission in wsb.top(limit=None):
# 		if submission.link_flair_text == "DD":
# 			print(submission.title)
# 			f.write(submission.selftext) 
# 			#print(submission.selftext)

# f.close()

# # https://stackoverflow.com/questions/53988619/praw-6-get-all-submission-of-a-subreddit

# Alternate scrape
from psaw import PushshiftAPI
import datetime as dt
import pandas as pd

api = PushshiftAPI()

start_epoch= int(dt.datetime(2013, 1, 1).timestamp())
end_epoch = int(dt.datetime(2013, 2, 1).timestamp())

results = api.search_submissions(q='DD', after=start_epoch,
	                            subreddit='wallstreetbets',
	                            filter=['author', 'title', 'selftext', 'link_flair_text', 'id', 'created'],
	                            limit=10)

df2 = pd.DataFrame([thing.d_ for thing in results])
print("Initialized data frame.")

for j in range(9):
	year = str(2013 + j)
	print("Year: " + year)
	for i in range(1, 11):
		print("Month: " + str(i))
		results = api.search_submissions(q='DD', after=start_epoch, before=end_epoch,
	                            subreddit='wallstreetbets',
	                            filter=['author', 'title', 'selftext', 'link_flair_text', 'id', 'created'],
	                            limit=1000)
		start_epoch = end_epoch
		end_epoch = int(dt.datetime(2013 + j, i + 2, 1).timestamp())
		df = pd.DataFrame([thing.d_ for thing in results])
		df2.append(df, sort=False)

df2.to_csv('results.csv', index=False, encoding='utf-8')
