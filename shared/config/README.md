# Shared Configuration

This directory contains configuration patterns and templates used across all parts of the Building Applied AI Systems series.

## Structure

```
shared/config/
├── environments/      # Environment-specific configurations
├── templates/         # Configuration templates
└── README.md         # This file
```

## Configuration Philosophy

### Config-First Approach
- **Environment Variables**: For secrets and environment-specific values
- **YAML Configs**: For structured configuration
- **Templates**: For generating environment-specific configs
- **Validation**: All configs validated at startup

### Common Patterns

#### 1. Environment Configuration
```yaml
# config.yaml
app:
  name: "applied-ai-system"
  version: "1.0.0"
  environment: "${ENVIRONMENT:-development}"

llm:
  provider: "${LLM_PROVIDER:-openai}"
  model: "${LLM_MODEL:-gpt-4}"
  api_key: "${LLM_API_KEY}"

vector_store:
  type: "${VECTOR_STORE_TYPE:-faiss}"
  config:
    dimension: 1536
    index_path: "${VECTOR_INDEX_PATH:-./data/faiss_index}"
```

#### 2. Feature Flags
```yaml
features:
  caching: "${ENABLE_CACHING:-true}"
  monitoring: "${ENABLE_MONITORING:-true}"
  safety_filters: "${ENABLE_SAFETY_FILTERS:-true}"
  cost_tracking: "${ENABLE_COST_TRACKING:-true}"
```

#### 3. Service Configuration
```yaml
services:
  api:
    host: "${API_HOST:-0.0.0.0}"
    port: "${API_PORT:-8000}"
    workers: "${API_WORKERS:-1}"
  
  web:
    host: "${WEB_HOST:-localhost}"
    port: "${WEB_PORT:-3000}"
```

## Environment Templates

### Development
- Local services (Docker Compose)
- Debug logging
- Mock external services
- Fast iteration

### Staging
- Cloud infrastructure
- Production-like data
- Full monitoring
- Integration testing

### Production
- High availability
- Security hardening
- Performance optimization
- Compliance features

## Configuration Validation

All configurations are validated using Pydantic:

```python
from pydantic import BaseSettings, Field

class AppConfig(BaseSettings):
    name: str = Field(..., description="Application name")
    version: str = Field(..., description="Application version")
    environment: str = Field(default="development", description="Environment")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
```

## Security Considerations

### Secrets Management
- **Local**: `.env` files (never committed)
- **Cloud**: AWS Secrets Manager, Parameter Store
- **Validation**: No secrets in logs or configs

### Environment Isolation
- Separate configs per environment
- No cross-environment data sharing
- Proper access controls

## Usage Examples

### Loading Configuration
```python
from shared.config import load_config

config = load_config("config.yaml")
llm_provider = config.llm.provider
```

### Environment-Specific Overrides
```python
# Override for specific environment
config = load_config("config.yaml", environment="production")
```

### Validation
```python
# Validate configuration at startup
config = load_config("config.yaml")
config.validate()
```

## Best Practices

1. **Default Values**: Always provide sensible defaults
2. **Environment Variables**: Use for secrets and environment-specific values
3. **Validation**: Validate all configurations at startup
4. **Documentation**: Document all configuration options
5. **Security**: Never commit secrets or sensitive data
6. **Testing**: Test configuration loading and validation
7. **Migration**: Version configuration schemas for backward compatibility

## Configuration Files

### Required Files
- `config.yaml` - Main configuration
- `.env.example` - Environment variable template
- `validation.py` - Configuration validation

### Optional Files
- `config.dev.yaml` - Development overrides
- `config.staging.yaml` - Staging overrides
- `config.prod.yaml` - Production overrides
