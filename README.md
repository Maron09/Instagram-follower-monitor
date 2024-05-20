# Follower Monitoring Telegram Bot

This project is a Flask-based web application designed to monitor the follower counts of specified usernames on a social media platform. It sends notifications to a Telegram chat whenever there is an increase in followers.

## Features

- **Set Usernames:** Specify a list of usernames to monitor.
- **Start/Stop Monitoring:** Start or stop the monitoring process.
- **Follower Count Checking:** Periodically checks follower counts and detects new followers.
- **Telegram Notifications:** Sends a message to a specified Telegram chat when new followers are detected.

## Technologies Used

- **Flask:** Web framework for building the application.
- **APScheduler:** For scheduling periodic follower count checks.
- **Telegram Bot API:** For sending notifications.
- **Decouple:** For managing configuration variables.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maron09/follower-monitoring-bot.git
   cd follower-monitoring-bot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the project root and add your Telegram bot token and chat ID:**
   ```
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   TELEGRAM_CHAT_ID=your-telegram-chat-id
   ```

5. **Ensure you have the `follower` module with a `get_follower_count` function:**
   ```python
   # follower.py

   def get_follower_count(username):
       # Implement this function to return the follower count for the given username
       pass
   ```

## Running the Application

1. **Run the Flask application:**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints

- **`GET /`**: Renders the index page.
- **`POST /set_usernames`**: Sets the list of usernames to monitor. Expects a JSON payload with a `usernames` key.
  ```json
  {
    "usernames": ["username1", "username2"]
  }
  ```
- **`POST /start_monitoring`**: Starts the monitoring process.
- **`POST /stop_monitoring`**: Stops the monitoring process.

## How It Works

1. **Set Usernames:**
   - Use the `/set_usernames` endpoint to specify the usernames you want to monitor.
   - This initializes the `last_follower_counts` dictionary with the current follower counts for the provided usernames.

2. **Start Monitoring:**
   - Use the `/start_monitoring` endpoint to start the periodic follower count checks.
   - The `check_followers` function is scheduled to run every minute.

3. **Check Followers:**
   - The `check_followers` function retrieves the current follower count for each username.
   - If there is an increase in the follower count, a Telegram message is sent to the specified chat.

4. **Stop Monitoring:**
   - Use the `/stop_monitoring` endpoint to stop the monitoring process.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [APScheduler](https://apscheduler.readthedocs.io/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Decouple](https://pypi.org/project/python-decouple/)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any inquiries, please reach out to [chimarokeonyebi@gmail.com].

---

