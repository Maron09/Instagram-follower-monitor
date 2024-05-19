import time
import requests
import asyncio
from follower import get_follower_count
from telegram import Bot

# Replace with your webhook URL, Telegram bot token, and chat ID
WEBHOOK_URL = 'http://127.0.0.1:5000/webhook'
TELEGRAM_BOT_TOKEN = '6104997266:AAGhlwpyWTvpEqSh5iNUMF6EBs-3ubcCJno'
TELEGRAM_CHAT_ID = '1639442338'

# List of Instagram usernames to monitor
USERNAMES = ['ezra.automobiles', '_ezra.o_']

def send_webhook(username, new_follower_count):
    data = {
        'username': username,
        'new_follower_count': new_follower_count
    }
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        response.raise_for_status()
        print(f'Webhook sent for {username}, response status:', response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Error sending webhook for {username}: {e}")

async def send_telegram_message(username, new_follower_count):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    message = f"New followers detected: {new_follower_count} for {username}"
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print(f'Telegram message sent for {username}')
    except Exception as e:
        print(f"Error sending Telegram message for {username}: {e}")

def main():
    last_follower_counts = {username: get_follower_count(username) for username in USERNAMES}
    for username, count in last_follower_counts.items():
        print(f"Initial follower count for {username}: {count}")

    while True:
        try:
            time.sleep(900)  # Sleep for 15 minutes
            for username in USERNAMES:
                current_follower_count = get_follower_count(username)
                print(f"Current follower count for {username}: {current_follower_count}")

                last_follower_count = last_follower_counts[username]
                if current_follower_count > last_follower_count:
                    new_followers = current_follower_count - last_follower_count
                    print(f"New followers detected for {username}: {new_followers}")
                    send_webhook(username, new_followers)
                    asyncio.run(send_telegram_message(username, new_followers))
                    last_follower_counts[username] = current_follower_count
        except Exception as e:
            print(f"Error in main loop: {e}")

if __name__ == "__main__":
    main()
