import folium
import json
import time
import geopandas as gpd
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

# Load Czech regions GeoJSON data for the choropleth
try:
    with open("czech_regions.geojson", "r", encoding="utf-8") as f:
        czech_regions_geojson = json.load(f)
except FileNotFoundError:
    print("Error: czech_regions.geojson not found.")
    exit()

# --- 2. Initialize Map and Geocoder ---

# Create a map centered on the Czech Republic
m = folium.Map(location=[49.8175, 15.4730], zoom_start=7, tiles="CartoDB positron")

# Initialize geolocator
geolocator = Nominatim(user_agent="czech_supermarket_map_creator")


# --- 3. Add Map Layers ---

# Add Choropleth Layer for Housing Prices
folium.Choropleth(
    geo_data=czech_regions_geojson,
    name='Housing Prices',
    data=housing_prices,
    key_on='feature.properties.NAME_1',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name='Average Housing Price (CZK/m²)',
).add_to(m)

# Generate and add the national border
try:
    # Use geopandas to read the geojson and merge all region polygons
    gdf = gpd.read_file("czech_regions.geojson")
    national_border = gdf.unary_union

    # Create a GeoDataFrame from the unified geometry
    border_gdf = gpd.GeoDataFrame(crs="EPSG:4326", geometry=[national_border])

    # Add the national border to the map
    folium.GeoJson(
        border_gdf,
        name="Czech Republic Border",
        style_function=lambda x: {
            'color': 'darkgreen',
            'weight': 4,
            'fillOpacity': 0 # No fill
        }
    ).add_to(m)
except Exception as e:
    print(f"Could not generate national border: {e}")


# Add Supermarket Markers with Clustering
marker_cluster = MarkerCluster(name="Supermarkets").add_to(m)

# Create markers for each city from user data
for city_data in user_cities_data:
    city_name = city_data["city"]
    try:
        location = geolocator.geocode(f"{city_name}, Czech Republic")

        if location:
            lat, lon = location.latitude, location.longitude
            
            popup_text = f"<b>{city_name}</b><br>"
            brands = [brand for brand in ["Lidl", "Kaufland", "Tesco"] if city_data.get(brand)]
            
            if brands:
                popup_text += "Supermarkets:<br>" + "<br>".join(brands)
            else:
                popup_text += "No specified supermarkets."

            folium.Marker(
                [lat, lon], 
                popup=folium.Popup(popup_text, max_width=200),
                icon=folium.Icon(color='blue', icon='shopping-cart', prefix='glyphicon')
            ).add_to(marker_cluster)
        else:
            print(f"Warning: Could not geocode city: {city_name}")
        
        time.sleep(1)

    except Exception as e:
        print(f"An error occurred while processing {city_name}: {e}")

# --- 4. Add Layer Control and Save ---

folium.LayerControl().add_to(m)

m.save("index.html")

print("Combined interactive map saved to index.html")
print("This file includes housing price data, supermarket locations, and a national border.")
