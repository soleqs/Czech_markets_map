import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

export const languageOptions = {
  en: { code: 'en', name: 'English', nativeName: 'English' },
  cs: { code: 'cs', name: 'Czech', nativeName: 'Čeština' },
  uk: { code: 'uk', name: 'Ukrainian', nativeName: 'Українська' },
  ru: { code: 'ru', name: 'Russian', nativeName: 'Русский' }
};

i18n
  .use(initReactI18next)
  .init({
    fallbackLng: 'en',
    resources: {
      en: {
        translation: {
          title: 'Czech Republic Property Market & Supermarkets',
          subtitle: 'Housing prices by region and supermarket locations',
          pricePerMeter: 'Price per m²',
          supermarketLocations: 'Supermarket Locations',
          region: 'Region',
          averagePrice: 'Average Price',
          selectLanguage: 'Select Language',
          loading: 'Loading...',
          error: 'Error loading data',
          currency: 'CZK'
        }
      },
      cs: {
        translation: {
          title: 'Realitní trh a supermarkety v České republice',
          subtitle: 'Ceny bydlení podle regionů a umístění supermarketů',
          pricePerMeter: 'Cena za m²',
          supermarketLocations: 'Umístění supermarketů',
          region: 'Kraj',
          averagePrice: 'Průměrná cena',
          selectLanguage: 'Vyberte jazyk',
          loading: 'Načítání...',
          error: 'Chyba při načítání dat',
          currency: 'Kč'
        }
      },
      uk: {
        translation: {
          title: 'Ринок нерухомості та супермаркети Чехії',
          subtitle: 'Ціни на житло за регіонами та розташування супермаркетів',
          pricePerMeter: 'Ціна за м²',
          supermarketLocations: 'Розташування супермаркетів',
          region: 'Регіон',
          averagePrice: 'Середня ціна',
          selectLanguage: 'Виберіть мову',
          loading: 'Завантаження...',
          error: 'Помилка завантаження даних',
          currency: 'Крон'
        }
      },
      ru: {
        translation: {
          title: 'Рынок недвижимости и супермаркеты Чехии',
          subtitle: 'Цены на жилье по регионам и расположение супермаркетов',
          pricePerMeter: 'Цена за м²',
          supermarketLocations: 'Расположение супермаркетов',
          region: 'Регион',
          averagePrice: 'Средняя цена',
          selectLanguage: 'Выберите язык',
          loading: 'Загрузка...',
          error: 'Ошибка загрузки данных',
          currency: 'Крон'
        }
      }
    },
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
