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

