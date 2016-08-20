Insta Crawler
=============

This python script crawls the landing page of an Instagram public profile and analyze the last 12 media items, downloading new images and videos.

With two separate metadata dictionaries, it tracks the images and videos downloaded to the local filesystem. If new images or videos appear in the landing page of the profile, the script downloads them and update the metadata dictionaries.

Usage:
```
python insta_crawler.py --profile sdiazb
```

The Insta Crawler can also be used through Telegram with a bot called InstaCrawlerBot(telegram.me/InstaCrawlerBot). 

The execution of the insta_crawler_telegram_bot.py file works as a host that receives users requests, so while not launched, the bot is not available.

Installation:
```
pip install -r requierements.txt
```

Usage:
```
python insta_crawler_telegram_bot.py 
```

