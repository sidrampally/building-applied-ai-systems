import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

// Types
interface SearchResult {
  text: string;
  metadata: any;
  score: number;
  index: number;
}

interface AnswerResponse {
  answer: string;
  sources: string[];
  question: string;
}

function App() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');
  const [sources, setSources] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

  const handleSearch = async () => {
    if (!query.trim()) {
      setError('Please enter a question');
      return;
    }

    setLoading(true);
    setError('');
    setAnswer('');
    setSources([]);

    try {
      // Step 1: Search for relevant documents
      const searchResponse = await axios.post(`${API_BASE_URL}/search`, {
        query: query,
        top_k: 5
      });

      const searchResults: SearchResult[] = searchResponse.data.results;
      
      if (searchResults.length === 0) {
        setError('No relevant documents found');
        setLoading(false);
        return;
      }

      // Step 2: Generate answer using RAG
      const context = searchResults.map(result => result.text);
      const answerResponse = await axios.post(`${API_BASE_URL}/answer`, {
        question: query,
        context: context,
        search_results: searchResults
      });

      const answerData: AnswerResponse = answerResponse.data;
      
      setAnswer(answerData.answer);
      setSources(answerData.sources);

    } catch (err: any) {
      console.error('Error:', err);
      setError(err.response?.data?.detail || 'An error occurred while processing your request');
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !loading) {
      handleSearch();
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>RAG Foundations</h1>
        <p>Ask questions about your documents</p>
      </header>

      <main className="App-main">
        <div className="search-container">
          <div className="input-group">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Ask a question..."
              className="search-input"
              disabled={loading}
            />
            <button 
              onClick={handleSearch}
              disabled={loading || !query.trim()}
              className="search-button"
            >
              {loading ? 'Searching...' : 'Search'}
            </button>
          </div>
        </div>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>Processing your question...</p>
          </div>
        )}

        {answer && (
          <div className="results">
            <div className="answer-section">
              <h3>Answer:</h3>
              <div className="answer-text">
                {answer}
              </div>
            </div>

            {sources.length > 0 && (
              <div className="sources-section">
                <h3>Sources:</h3>
                <ul className="sources-list">
                  {sources.map((source, index) => (
                    <li key={index} className="source-item">
                      {source}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </main>

      <footer className="App-footer">
        <p>Part 01: Foundations - Building Applied AI Systems</p>
      </footer>
    </div>
  );
}

export default App;
