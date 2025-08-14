import requests
import subprocess
import sys
from datetime import datetime, timedelta

# Install snscrape if not present
try:
    import snscrape.modules.twitter as sntwitter
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "snscrape"])
    import snscrape.modules.twitter as sntwitter

HASHTAGS = [
    "FirstKhaotung",
    "เฟิร์สข้าวตัง",
    "FirstKanaphan",
    "Khaotungg"
]

# Webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1405472702990651462/zyu4nwvetIygzPhlXbQtGTeg_PzVJbw-17sjJqA5vysrVz2JUFdLHxHP1grm9tlpkNru"

def count_tweets(hashtag):
    # Count tweets from last 5 hours
    since_time = datetime.utcnow() - timedelta(hours=5)
    query = f"#{hashtag} since:{since_time.strftime('%Y-%m-%d_%H:%M:%S_UTC')}"
    count = 0
    for _ in sntwitter.TwitterSearchScraper(query).get_items():
        count += 1
    return count

def send_discord():
    since_time = (datetime.utcnow() - timedelta(hours=5)).strftime('%Y-%m-%d %H:%M:%S UTC')
    results = []
    for tag in HASHTAGS:
        count = count_tweets(tag)
        results.append(f"#{tag}: {count}")
    message = f"📊 **Tweet count in last 5h** (since {since_time}):\n" + "\n".join(results)
    requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
    print("Sent to Discord.")

if __name__ == "__main__":
    send_discord()
