# Dumper Script Documentation

## Overview
This Python script dumps  Fortnite API. It filters cosmetics based on user-defined parameter called season. The filtered data is then saved as a JSON file.

---

## Requirements
### Dependencies
- Python 3.6+
- Required Libraries:
  - `requests`: For making HTTP requests.
  - `json`: For parsing and handling JSON data.

### Installation
To install the required dependencies, run the following command:
```bash
pip install requests
```

---

## Configuration
Customize the maximum season to include by modifying the `max_season` variable in the dumper:
```python
max_season = '2'  # Specify the desired maximum season (e.g., '1', '2', etc.)
```

---

## Script Workflow
1. **Fetch Data**:
   The script retrieves cosmetic data from the Fortnite API:
   ```python
   url = "https://fortnite-api.com/v2/cosmetics/br"
   response = requests.get(url)
   data = response.json()
   ```

2. **Validate Introductions**:
   Each item is validated to ensure it belongs to a valid season and chapter:
   ```python
   def is_valid_intro(intro):
       if not intro:
           return False
       chapter = intro.get('chapter', '1')
       season = intro.get('season', '1')

       if chapter == '1' and season.isdigit() and int(season) <= 9:
           return True
       return False
   ```

3. **Exclude Specific Types**:
   Certain types of cosmetics are excluded based on their backend values:
   ```python
   excluded_types = {"AthenaLoadingScreen", "AthenaSkyDiveContrail"}
   ```

4. **Filter by Season**:
   The script filters items to include only those from seasons up to the defined `max_season`:
   ```python
   def filter_items_by_max_season(items, max_season):
       return [item for item in items if item['introduction'].get('season', '1').isdigit() and int(item['introduction'].get('season', '1')) <= int(max_season)]
   ```

5. **Sort Data**:
   Filtered items are sorted by season for better organization:
   ```python
   filtered_items.sort(key=lambda x: int(x.get('introduction', {}).get('season', '1')))
   ```

6. **Save to JSON**:
   The processed data is saved to a file named based on the maximum season specified:
   ```python
   filename = f's1-to-s{max_season}.json'
   with open(filename, 'w') as f:
       json.dump(filtered_items, f, indent=4)
   ```

---

## Running the Script
Run the script using the following command:
```bash
python dumper.py
```

---

## Output
The output is a JSON file named according to the specified maximum season, e.g.,:
```
s1-to-s2.json
```
This file contains:
- Items with a featured image.
- Items that are not in the excluded types (e.g., `AthenaLoadingScreen`, `AthenaSkyDiveContrail`).
- Items that belong to seasons up to and including the defined `max_season`.

---

## Example Output
Sample JSON structure of the output file:
```json
[
    {
        "id": "CID_010_Athena_Commando_M",
        "name": "Ranger",
        "description": "Uncommon ranger outfit.",
        "type": {
            "value": "outfit",
            "displayValue": "Outfit",
            "backendValue": "AthenaCharacter"
        },
        "rarity": {
            "value": "uncommon",
            "displayValue": "Uncommon",
            "backendValue": "EFortRarity::Uncommon"
        },
        "introduction": {
            "chapter": "1",
            "season": "1",
            "text": "Introduced in Chapter 1, Season 1.",
            "backendValue": 1
        },
        "images": {
            "smallIcon": "https://fortnite-api.com/images/cosmetics/br/cid_010_athena_commando_m/smallicon.png",
            "icon": "https://fortnite-api.com/images/cosmetics/br/cid_010_athena_commando_m/icon.png",
            "featured": "https://fortnite-api.com/images/cosmetics/br/cid_010_athena_commando_m/featured.png",
            "lego": {
                "small": "https://fortnite-api.com/images/cosmetics/lego/cid_010_athena_commando_m/small.png",
                "large": "https://fortnite-api.com/images/cosmetics/lego/cid_010_athena_commando_m/large.png"
            },
            "bean": {
                "small": "https://fortnite-api.com/images/cosmetics/beans/bean_ranger/small.png",
                "large": "https://fortnite-api.com/images/cosmetics/beans/bean_ranger/large.png"
            }
        },
        "showcaseVideo": "z8veIqFKlCM",
        "added": "2019-11-20T12:50:30Z"
    },
    ...
]
```

---

## Notes
- Ensure your internet connection is stable as the script fetches data from an external API.
- Update the `excluded_types` set to customize the types of cosmetics to exclude.
- Make sure the `max_season` variable aligns with your data filtering requirements.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

