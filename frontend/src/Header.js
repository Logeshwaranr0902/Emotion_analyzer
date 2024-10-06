import React from 'react';
import DarkModeIcon from '@mui/icons-material/DarkMode';
import DarkModeOutlinedIcon from '@mui/icons-material/DarkModeOutlined';

const Header = ({ onNightModeToggle, isNightMode }) => {
    return (
        <header className={`sticky top-0 flex justify-between items-center p-4 ${isNightMode ? 'bg-gray-800' : 'bg-gray-700'} transition-colors duration-300`}>
            <div className="flex flex-col items-start">
                <h1 className={`text-2xl font-bold text-white absolute`}>Emotion Analyzer</h1>
                <p className={`text-md mt-8 ml-[8rem]  text-white`}>By Logeshwaran</p> {/* Add this line */}
            </div>
            <div className="flex items-center">
                <button onClick={onNightModeToggle} className="text-white">
                    {isNightMode ? <DarkModeIcon /> : <DarkModeOutlinedIcon />}
                </button>
            </div>
        </header>
    );
};

export default Header;
