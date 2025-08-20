# Datasets

This directory contains datasets used throughout the Building Applied AI Systems series.

## Structure

```
datasets/
├── synthetic/          # Generated synthetic data for testing
├── public/            # Public datasets with proper licensing
└── licenses/          # Dataset licenses and attribution
```

## Data Sources

### Synthetic Data
- **Purpose**: Testing and development without privacy concerns
- **Generation**: Scripts in `tools/data-generation/`
- **Format**: JSON, CSV, Parquet
- **Use Cases**: Unit tests, integration tests, demos

### Public Datasets
- **Medical**: PubMed abstracts, clinical trial data
- **Technical**: Documentation, code repositories
- **General**: News articles, academic papers
- **Licensing**: All datasets include proper attribution and licensing

## Usage Guidelines

1. **Synthetic Data**: Safe for all use cases, no restrictions
2. **Public Data**: 
   - Check individual dataset licenses
   - Include proper attribution
   - Respect usage terms
3. **Never Include**: 
   - PHI (Protected Health Information)
   - PII (Personally Identifiable Information)
   - Proprietary or confidential data

## Adding New Datasets

1. Create a subdirectory in `public/` or `synthetic/`
2. Include a `README.md` with:
   - Source and license information
   - Data format and schema
   - Usage examples
3. Add to this index
4. Update `licenses/` directory if needed

## Dataset Index

### Synthetic
- `medical-qa/` - Synthetic medical Q&A pairs
- `code-docs/` - Generated code documentation
- `clinical-notes/` - Synthetic clinical notes (no PHI)

### Public
- `pubmed-abstracts/` - PubMed article abstracts
- `clinical-trials/` - Clinical trial metadata
- `medical-textbooks/` - Open access medical textbooks

## License Compliance

All datasets in this repository comply with:
- MIT License (for synthetic data)
- Original dataset licenses (for public data)
- No PHI/PII included
- Proper attribution maintained

## Data Generation Scripts

See `tools/data-generation/` for scripts to:
- Generate synthetic medical data
- Create test datasets
- Validate data quality
- Convert between formats
