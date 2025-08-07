import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import axios from 'axios';
import { MapState, Region, Supermarket } from '../types';

const initialState: MapState = {
  regions: [],
  supermarkets: [],
  selectedRegion: null,
  selectedSupermarket: null,
  loading: false,
  error: null,
};

export const fetchMapData = createAsyncThunk(
  'map/fetchData',
  async () => {
    const [regionsResponse, supermarketsResponse] = await Promise.all([
      axios.get('/data/czech_regions.geojson'),
      axios.get('/data/supermarkets.geojson')
    ]);

    return {
      regions: regionsResponse.data.features.map((feature: any) => ({
        id: feature.properties.NAME_1,
        name: feature.properties.NAME_1,
        properties: feature.properties,
        geometry: feature.geometry,
        averagePrice: getRegionPrice(feature.properties.NAME_1)
      })),
      supermarkets: supermarketsResponse.data.features.map((feature: any) => ({
        id: feature.properties.id || String(Math.random()),
        name: feature.properties.name || 'Supermarket',
        city: feature.properties.city || '',
        location: feature.geometry.coordinates
      }))
    };
  }
);

const getRegionPrice = (regionName: string): number => {
  const prices: { [key: string]: number } = {
    "Prague": 124900,
    "Středočeský": 75000,
    "Jihočeský": 67600,
    "Plzeňský": 65000,
    "Karlovarský": 45000,
    "Ústecký": 42000,
    "Liberecký": 71000,
    "Královéhradecký": 69000,
    "Pardubický": 64000,
    "KrajVysočina": 58000,
    "Jihomoravský": 102000,
    "Olomoucký": 61000,
    "Zlínský": 59000,
    "Moravskoslezský": 48000
  };
  return prices[regionName] || 0;
};

export const mapSlice = createSlice({
  name: 'map',
  initialState,
  reducers: {
    selectRegion: (state, action: PayloadAction<string | null>) => {
      state.selectedRegion = action.payload;
    },
    selectSupermarket: (state, action: PayloadAction<string | null>) => {
      state.selectedSupermarket = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchMapData.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchMapData.fulfilled, (state, action) => {
        state.loading = false;
        state.regions = action.payload.regions;
        state.supermarkets = action.payload.supermarkets;
      })
      .addCase(fetchMapData.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Failed to load map data';
      });
  },
});

export const { selectRegion, selectSupermarket } = mapSlice.actions;

export default mapSlice.reducer;
