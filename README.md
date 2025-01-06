# BirdyBot
A python program to make your twitter account easier to run. This posts tweets for you, follows people, likes and retweets posts all on a schedule you set!

## Getting Started
Once downloaded, make sure to start with installing the neccessary files:
```
pip install -r requirements.txt
```

Now add what you'd like the account to tweet in 'file.txt'. This supports emojis and images, please see below on how to add images to the tweets. Modify the config file (config.yaml) to include your username + password for the account. You can also change the amounts of different things here if you'd like, otherwise just leave the other values as is. Make sure to move config.yaml, and file.txt into the same folder as main.py. Once everything is downloaded and modified you can simply run 
``` 
python3 main.py
```

**Chomedriver is required.** This has to be placed in the same folder or you have to modify the path. That can be downloaded at https://googlechromelabs.github.io/chrome-for-testing/#stable

### Linux
If you are on linux, please make sure you use that version for tweet instead. The main file version uses Win32Clipboard which linux does't support. Please keep in mind this might be slower to get updates. There is almost no difference in each file except tweet.py. You can copy from the windows folder and remove the '.exe' for the driver path. Images should now be working again, with a way more simplified manner! (HOPEFULLY IS FIXED NOW WITH ADDING DRIVER.QUIT) There is a chance that your storage system will get filled from running this, to avoid this please make sure your /tmp is frequently cleaned.

## Image Support is now Added!
To add an image to your tweet, add the filepath in file.txt between '<' & '>'

For example, 
> This is a tweet <image.png>

## Modifying
It is open source so you can make any modifications to the timing and amount of stuff done. The schedule is in main.py but the delays should be at the start of each program. If you wish to run individual they should be setup to support that as well, meaning you can just run the tweet or retweet features. Make sure to also modify the files to traget the specific searches and accounts you want.

