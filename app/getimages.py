import requests
import json
from config import API_KEY, SECRET_KEY
def find_image_url(project_title):
    access_key = API_KEY
    search_query = project_title.replace(' ', '+')

    # Make a request to the Unsplash API
    search_url = f'https://api.unsplash.com/search/photos?query={search_query}&per_page=1'
    headers = {
        'Authorization': f'Client-ID {access_key}'
    }
    response = requests.get(search_url, headers=headers)
    response.raise_for_status()

    # Parse the JSON response
    data = json.loads(response.text)
    if 'results' in data and len(data['results']) > 0:
        image_url = data['results'][0]['urls']['regular']
        return image_url

    return None
#y2ZoBkOYYgH4goEfInz0V03XWCR8l6KKxcjNQiC6tWaJAeWadxKpze3Q 
# Example usage
project_title = input('Enter project title: ')
image_url = find_image_url(project_title)
if image_url:
    print('Image URL:', image_url)
else:
    print('No image found for the given project title.')
