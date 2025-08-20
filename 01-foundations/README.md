# Part 01: Foundations - From Model to System

Build a minimal RAG microservice with FastAPI and React UI. This is your first step into building production-ready AI systems.

## 🎯 What You'll Build

A complete RAG (Retrieval-Augmented Generation) system with:
- **FastAPI Backend**: `/embed`, `/search`, `/answer` endpoints
- **React Frontend**: Search interface with real-time results
- **Vector Search**: FAISS-based similarity search
- **Production Ready**: Docker Compose + CloudFormation deployment

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React UI      │    │   FastAPI       │    │   FAISS         │
│   (Port 3000)   │◄──►│   (Port 8000)   │◄──►│   Vector Store  │
│                 │    │                 │    │                 │
│ • Search Box    │    │ • /embed        │    │ • Index         │
│ • Results       │    │ • /search       │    │ • Search        │
│ • Sources       │    │ • /answer       │    │ • Persistence   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📁 Project Structure

```
parts/01-foundations/
├── app/
│   ├── main.py              # FastAPI application
│   ├── models.py            # Pydantic models
│   └── dependencies.py      # Dependency injection
├── src/
│   └── rag_basic/
│       ├── __init__.py
│       ├── chunker.py       # Text chunking
│       ├── embedder.py      # Sentence transformers
│       └── faiss_store.py   # Vector store
├── web/
│   ├── package.json
│   ├── src/
│   │   ├── App.tsx
│   │   ├── components/
│   │   └── hooks/
│   └── public/
├── cfn/
│   └── stack.yaml           # CloudFormation template
├── tests/
│   ├── test_api.py
│   └── test_rag.py
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- AWS CLI (for cloud deployment)

### Local Development

1. **Clone and navigate**
   ```bash
   cd 01-foundations
   ```

2. **Start services**
   ```bash
   docker compose up
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Cloud Deployment

1. **Deploy to AWS**
   ```bash
   aws cloudformation deploy \
     --template-file cfn/stack.yaml \
     --stack-name applied-ai-part01 \
     --capabilities CAPABILITY_IAM \
     --parameter-overrides \
       Environment=production \
       DomainName=your-domain.com
   ```

2. **Access deployed application**
   - Frontend: https://your-domain.com
   - API: https://api.your-domain.com

## 📊 API Endpoints

### POST /embed
Embed text chunks into vector store
```json
{
  "texts": ["chunk 1", "chunk 2", "chunk 3"],
  "metadata": [{"source": "doc1"}, {"source": "doc2"}]
}
```

### POST /search
Search for similar documents
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

### Configuration File
```yaml
# config.yaml
app:
  name: "rag-foundations"
  version: "1.0.0"

llm:
  provider: "openai"
  model: "gpt-4"
  max_tokens: 1000

vector_store:
  type: "faiss"
  dimension: 1536
  index_path: "./data/faiss_index"

chunking:
  chunk_size: 1000
  chunk_overlap: 200
```

## 🧪 Testing

### Run Tests
```bash
# Unit tests
pytest tests/

# Integration tests
pytest tests/ -m integration

# API tests
pytest tests/test_api.py -v
```

### Test Coverage
```bash
pytest --cov=app --cov=src tests/
```

## 📈 Metrics & Monitoring

### What to Measure

#### Performance
- **Latency**: p50/p95 response times for each endpoint
- **Throughput**: requests per second
- **Resource Usage**: CPU, memory, disk I/O

#### Quality
- **Recall@k**: How many relevant documents are retrieved
- **Answer Relevance**: Human evaluation of answer quality
- **Source Attribution**: Accuracy of source citations

#### Cost
- **Tokens per Query**: Input + output tokens
- **Cost per Query**: $/request breakdown
- **Monthly Forecast**: Projected costs at scale

### Monitoring Setup
```python
# Example metrics collection
from prometheus_client import Counter, Histogram

request_counter = Counter('rag_requests_total', 'Total RAG requests')
request_duration = Histogram('rag_request_duration_seconds', 'Request duration')
```

## 🔒 Security Considerations

### Data Protection
- No PHI/PII in training data
- Input validation and sanitization
- Rate limiting on API endpoints

### Access Control
- API key authentication
- CORS configuration
- Request logging and monitoring

## 🚨 Troubleshooting

### Common Issues

1. **FAISS Index Not Found**
   ```bash
   # Create index directory
   mkdir -p data/
   ```

2. **CORS Errors**
   ```python
   # Update CORS settings in main.py
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:3000"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

3. **Memory Issues**
   ```bash
   # Increase Docker memory limit
   docker compose up --memory=4g
   ```

## 📚 Next Steps

After completing Part 01, you'll be ready for:
- **Part 02**: Data ingest and cleaning pipeline
- **Part 03**: Multiple vector store implementations
- **Part 04**: Orchestration framework comparison

## 🤝 Contributing

Found a bug or have an improvement? 
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

MIT License - see [LICENSE](../LICENSE) for details.
