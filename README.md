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
        "id": "item_id",
        "name": "Item Name",
        "type": { "backendValue": "AthenaCharacter" },
        "images": { "featured": "https://example.com/image.jpg" },
        "introduction": { "chapter": "1", "season": "2" }
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
This script is distributed "as is" without any warranty. Use it at your own discretion and risk.

