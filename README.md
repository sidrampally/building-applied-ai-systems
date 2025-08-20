# Building Applied AI Systems

A comprehensive 16-part series where every post ships real code + push-button deploy. Learn to build production-ready AI systems through hands-on implementation.

## 🎯 What You'll Build

Each part delivers a complete, deployable AI system with:
- **Working code** that runs locally and in the cloud
- **Docker Compose** for local development
- **CloudFormation** stacks for AWS deployment
- **Real metrics** and observability
- **Production patterns** that scale

## 📚 Series Overview

### Core Track (Parts 01-16)

| Part | Focus | What You Build |
|------|-------|----------------|
| 01 | Foundations | RAG microservice + React UI |
| 02 | Data Pipeline | Document ingest + PII scrubbing |
| 03 | Vector Stores | FAISS, Weaviate, pgvector adapters |
| 04 | Orchestration | LangChain, LangGraph, Strands, CrewAI, Haystack |
| 05 | Agent Patterns | Planner-executor, toolformer, critique-revise |
| 06 | Enterprise RAG | Caching, re-ranking, structured outputs |
| 07 | Drug Discovery | Literature → candidate pipeline |
| 08 | Clinical Trials | Decentralized trial simulation |
| 09 | Safety & Eval | Llama Guard, red team, PHI protection |
| 10 | Multi-Modal | Vision + speech for clinical notes |
| 11 | MLOps | CI/CD, model registry, canary deployments |
| 12 | Observability | Traces, tokens, cost tracking |
| 13 | Security | Secrets, KMS, data retention |
| 14 | Productization | UX for experts & non-experts |
| 15 | Multi-Cloud | Provider-agnostic LLM routing |
| 16 | Starter Kit | One-click "Applied AI Starter Kit" |

### Advanced Tracks

- **A1**: Advanced Agentic Architectures @ Scale
- **A2**: Retrieval Beyond Text (Graphs, SQL, Function Calling)
- **A3**: Federated & Edge Computing

## 🏗️ Repository Structure

```
building-applied-ai-systems/
├── 01-foundations/                # RAG microservice + React UI
├── 02-data-ingest/                # Document pipeline + PII scrubbing
├── 03-vector-stores/              # FAISS, Weaviate, pgvector
├── 04-orchestration/              # LangChain, LangGraph, etc.
├── 05-agent-patterns/             # Production agent patterns
├── 06-enterprise-rag/             # Advanced RAG with caching
├── 07-hcls-drug-discovery/        # Drug discovery pipeline
├── 08-clinical-trials/            # DCT simulation
├── 09-evaluation-safety/          # Safety & evaluation
├── 10-multimodal/                 # Vision + speech
├── 11-mlops/                      # CI/CD, model registry
├── 12-observability/              # Traces, metrics, cost
├── 13-security/                   # Secrets, KMS, retention
├── 14-productization/             # UX for different users
├── 15-multi-cloud/                # Provider-agnostic routing
├── 16-starter-kit/                # Complete starter kit
├── shared/                        # Common code across parts
│   ├── src/                       # Shared libraries
│   ├── tests/                     # Common test utilities
│   ├── config/                    # Shared configuration
│   └── scripts/                   # Common deployment scripts
├── datasets/                      # Synthetic/public datasets
├── docs/                          # Documentation
├── tools/                         # Development tools
└── advanced/                      # Advanced tracks A1-A3
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- AWS CLI (for cloud deployment)
- Node.js 18+ (for React components)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/building-applied-ai-systems.git
   cd building-applied-ai-systems
   ```

2. **Start with Part 01**
   ```bash
   cd 01-foundations
   docker compose up
   ```

3. **Deploy to AWS**
   ```bash
   aws cloudformation deploy \
     --template-file cfn/stack.yaml \
     --stack-name applied-ai-part01 \
     --capabilities CAPABILITY_IAM
   ```

## 📊 What You'll Learn

### Technical Skills
- **AI/ML**: RAG, embeddings, vector search, agents, multi-modal
- **Backend**: FastAPI, async Python, microservices
- **Frontend**: React, TypeScript, modern UI patterns
- **Infrastructure**: Docker, AWS, CloudFormation, observability
- **Security**: Secrets management, data protection, compliance

### Production Patterns
- **Observability**: Tracing, metrics, cost tracking
- **Reliability**: Caching, fallbacks, error handling
- **Scalability**: Load balancing, auto-scaling, performance
- **Security**: Zero-trust, encryption, access controls
- **MLOps**: Model versioning, A/B testing, canary deployments

## 🎯 Success Metrics

Each part includes specific metrics to measure:
- **Performance**: Latency (p50/p95), throughput, resource usage
- **Quality**: Accuracy, relevance, user satisfaction
- **Reliability**: Uptime, error rates, recovery time
- **Cost**: $/query, resource efficiency, ROI
- **Security**: Compliance, vulnerability scans, data protection

## 🤝 Contributing

This is a learning series - contributions welcome!
- Report bugs or issues
- Suggest improvements
- Add new parts or advanced tracks
- Share your implementations

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🗺️ Roadmap

- [ ] [Part 01: Foundations](01-foundations/) (Week 1)
- [ ] [Part 02: Data Pipeline](02-data-ingest/) (Week 2)
- [ ] [Part 03: Vector Stores](03-vector-stores/) (Week 3)
- [ ] [Part 04: Orchestration](04-orchestration/) (Week 4)
- [ ] [Part 05: Agent Patterns](05-agent-patterns/) (Week 5)
- [ ] [Part 06: Enterprise RAG](06-enterprise-rag/) (Week 6)
- [ ] [Part 07: Drug Discovery](07-hcls-drug-discovery/) (Week 7)
- [ ] [Part 08: Clinical Trials](08-clinical-trials/) (Week 8)
- [ ] [Part 09: Safety & Evaluation](09-evaluation-safety/) (Week 9)
- [ ] [Part 10: Multi-Modal](10-multimodal/) (Week 10)
- [ ] [Part 11: MLOps](11-mlops/) (Week 11)
- [ ] [Part 12: Observability](12-observability/) (Week 12)
- [ ] [Part 13: Security](13-security/) (Week 13)
- [ ] [Part 14: Productization](14-productization/) (Week 14)
- [ ] [Part 15: Multi-Cloud](15-multi-cloud/) (Week 15)
- [ ] [Part 16: Starter Kit](16-starter-kit/) (Week 16)
- [ ] [Advanced Tracks](advanced/) (Ongoing)

---

**Ready to build production AI systems? Start with [Part 01: Foundations](01-foundations/README.md)**
