import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';
import 'tailwindcss/tailwind.css';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';



function App({ nightMode }) {
  const [file, setFile] = useState(null);
  const [chartData, setChartData] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) {
      alert("Please upload a file!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      const data = Object.keys(response.data).map(key => ({
        name: key,
        count: response.data[key],
      }));
      setChartData(data);
    } catch (error) {
      console.error("There was an error uploading the file!", error);
    } finally {
      setLoading(false);
    }
  };

  const handleInfoClick = () => {
    alert(`File Format : CSV \nAll the comments/text should be in the first column with coulmn header as "text" `);
  };

  return (
    <div className={`min-h-screen flex flex-col  ${nightMode ? 'bg-gray-900 text-white' : 'bg-gray-100 text-black'}`}>
      <div className="flex flex-col items-center  justify-center mt-[8rem]">
        <h1 className="text-7xl font-bold mb-6">Emotion Analyzer</h1>

        <div className="flex flex-col items-center">
          <div className='flex items-center'>
            <input
              type="file"
              accept=".csv"
              onChange={handleFileChange}
              className="mb-4 p-2 border rounded"
            />
            <button onClick={handleInfoClick} className="ml-2 mb-4">
              <InfoOutlinedIcon />
            </button>
          </div>
          <button
            onClick={handleSubmit}
            className="bg-blue-500 text-white px-4 py-2 rounded "
          >
            {loading ? 'Processing...' : 'Analyze Emotions'}
          </button>
        </div>

        {chartData.length > 0 && (
          <BarChart
            width={600}
            height={300}
            data={chartData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
            className="mt-6"
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count" fill="#8884d8" />
          </BarChart>
        )}
      </div>
    </div>
  );
}

export default App;
