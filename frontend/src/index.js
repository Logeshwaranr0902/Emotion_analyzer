import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Header from './Header';
import Footer from './Footer';

const root = ReactDOM.createRoot(document.getElementById('root'));

const Main = () => {
  const [isNightMode, setIsNightMode] = useState(false);

  const toggleNightMode = () => {
    setIsNightMode(prevMode => !prevMode);
    document.body.classList.toggle('dark', !isNightMode);
  };

  return (
    <React.StrictMode>
      <Header onNightModeToggle={toggleNightMode} isNightMode={isNightMode} />
      <App nightMode={isNightMode} />
      <Footer />
    </React.StrictMode>
  );
};

root.render(<Main />);
