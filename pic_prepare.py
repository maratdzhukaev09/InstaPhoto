import requests, os, sys
from PIL import Image

def download_picture(url, filename, folder="images"):
    filepath = os.path.join(folder, filename)

    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)

def change_for_instagram(filename, folder="images"):
    filepath = os.path.join(folder, filename)
    image = Image.open(filepath)
    image.thumbnail((1800, 1800))
    image.save(filepath, format="JPEG")