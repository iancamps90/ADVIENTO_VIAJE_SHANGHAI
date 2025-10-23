import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import { apiCall, API_CONFIG } from './config/api';

function App() {
  const [backendStatus, setBackendStatus] = useState<string>('Checking...');
  const [backendUrl, setBackendUrl] = useState<string>('');

  useEffect(() => {
    // Set the backend URL for display
    setBackendUrl(API_CONFIG.BASE_URL);
    
    // Test backend connection
    const testBackend = async () => {
      try {
        // Replace with your actual API endpoint
        const response = await apiCall('/api/health');
        setBackendStatus('✅ Connected to Railway backend');
      } catch (error) {
        setBackendStatus('❌ Backend connection failed');
        console.error('Backend test failed:', error);
      }
    };

    testBackend();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Shanghai Frontend</h1>
        <p>
          Frontend deployed on Vercel
        </p>
        <div style={{ margin: '20px 0', padding: '10px', backgroundColor: '#f0f0f0', borderRadius: '5px', color: '#333' }}>
          <p><strong>Backend URL:</strong> {backendUrl}</p>
          <p><strong>Status:</strong> {backendStatus}</p>
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
