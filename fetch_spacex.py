import requests, os
from pic_prepare import download_picture, change_for_instagram

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