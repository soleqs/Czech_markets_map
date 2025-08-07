import { Suspense } from 'react';
import { Provider } from 'react-redux';
import { store } from './store';
import { useTranslation } from 'react-i18next';
import './i18n/config';
import Map from './components/Map';
import LanguageSelector from './components/LanguageSelector';
import './styles/index.css';

const App = () => {
  const { t } = useTranslation();

  return (
    <Provider store={store}>
      <Suspense fallback={<div>Loading...</div>}>
        <div className="relative">
          <div className="absolute top-4 left-4 z-10">
            <LanguageSelector />
          </div>
          <div className="absolute top-4 left-1/2 transform -translate-x-1/2 z-10 bg-white bg-opacity-90 px-6 py-3 rounded-lg shadow-lg text-center">
            <h1 className="text-xl font-bold text-gray-800">{t('title')}</h1>
            <p className="text-sm text-gray-600 mt-1">{t('subtitle')}</p>
          </div>
          <Map />
        </div>
      </Suspense>
    </Provider>
  );
};

export default App;
