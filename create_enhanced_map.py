import folium
import json
import time
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster

# --- 1. Load Data ---

# Load city and supermarket data
try:
    with open("user_city_data.json", "r", encoding="utf-8") as f:
        user_cities_data = json.load(f)
except FileNotFoundError:
    print("Error: user_city_data.json not found.")
    exit()

# Load housing price data
try:
    with open("housing_prices.json", "r", encoding="utf-8") as f:
        housing_prices = json.load(f)
except FileNotFoundError:
    print("Error: housing_prices.json not found.")
    exit()

# Load Czech regions GeoJSON
try:
    with open("czech_regions.geojson", "r", encoding="utf-8") as f:
        czech_regions_geojson = json.load(f)
except FileNotFoundError:
    print("Error: czech_regions.geojson not found.")
    exit()

# --- 2. Initialize Map and Geocoder ---

# Create a map centered on the Czech Republic
m = folium.Map(location=[49.8175, 15.4730], zoom_start=8, tiles="CartoDB positron")

# Initialize geolocator
geolocator = Nominatim(user_agent="czech_supermarket_map_creator")

# --- 3. Add Choropleth Layer for Housing Prices ---

# Create a Choropleth layer
folium.Choropleth(
    geo_data=czech_regions_geojson,
    name='choropleth',
    data=housing_prices,
    columns=['Region', 'Price'],  # This is not used directly, but good practice
    key_on='feature.properties.NAME_1', # Key in GeoJSON to bind data to
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Average Housing Price (CZK/m²)',
    # The 'data' is a dict, so folium handles the mapping automatically
    # if key_on matches the keys in the data dict.
).add_to(m)


# --- 4. Add Supermarket Markers with Clustering ---

# Create a MarkerCluster layer
marker_cluster = MarkerCluster().add_to(m)

# Create markers for each city from user data
for city_data in user_cities_data:
    city_name = city_data["city"]
    try:
        # Use caching for geocoding to avoid repeated lookups if cities are duplicated
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

            # Add marker for the city to the cluster
            folium.Marker(
                [lat, lon], 
                popup=folium.Popup(popup_text, max_width=200),
                icon=folium.Icon(color='blue', icon='shopping-cart', prefix='glyphicon')
            ).add_to(marker_cluster)
        else:
            print(f"Warning: Could not geocode city: {city_name}")
        
        # Be respectful of the geocoding service's usage policy by adding a delay
        time.sleep(1)

    except Exception as e:
        print(f"An error occurred while processing {city_name}: {e}")

# --- 5. Add Layer Control and Save Map ---

# Add a layer control to toggle layers
folium.LayerControl().add_to(m)

# Save the map to the new standard file name
m.save("index.html")

print("Combined interactive map saved to index.html")
print("This file includes both housing price data and supermarket locations.")
