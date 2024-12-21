import requests
import json

# Specify the maximum season you want to include
max_season = '2'  # Change this to the maximum season you want to include (e.g., '1', '2', etc.)

def is_valid_intro(intro):
    if not intro:
        return False
    chapter = intro.get('chapter', '1')
    season = intro.get('season', '1')

    if chapter == '1' and season.isdigit() and int(season) <= 9:
        return True
    return False

def filter_items_by_max_season(items, max_season):
    return [item for item in items if item['introduction'].get('season', '1').isdigit() and int(item['introduction'].get('season', '1')) <= int(max_season)]

# Fetch data from API
url = "https://fortnite-api.com/v2/cosmetics/br"
response = requests.get(url)
data = response.json()

# Filter items with featured image and exclude specific types
valid_items = []
excluded_types = {"AthenaLoadingScreen", "AthenaSkyDiveContrail"}  # Types to exclude

for item in data.get('data', []):
    intro = item.get('introduction', None)
    featured_image = item.get('images', {}).get('featured')  # Check for featured image
    backend_type = item.get('type', {}).get('backendValue')  # Get type

    # Only include items with a featured image and not in the excluded types
    if is_valid_intro(intro) and featured_image and backend_type not in excluded_types:
        valid_items.append(item)

# Filter items for seasons up to and including the max_season
filtered_items = filter_items_by_max_season(valid_items, max_season)

# Sort filtered items by season
filtered_items.sort(key=lambda x: int(x.get('introduction', {}).get('season', '1')))

# Save the filtered items to a file named based on the max season
filename = f's1-to-s{max_season}.json'
with open(filename, 'w') as f:
    json.dump(filtered_items, f, indent=4)

print(f'Saved {len(filtered_items)} items with featured images (excluding AthenaLoadingScreen and AthenaSkyDiveContrail) to {filename}')
