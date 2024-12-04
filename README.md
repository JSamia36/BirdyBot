# BirdyBot
A python program to make your twitter account easier to run. This posts tweets for you, follows people, likes and retweets posts all on a schedule you set!

## Getting Started
I haven't had a second to fully test from the start. I will make updates and revisions as needed based on that. Make sure to start with installing the neccessary files:
```pip install -r requirements.txt```

Following that update file.txt to include tweets you'd like. You then have to modify cookies.py to include your username and password. Once cookies.py is ran once it ideally won't need to be ran again.

You also will need chromedriver, this has to be placed in the same folder or you have to modify the path. That can be downloaded at https://googlechromelabs.github.io/chrome-for-testing/#stable

#### Image Support is now Added!
To add an image to your tweet, add the filepath in file.txt between '<' & '>'

For example, 
``This is a tweet <image.png>``

## Modifying
It is open source so you can make any modifications to the timing and amount of stuff done. The schedule is in main.py but the delays should be at the start of each program. If you wish to run individual they should be setup to support that as well, meaning you can just run the tweet or retweet features. Make sure to also modify the files to traget the specific searches and accounts you want.
