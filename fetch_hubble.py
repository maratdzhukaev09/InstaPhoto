import requests, os, argparse
from pic_prepare import download_picture, change_for_instagram

def fetch_hubble_image(id):
    response = requests.get(f"http://hubblesite.org/api/v3/image/{id}")
    response.raise_for_status()
    url = f"https:{response.json()['image_files'][-1]['file_url']}"
    filename = f"hubble_{id}.{url.split('.')[-1]}"
    download_picture(url, filename)
    change_for_instagram(filename)

def fetch_hubble_collection(collection):
    response = requests.get(f"http://hubblesite.org/api/v3/images/{collection}")
    response.raise_for_status()
    images = response.json()
    for image in images:
        fetch_hubble_image(image['id'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This parser is designed to quickly and efficiently search for data on science fiction \
                books from tululu.org. At the same time, you can download their contents and their covers.'
    )
    parser.add_argument('collection', help='Images collection', type=str)
    args = parser.parse_args()

    os.makedirs("images", exist_ok=True)
    fetch_hubble_collection(args.collection)
