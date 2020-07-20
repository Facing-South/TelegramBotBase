# TelegramBotBase
Here you will find the basis for a Telegram bot based on Python. Just like with a Discord bot, it is possible to use different programming languages for a Telegram bot. However, since I want to use a Telegram bot in connection with a Raspberry-Pi in the course of my development and the connection between Raspberry-Pi and Python is great, I decided to use Python for the base.
 
## Installation
To run a Telegram bot under Python, you need two things. For one, Python (I recommend Python3) and the Telegram API. You can find out exactly how you can download and install these elements in the following:

### Python3
1. Download latest Python3-Version here: [python.org](https://www.python.org/downloads/windows/)
2. Run the installer you just downloaded and be sure you enable the "Add Python to Path" option during installation

### Telegram
1. Open Command-Window (win + R, insert cmd and hit enter) and execute the following command: pip install python-telegram-bot

## Create Bot
<p align="center">
  <img src="https://www.facing-south.com/img/botfather.png" width="500">
</p>

To create a Telegram bot, please follow these instructions of the [Botfather](https://core.telegram.org/bots). During the installation you will receive a token, which must be kept secret so that the bot you create cannot be misused. And just for your information: The Botfather is a bot himself ;)</br>
After following the instructions and registering a bot with Telegram, please insert the token you received into token.txt. The token.txt is also in the project folder. Within this file, the sample token must be deleted before inserting the token you received.

## Download Project
After you have created your bot, you can download my template here from Github. Please make sure that all files end up in the same folder (otherwise the bot will not work). Then you search for the file token.txt and enter the token you received from the botfather.

## Run Bot
After you have registered your bot and inserted the token in the token.txt, you can start the Python script. As long as the program is active, you can communicate with your bot via Telegram. In our example you can write the bot with "/ Hello", after which it will respond with "Hello". All other words you write to the bot will be answered with "I onlny react on" Hello ";)". Note that the token.txt file must be in the same folder as the TelegramBotBase.py Python file to be executed.
