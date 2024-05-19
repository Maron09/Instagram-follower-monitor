from flask import Flask, request, jsonify, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import time
import requests
import asyncio
from telegram import Bot
from follower import get_follower_count
from decouple import config

app = Flask(__name__)

# Replace with your Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = config('TELEGRAM_CHAT_ID')

# Global variables
scheduler = BackgroundScheduler()
usernames = []
last_follower_counts = {}



async def send_telegram_message(username, new_follower_count):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    message = f"New followers detected: {new_follower_count} for {username}"
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print(f'Telegram message sent for {username}')
    except Exception as e:
        print(f"Error sending Telegram message for {username}: {e}")

def check_followers():
    global last_follower_counts
    for username in usernames:
        current_follower_count = get_follower_count(username)
        print(f"Current follower count for {username}: {current_follower_count}")

        last_follower_count = last_follower_counts.get(username, 0)
        if current_follower_count > last_follower_count:
            new_followers = current_follower_count - last_follower_count
            print(f"New followers detected for {username}: {new_followers}")
            asyncio.run(send_telegram_message(username, new_followers))
            last_follower_counts[username] = current_follower_count

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_usernames', methods=['POST'])
def set_usernames():
    global usernames, last_follower_counts
    usernames = request.json.get('usernames', [])
    last_follower_counts = {username: get_follower_count(username) for username in usernames}
    return jsonify({"status": "success", "usernames": usernames})

@app.route('/start_monitoring', methods=['POST'])
def start_monitoring():
    if not scheduler.get_jobs():
        scheduler.add_job(func=check_followers, trigger="interval", minutes=1)
        scheduler.start()
    return jsonify({"status": "monitoring started"})

@app.route('/stop_monitoring', methods=['POST'])
def stop_monitoring():
    scheduler.remove_all_jobs()
    return jsonify({"status": "monitoring stopped"})

if __name__ == "__main__":
    app.run(debug=True)