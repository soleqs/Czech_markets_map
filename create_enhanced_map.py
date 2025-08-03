import folium
import json
from collections import defaultdict

# Load supermarket data
with open("/home/ubuntu/supermarkets.json", "r", encoding="utf-8") as f:
    supermarket_data = json.load(f)

# Create a map centered on the Czech Republic
m = folium.Map(location=[49.8175, 15.4730], zoom_start=7)

# Group supermarkets by city
cities_data = defaultdict(list)
for element in supermarket_data["elements"]:
    if element["type"] == "node" and "lat" in element and "lon" in element and "tags" in element and "addr:city" in element["tags"]:
        lat = element["lat"]
        lon = element["lon"]
        name = element["tags"].get("name", "Supermarket")
        brand = element["tags"].get("brand", "Unknown Brand")
        city = element["tags"].get("addr:city", "Unknown City")
        
        cities_data[city].append({
            "lat": lat,
            "lon": lon,
            "name": name,
            "brand": brand
        })

# Create markers for each city
for city, supermarkets in cities_data.items():
    if city != "Unknown City":
        # Calculate average position for the city
        avg_lat = sum(s["lat"] for s in supermarkets) / len(supermarkets)
        avg_lon = sum(s["lon"] for s in supermarkets) / len(supermarkets)
        
        # Count supermarkets by brand
        brand_count = defaultdict(int)
        for s in supermarkets:
            brand_count[s["brand"]] += 1
        
        # Create popup text
        popup_text = f"<b>{city}</b><br>"
        popup_text += f"Total supermarkets: {len(supermarkets)}<br>"
        for brand, count in brand_count.items():
            popup_text += f"{brand}: {count}<br>"
        
        # Add marker for the city
        folium.Marker(
            [avg_lat, avg_lon], 
            popup=popup_text,
            icon=folium.Icon(color='blue', icon='shopping-cart', prefix='fa')
        ).add_to(m)

# Save the map to an HTML file
m.save("/home/ubuntu/supermarket_map_project/czech_republic_city_supermarket_map.html")

print("Enhanced interactive map saved to czech_republic_city_supermarket_map.html")

