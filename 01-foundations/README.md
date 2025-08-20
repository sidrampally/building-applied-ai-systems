# Part 01: Foundations - From Model to System

> **Part of the "Building Applied AI Systems" Blog Series**  
> Learn to build production-ready AI systems step by step, from basic RAG to enterprise deployment.

Build a minimal RAG (Retrieval-Augmented Generation) system with FastAPI backend and React frontend. This foundation will prepare you for more advanced AI system patterns in the upcoming blog posts.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- OpenAI API key

### Run the System

1. **Set up environment**
   ```bash
   cp env.example .env
   # Edit .env with your OpenAI API key
   ```

2. **Start services**
   ```bash
   docker compose up
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - API Docs: http://localhost:8000/docs

4. **Add sample data**
   - Go to http://localhost:8000/docs
   - Use the `/embed` endpoint to add documents
   - Try the sample drug data in `sample_drug_data.json`

## 🎯 What You Get

- **Document embedding** into FAISS vector database
- **Semantic search** with similarity scoring  
- **RAG-powered answers** using GPT-4
- **Source attribution** with real filenames
- **Interactive UI** for testing and demos

## 📊 API Endpoints

### POST /embed
Add documents to the knowledge base
```json
{
  "texts": ["chunk 1", "chunk 2", "chunk 3"],
  "metadata": [{"source": "doc1"}, {"source": "doc2"}]
}
```

### POST /search
Find relevant document chunks
```json
{
  "query": "What is machine learning?",
  "top_k": 5
}
```

### POST /answer
Generate answer using RAG
```json
{
  "question": "What is machine learning?",
  "context": ["relevant doc 1", "relevant doc 2"]
}
```

## 🔧 Configuration

### Environment Variables
```bash
# LLM Configuration
LLM_PROVIDER=openai
LLM_MODEL=gpt-4
LLM_API_KEY=your-api-key

# Vector Store
VECTOR_STORE_TYPE=faiss
VECTOR_INDEX_PATH=./data/faiss_index

# Application
API_HOST=0.0.0.0
API_PORT=8000
WEB_HOST=localhost
WEB_PORT=3000
```

## 🧪 Testing

### Run Tests
```bash
# Unit tests
pytest tests/

# API tests
pytest tests/test_api.py -v
```

## 📈 What to Measure

### Performance
- **Latency**: p50/p95 response times for each endpoint
- **Throughput**: requests per second
- **Resource Usage**: CPU, memory, disk I/O

### Quality
- **Recall@k**: How many relevant documents are retrieved
- **Answer Relevance**: Human evaluation of answer quality
- **Source Attribution**: Accuracy of source citations

### Cost
- **Tokens per Query**: Input + output tokens
- **Cost per Query**: $/request breakdown
- **Monthly Forecast**: Projected costs at scale

## 🔒 Security Considerations

- No PHI/PII in training data
- Input validation and sanitization
- Rate limiting on API endpoints
- API key authentication

## 🚨 Troubleshooting

### Common Issues

1. **FAISS Index Not Found**
   ```bash
   mkdir -p data/
   ```

2. **CORS Errors**
   - Check that frontend is running on http://localhost:3000
   - Verify CORS settings in main.py

3. **Memory Issues**
   ```bash
   docker compose up --memory=4g
   ```

## 📚 Next in the Series

- **Part 02**: Data ingest and cleaning pipeline  
- **Part 03**: Multiple vector store implementations
- **Part 04**: Orchestration framework comparison
- **Part 05**: Amazon Bedrock AgentCore for Enterprise AI Agents

## 📄 License

MIT License - see [LICENSE](../LICENSE) for details.
