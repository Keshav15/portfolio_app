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
    response.raise_for_status()loads

    # Parse the JSON response
    data = json.loads(response.text)
    if 'results' in data and len(data['results']) > 0:
        image_url = data['results'][0]['urls']['regular']
        return image_url

    return None

def extract_project_names(resume_text):   # new code
    # Use regular expression to find project names in the resume
    project_names = re.findall(r'Project Name: (.+)', resume_text)
    return project_names

# Load or initialize config file
config_file_path = 'config_file.json'
try:
    with open(config_file_path, 'r') as file:
        config_data = json.load(file)
except FileNotFoundError:
    config_data = {}

# Get the resume text (replace this with your actual method of getting the resume text)
resume_text = "Project Name: Project 1\nDescription: Lorem ipsum dolor sit amet\nProject Name: Project 2\nDescription: Consectetur adipiscing elit"
# Example resume text for testing     #new code

# Extract project names from the resume
project_names = extract_project_names(resume_text)

# Iterate over project names, search for images, and store in config data
for project_name in project_names:
    if project_name not in config_data:
        image_url = find_image_url(project_name)
        if image_url:
            config_data[project_name] = {'image_url': image_url}

# Save the updated config data to the config file
with open(config_file_path, 'w') as file:
    json.dump(config_data, file, indent=2)

print('Config file updated successfully.')      #new code

#y2ZoBkOYYgH4goEfInz0V03XWCR8l6KKxcjNQiC6tWaJAeWadxKpze3Q 
# Example usage
project_title = input('Enter project title: ')
image_url = find_image_url(project_title)
if image_url:
    print('Image URL:', image_url)
else:
    print('No image found for the given project title.')

