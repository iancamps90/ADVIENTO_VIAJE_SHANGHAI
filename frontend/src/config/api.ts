// API Configuration for Shanghai Frontend
const backend = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';

export const API_CONFIG = {
  BASE_URL: backend,
  ENDPOINTS: {
    // Add your API endpoints here
    CALENDAR: '/api/calendar',
    DAYS: '/api/days',
    CONTENT: '/api/content',
    // Add more endpoints as needed
  }
};

// Axios instance configuration
export const apiClient = {
  baseURL: API_CONFIG.BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
};

// Helper function to make API calls
export const apiCall = async (endpoint: string, options: RequestInit = {}) => {
  const url = `${API_CONFIG.BASE_URL}${endpoint}`;
  
  const defaultOptions: RequestInit = {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  };

  try {
    const response = await fetch(url, { ...defaultOptions, ...options });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API call failed:', error);
    throw error;
  }
};
