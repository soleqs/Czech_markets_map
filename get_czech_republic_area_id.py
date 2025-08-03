
import requests
import json

nominatim_url = "https://nominatim.openstreetmap.org/search"

headers = {
    "User-Agent": "Manus-Agent/1.0 (https://www.example.com/manus-agent)"
}

params = {
    "q": "Czech Republic",
    "format": "json",
    "polygon_geojson": 1,
    "addressdetails": 1
}

response = requests.get(nominatim_url, params=params, headers=headers)

try:
    data = response.json()
    if data:
        for item in data:
            if item.get("osm_type") == "relation" and item.get("class") == "boundary" and item.get("type") == "administrative":
                print("Czech Republic Area ID: {}".format(int(item["osm_id"]) + 3600000000))
                break
    else:
        print("No results found for Czech Republic.")
except json.JSONDecodeError:
    print("Error: Could not decode JSON from response.")
    print("Response content:", response.text)


