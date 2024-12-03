import schedule, random
import time, datetime
import subprocess, os

file_path = "cookies.pkl"
if os.path.exists(file_path):
	print('Cookies already saved')
else:
	subprocess.run(["python3", "cookies.py"])


def tweet():
	subprocess.run(["python3", "tweet.py"])

def like():
	subprocess.run(["python3", "like.py"])

def follow():
	subprocess.run(["python3", "follow.py"])

def retweet():
	subprocess.run(["python3", "retweet.py"])

# Tweeting then sleeping for random time
schedule.every(1).to(3).hours.do(tweet)
schedule.every(2).hours.do(like)
schedule.every(2).hours.do(retweet)
schedule.every(2).to(3).hours.do(follow)

start_time = datetime.time(6, 0)
end_time = datetime.time(20, 0)
current_time = datetime.datetime.now().time()

while True:
    if start_time <= current_time <= end_time:
        schedule.run_pending()
        time.sleep(1)
    else:
        time.sleep(3600)
