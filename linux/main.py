import schedule, random
import time, datetime
import subprocess, os

file_path = "cookies.pkl"
if os.path.exists(file_path):
	print('Cookies already saved')
else:
	print("Preparing to grab those cookies..")
	subprocess.run(["python3", "cookies.py"])
	print("Cookies are now stored")


def tweet():
	subprocess.run(["python3", "tweet.py"])

def like():
	subprocess.run(["python3", "like.py"])

def follow():
	subprocess.run(["python3", "follow.py"])

def retweet():
	subprocess.run(["python3", "retweet.py"])


# Tweeting then sleeping for random time
schedule.every(1).to(120).minutes.do(tweet) 
schedule.every(30).minutes.do(like)
schedule.every(30).minutes.do(retweet)
schedule.every(30).to(120).minutes.do(follow)

start_time = datetime.time(6, 0)
end_time = datetime.time(20, 0)
current_time = datetime.datetime.now().time()

print("Created Schedule!")

while True:
    if start_time <= current_time and current_time <= end_time:
        schedule.run_pending()
        time.sleep(1)
    else:
        time.sleep(3600)
