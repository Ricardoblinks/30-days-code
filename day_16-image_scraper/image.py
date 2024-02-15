import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, save_dir):
    # Create directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Fetch the web page content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract image URLs
    image_tags = soup.find_all('img')
    for img_tag in image_tags:
        img_url = img_tag.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            img_name = img_url.split('/')[-1]
            img_path = os.path.join(save_dir, img_name)
            try:
                img_data = requests.get(img_url).content
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)
                print(f"Image downloaded: {img_name}")
            except Exception as e:
                print(f"Failed to download {img_name}: {e}")

# Example usage
url = 'https://example.com'
save_directory = 'images'
download_images(url, save_directory)
