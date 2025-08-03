import folium
import json
from collections import defaultdict
import time

try:
    from geopy.geocoders import Nominatim
except ImportError:
    print("Geopy is not installed. Please install it by running: pip install geopy")
    exit()

# Load user-provided city data
with open("user_city_data.json", "r", encoding="utf-8") as f:
    user_cities_data = json.load(f)

# Initialize geolocator
geolocator = Nominatim(user_agent="czech_supermarket_map")

# Create a map centered on the Czech Republic
m = folium.Map(location=[49.8175, 15.4730], zoom_start=7)

# Create markers for each city from user data
for city_data in user_cities_data:
    city_name = city_data["city"]
    try:
        location = geolocator.geocode(f"{city_name}, Czech Republic")
        if location:
            lat, lon = location.latitude, location.longitude
            
            # Create popup text
            popup_text = f"<b>{city_name}</b><br>"
            brands = []
            if city_data.get("Lidl"):
                brands.append("Lidl")
            if city_data.get("Kaufland"):
                brands.append("Kaufland")
            if city_data.get("Tesco"):
                brands.append("Tesco")
            
            if brands:
                popup_text += "Supermarkets:<br>" + "<br>".join(brands)
            else:
                popup_text += "No specified supermarkets."

            # Add marker for the city
            folium.Marker(
                [lat, lon], 
                popup=popup_text,
                icon=folium.Icon(color='green', icon='info-sign', prefix='glyphicon')
            ).add_to(m)
        else:
            print(f"Could not geocode city: {city_name}")
        
        # Be respectful of the geocoding service's usage policy
        time.sleep(1)

    except Exception as e:
        print(f"An error occurred while geocoding {city_name}: {e}")

# Save the map to an HTML file
m.save("czech_republic_city_supermarket_map.html")

print("Enhanced interactive map based on user data saved to czech_republic_city_supermarket_map.html")
