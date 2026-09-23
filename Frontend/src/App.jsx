import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [newsList, setNewsList] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetching data from Node.js backend API
    axios.get('http://localhost:5000/api/news')
      .then((response) => {
        setNewsList(response.data.news || []);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching news in frontend:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', backgroundColor: '#f4f4f9', minHeight: '100vh', padding: '20px' }}>
      <header style={{ textAlign: 'center', marginBottom: '40px', borderBottom: '2px solid #ddd', paddingBottom: '20px' }}>
        <h1 style={{ color: '#333', fontSize: '2.5rem' }}>📰 Timeline News</h1>
        <p style={{ color: '#666' }}>Your Live BBC News Pulse Dashboard</p>
      </header>

      {loading ? (
        <h2 style={{ textAlign: 'center', color: '#666' }}>Loading fresh news articles...</h2>
      ) : (
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          {newsList.length === 0 ? (
            <p style={{ textAlign: 'center' }}>No news articles found in the database.</p>
          ) : (
            newsList.map((news) => (
              <div key={news.id} style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
                <h3 style={{ margin: '0 0 15px 0', color: '#0070f3' }}>
                  <a href={news.link} target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none', color: 'inherit' }}>
                    {news.title}
                  </a>
                </h3>
                <p style={{ color: '#444', lineHeight: '1.6' }}>{news.description}</p>
                <small style={{ color: '#999', display: 'block', marginTop: '10px' }}>
                  Fetched on: {new Date(news.created_at).toLocaleString()}
                </small>
              </div>
            ))
          )}
        </div>
      )}
    </div>
  );
}

export default App;
