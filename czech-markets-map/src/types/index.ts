export interface Region {
  id: string;
  name: string;
  averagePrice: number;
  properties: {
    NAME_1: string;
  };
  geometry: any;
}

export interface Supermarket {
  id: string;
  name: string;
  city: string;
  location: [number, number];
}

export interface LanguageOption {
  code: string;
  name: string;
  nativeName: string;
}

export type PriceRange = {
  min: number;
  max: number;
  color: string;
};

export interface MapState {
  regions: Region[];
  supermarkets: Supermarket[];
  selectedRegion: string | null;
  selectedSupermarket: string | null;
  loading: boolean;
  error: string | null;
}
