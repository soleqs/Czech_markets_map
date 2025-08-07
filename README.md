# Interactive Map of Czech Housing Prices and Supermarkets

This project generates a single, interactive map of the Czech Republic that visualizes two key datasets:
1.  **Choropleth Map of Housing Prices:** Regions are colored based on the average price per square meter of housing.
2.  **Supermarket Locations:** Cities with major supermarkets (Lidl, Kaufland, Tesco) are marked and clustered.

The final output is a single `index.html` file that can be opened in any modern web browser.

---

## Requirements

-   Python 3
-   The following Python libraries: `folium`, `geopy`

## How to Use

### 1. Setup

**Clone the repository:**
```bash
git clone https://github.com/soleqs/Czech_markets_map.git
cd Czech_markets_map
```

**Install the required Python libraries:**
```bash
pip install -r requirements.txt
```
*(Note: You may need to create a `requirements.txt` file if one doesn't exist. It should contain `folium` and `geopy`.)*

### 2. Provide Necessary Data

Make sure you have the following data files in the root of the project directory:

-   `czech_regions.geojson`: A GeoJSON file containing the geographical boundaries of the Czech regions (`kraje`). You can find this data on sites like [GADM](https://gadm.org/download_country.html) or Czech government data portals.
-   `user_city_data.json`: A JSON file listing cities and the supermarkets they contain.
-   `housing_prices.json`: A JSON file with the average housing price for each region.

### 3. Generate the Map

Run the main script from your terminal:
```bash
python create_enhanced_map.py
```
This script will read the data files, generate the map, and save it as `index.html`.

### 4. View the Map

Open the generated `index.html` file in your web browser to see the interactive map.

---

## How to Update the Data

You can easily update the map by editing the data files:

-   **To update supermarket locations:**
    Edit the `user_city_data.json` file. You can add, remove, or modify cities and their `true`/`false` values for each supermarket brand.

-   **To update housing prices:**
    Edit the `housing_prices.json` file. Change the price value for each region as needed. The region names must match the `NAME_1` property in your `czech_regions.geojson` file.

After editing any data file, simply run the `create_enhanced_map.py` script again to regenerate `index.html` with the latest data.

---

## Project Files

-   `create_enhanced_map.py`: The main Python script that generates the map.
-   `index.html`: The final, interactive map file.
-   `user_city_data.json`: Data source for supermarket locations.
-   `housing_prices.json`: Data source for regional housing prices.
-   `czech_regions.geojson`: **(Required, user-provided)** GeoJSON data for region boundaries.
-   `requirements.txt`: Lists the Python dependencies.

---

## Deployment

The generated `index.html` is a static file and can be deployed on any static hosting service like Netlify, Vercel, or GitHub Pages.

1.  Push your project files (including the generated `index.html` and all data files) to your Git repository.
2.  On your hosting provider, connect to your Git repository.
3.  Set the **Publish directory** to the root of your project (`/`) and leave the **Build command** empty.
4.  Deploy the site. Your map will be live.
