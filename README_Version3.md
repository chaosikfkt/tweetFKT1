# Tweet Counter to Discord

This GitHub Actions script counts tweets with specific hashtags in the last 5 hours and sends the result to a Discord channel via webhook.

## How to use
1. Fork or create a new repo and paste these files.
2. Go to the "Actions" tab and enable workflows.
3. Edit the `HASHTAGS` list in `tweet_counter.py` for your own hashtags.
4. Replace the `DISCORD_WEBHOOK_URL` with your webhook.
5. Script will run every 5 hours automatically.