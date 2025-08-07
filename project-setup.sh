#!/bin/bash

# Create project
mkdir -p czech-markets-map
cd czech-markets-map

# Initialize npm project
npm init -y

# Install dependencies
npm install react react-dom
npm install react-leaflet leaflet @types/leaflet
npm install i18next react-i18next
npm install @reduxjs/toolkit react-redux
npm install axios
npm install @headlessui/react
npm install tailwindcss postcss autoprefixer
npm install leaflet.markercluster @types/leaflet.markercluster
npm install typescript @types/react @types/react-dom
npm install vite @vitejs/plugin-react

# Create project structure
mkdir -p public/locales/en
mkdir -p public/locales/cs
mkdir -p public/locales/uk
mkdir -p public/locales/ru
mkdir -p public/data
mkdir -p src/components
mkdir -p src/features
mkdir -p src/i18n
mkdir -p src/types
mkdir -p src/utils
mkdir -p src/styles

# Copy existing data
cp czech_regions.geojson czech-markets-map/public/data/
cp supermarkets.geojson czech-markets-map/public/data/

# Initialize TypeScript configuration
echo '{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}' > czech-markets-map/tsconfig.json

# Initialize Vite configuration
echo 'import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000
  }
});' > czech-markets-map/vite.config.ts

# Initialize Tailwind CSS
cd czech-markets-map
npx tailwindcss init -p

echo 'module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}' > tailwind.config.js

echo '@tailwind base;
@tailwind components;
@tailwind utilities;' > src/styles/index.css

echo "Project setup completed!"
