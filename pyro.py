from pyrogram import Client
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = Client("my_account")
def bio():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_time = current_time.split(':')
    print("Current Time =", current_time[0], ':' , current_time[1])
    image = Image.open('pil_text.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Ubuntu-Bold.ttf", 51)
    draw.text((300, 420),f'{current_time[0]} : {current_time[1]}',(255,255,255),font=font)
    app.update_profile(bio=f'{current_time[0]} : {current_time[1]} \n @messagetokhalil_bot' )
    image.save('sample-out.jpg')
    app.set_profile_photo(photo='sample-out.jpg')
    photos = app.get_profile_photos("me")
    app.delete_profile_photos(photos[1].file_id)
    # except:
    #     print('😕 ')

scheduler = AsyncIOScheduler()
scheduler.add_job(bio, "interval", seconds=30)
scheduler.start()
app.run()


