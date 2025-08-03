
import requests
import json

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json][timeout:25];
area(3600051684)->.searchArea;
(
  nwr["brand"="Lidl"](area.searchArea);
  nwr["brand"="Kaufland"](area.searchArea);
  nwr["brand"="Tesco"](area.searchArea);
);
out geom;
"""

response = requests.get(overpass_url, params={
    'data': overpass_query
})

try:
    data = response.json()
    with open("/home/ubuntu/supermarkets.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Data successfully fetched and saved to supermarkets.json")
except json.JSONDecodeError:
    print("Error: Could not decode JSON from response.")
    print("Response content:", response.text)


