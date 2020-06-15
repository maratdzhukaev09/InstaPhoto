import os, time, random
from dotenv import load_dotenv
from instabot import Bot

if __name__ == "__main__":
    load_dotenv()

    bot = Bot()
    bot.login(username=os.getenv('INSTAGRAM_LOGIN'), password=os.getenv('INSTAGRAM_PASSWORD'))
    folder = 'images'

    for filename in os.listdir(folder):
        bot.upload_photo(os.path.join(folder, filename))
        time.sleep(random.randrange(15, 35))