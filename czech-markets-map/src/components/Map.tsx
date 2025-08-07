import { useEffect, useMemo, useRef } from 'react';
import { useSelector } from 'react-redux';
import { useAppDispatch } from '../store';
import { FeatureCollection, Feature, Geometry } from 'geojson';
import { MapContainer, TileLayer, GeoJSON, Marker, Popup } from 'react-leaflet';
import { useTranslation } from 'react-i18next';
import 'leaflet/dist/leaflet.css';
import 'leaflet.markercluster/dist/MarkerCluster.css';
import 'leaflet.markercluster/dist/MarkerCluster.Default.css';
import { RootState } from '../store';
import { fetchMapData, selectRegion, selectSupermarket } from '../features/mapSlice';
import { Region, Supermarket } from '../types';
import L from 'leaflet';

const Map = () => {
  const { t } = useTranslation();
  const dispatch = useAppDispatch();
  const { regions, supermarkets, selectedRegion, loading, error } = useSelector(
    (state: RootState) => state.map
  );

  useEffect(() => {
    dispatch(fetchMapData());
  }, [dispatch]);

  const getColor = (price: number): string => {
    return price > 100000 ? '#67000d' :
           price > 80000 ? '#a50f15' :
           price > 60000 ? '#de2d26' :
           price > 50000 ? '#fb6a4a' :
           price > 40000 ? '#fc9272' :
           price > 30000 ? '#fcbba1' :
                          '#fee5d9';
  };

  const supermarketIcon = L.divIcon({
    html: '<div style="background-color: #2196F3; width: 10px; height: 10px; border-radius: 50%; border: 2px solid white; box-shadow: 0 0 3px rgba(0,0,0,0.4);"></div>',
    className: 'supermarket-marker',
    iconSize: [14, 14],
    iconAnchor: [7, 7]
  });

  const regionStyle = (feature: any) => {
    const region = regions.find(r => r.name === feature.properties.NAME_1);
    return {
      fillColor: getColor(region?.averagePrice || 0),
      weight: 2,
      opacity: 1,
      color: 'white',
      dashArray: '3',
      fillOpacity: 0.85
    };
  };

  const onEachRegion = (feature: any, layer: L.Layer) => {
    const region = regions.find(r => r.name === feature.properties.NAME_1);
    if (region) {
      layer.bindPopup(`
        <div class="font-sans p-2">
          <h3 class="text-lg font-bold mb-2">${region.name}</h3>
          <div class="text-sm">
            <strong>${t('averagePrice')}:</strong><br />
            <span class="text-red-600 text-base font-bold">
              ${region.averagePrice.toLocaleString()} ${t('currency')}/m²
            </span>
          </div>
        </div>
      `);

      layer.on({
        mouseover: (e) => {
          const layer = e.target;
          layer.setStyle({
            weight: 5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.9
          });
        },
        mouseout: (e) => {
          const layer = e.target;
          layer.setStyle(regionStyle(feature));
        },
        click: () => {
          dispatch(selectRegion(region.id));
        }
      });
    }
  };

  const mapContent = useMemo(() => (
    <MapContainer
      center={[49.8175, 15.4730]}
      zoom={7}
      style={{ height: '100vh', width: '100%' }}
    >
      <TileLayer
        url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>'
      />
      
      {regions.length > 0 && (
        <GeoJSON
          data={{
            type: 'FeatureCollection',
            features: regions.map(region => ({
              type: 'Feature',
              properties: region.properties,
              geometry: region.geometry
            }))
          } as FeatureCollection<Geometry>}
          style={regionStyle}
          onEachFeature={onEachRegion}
        />
      )}

      {/* Markers will be added via useEffect */}
      {supermarkets.map((supermarket: Supermarket) => (
        <Marker
          key={supermarket.id}
          position={[supermarket.location[1], supermarket.location[0]]}
          icon={supermarketIcon}
        >
          <Popup>
            <div className="font-sans p-1">
              <strong>{supermarket.name}</strong><br />
              {supermarket.city}
            </div>
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  ), [regions, supermarkets, t]);

  if (loading) {
    return <div className="h-screen flex items-center justify-center">{t('loading')}</div>;
  }

  if (error) {
    return <div className="h-screen flex items-center justify-center text-red-600">{error}</div>;
  }

  return (
    <div className="relative h-screen">
      {mapContent}
    </div>
  );
};

export default Map;
