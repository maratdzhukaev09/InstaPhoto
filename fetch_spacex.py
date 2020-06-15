import requests, os
from PIL import Image

def download_picture(url, filename, folder="images"):
    filepath = os.path.join(folder, filename)

    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)

def change_for_Instagram(filename, folder="images"):
    filepath = os.path.join(folder, filename)
    image = Image.open(filepath)
    width, height = image.size
    if width > height:
        image.thumbnail((1800, (height / (width / 1800))))
    elif height > width:
        image.thumbnail(((width / (height / 1800)), 1800))
    image.save(filepath, format="JPEG")

def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v3/launches/latest/")
    response.raise_for_status()
    urls = response.json()["links"]["flickr_images"]
    for id, url in enumerate(urls):
        filename = f"spacex_{id}.{url.split('.')[-1]}"
        download_picture(url, filename)
        change_for_instagram(filename)

if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    fetch_spacex_last_launch()