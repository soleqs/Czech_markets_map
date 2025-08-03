# Interactive Supermarket Map of the Czech Republic

This project contains two main features:
1.  An interactive map of supermarkets in the Czech Republic.
2.  A choropleth map visualizing average housing prices by region.

---

## 1. Housing Price Map

This map displays the regions of the Czech Republic, colored according to the average price per square meter of housing. It is fully interactive.

### How to Use

1.  **Add GeoJSON Data**: You must obtain a GeoJSON file containing the boundaries of the Czech regions (`kraje`). Name this file `czech_regions.geojson` and place it in the root of the project directory. You can find such data on sites like [GADM](https://gadm.org/download_country.html) or Czech government data portals.
2.  **Update Price Data**: Open the `housing_price_map.html` file and edit the `regionalPrices` JavaScript object with up-to-date and accurate housing price data for each region.
3.  **View the Map**: Open the `housing_price_map.html` file directly in your web browser.

### Project Files

-   `housing_price_map.html`: The standalone HTML file containing all the logic for the housing price map. It uses Leaflet.js.
-   `czech_regions.geojson`: **(Required, user-provided)** A GeoJSON file with the geographical boundaries of the Czech regions.

---

## 2. Supermarket Map

This map shows markers for cities in the Czech Republic that have Lidl, Kaufland, or Tesco supermarkets.

### Requirements

-   Python 3
-   `folium`
-   `geopy`

### Setup and Local Launch

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/soleqs/Czech_markets_map.git
    cd Czech_markets_map
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install folium geopy
    ```

3.  **Run the script to generate the map:**
    ```bash
    python create_enhanced_map.py
    ```
    This will create or update the `czech_republic_city_supermarket_map.html` file.

4.  **View the map:**
    Open the `czech_republic_city_supermarket_map.html` file in your web browser.

### How to Update the City List

To add, remove, or modify cities and their supermarket data, edit the `user_city_data.json` file. After editing, run the `create_enhanced_map.py` script again to regenerate the map.

### Project Files

-   `create_enhanced_map.py`: The main Python script to generate the supermarket map.
-   `user_city_data.json`: The data source for the supermarket map.
-   `czech_republic_city_supermarket_map.html`: The output interactive map file.

---

## Deployment to Netlify

Both `housing_price_map.html` and `czech_republic_city_supermarket_map.html` are static files. You can deploy this project on Netlify.

1.  Push your files (including the generated maps and the `czech_regions.geojson` file) to your Git repository.
2.  **Create a new site on Netlify:**
    -   Log in to your Netlify account.
    -   Click "Add new site" -> "Import an existing project".
    -   Connect to your Git provider.
    -   Select this repository.
    -   Set the **Publish directory** to `/` (the root of the project) and leave the **Build command** empty.
    -   Click "Deploy site".
