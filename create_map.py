
import folium
import json

# Load supermarket data
with open("/home/ubuntu/supermarkets.json", "r", encoding="utf-8") as f:
    supermarket_data = json.load(f)

# Create a map centered on the Czech Republic
m = folium.Map(location=[49.8175, 15.4730], zoom_start=7)

# Add markers for each supermarket
for element in supermarket_data["elements"]:
    if element["type"] == "node":
        lat = element["lat"]
        lon = element["lon"]
        name = element["tags"].get("name", "Supermarket")
        brand = element["tags"].get("brand", "Unknown Brand")
        city = element["tags"].get("addr:city", "Unknown City")
        
        popup_text = f"<b>{name}</b><br>Brand: {brand}<br>City: {city}"
        folium.Marker([lat, lon], popup=popup_text).add_to(m)

# Save the map to an HTML file
m.save("/home/ubuntu/czech_republic_supermarket_map.html")

print("Interactive map saved to czech_republic_supermarket_map.html")


