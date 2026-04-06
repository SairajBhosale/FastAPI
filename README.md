# FastAPI Machine Learning API

A RESTful API built with FastAPI for serving machine learning predictions. This project provides a simple, scalable way to deploy ML models as microservices with automatic API documentation.

## Features

- **FastAPI Framework**: High-performance, modern Python web framework
- **ML Model Integration**: Pre-trained machine learning model deployment
- **Docker Support**: Containerized application for easy deployment
- **Automatic Documentation**: Interactive API documentation with Swagger UI
- **City Tier Classification**: Built-in support for city tier categorization
- **Async Support**: Asynchronous request handling for better performance

## Project Structure

```
FastAPI/
├── fastapp.py          # Main FastAPI application
├── predict.py          # Prediction logic and model inference
├── user_input.py       # Input validation and data models
├── city_tier.py        # City tier classification utilities
├── model.pkl           # Pre-trained ML model (pickled)
├── requirements.txt    # Python dependencies
└── Dockerfile         # Docker configuration
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Docker (optional, for containerized deployment)

## Installation

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SairajBhosale/FastAPI.git
   cd FastAPI
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Docker Installation

1. **Build the Docker image**
   ```bash
   docker build -t fastapi-ml-app .
   ```

2. **Run the container**
   ```bash
   docker run -d -p 8000:8000 fastapi-ml-app
   ```

## Usage

### Running the Application

**Local Development:**
```bash
uvicorn fastapp:app --reload --host 0.0.0.0 --port 8000
```

**Production:**
```bash
uvicorn fastapp:app --host 0.0.0.0 --port 8000 --workers 4
```

### Accessing the API

Once the application is running, you can access:

- **API Endpoint**: http://localhost:8000
- **Interactive Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative Documentation (ReDoc)**: http://localhost:8000/redoc

### Example API Request

```python
import requests

url = "http://localhost:8000/predict"
data = {
    # Add your input data here based on your model requirements
}

response = requests.post(url, json=data)
print(response.json())
```

**Using cURL:**
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"key": "value"}'
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check / Welcome message |
| POST | `/predict` | Make predictions using the ML model |
| GET | `/docs` | Interactive API documentation |

## Configuration

Key configuration parameters can be adjusted in the main application file or through environment variables:

- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `WORKERS`: Number of worker processes (production)
- `MODEL_PATH`: Path to the trained model file

## Model Information

The API uses a pre-trained machine learning model stored in `model.pkl`. The model accepts structured input data and returns predictions based on the trained algorithm.

### Input Schema

Refer to `user_input.py` for the complete input schema and validation rules.

### City Tier Classification

The application includes city tier classification functionality in `city_tier.py`, which can be used for geographical segmentation and analysis.

## Testing

Run tests using pytest:

```bash
pytest tests/
```

For coverage report:
```bash
pytest --cov=. tests/
```

## Performance

FastAPI provides excellent performance characteristics:
- High throughput with async/await support
- Automatic request validation
- Efficient JSON serialization
- Low latency response times

## Docker Deployment

The included `Dockerfile` provides a production-ready container configuration. Key features:

- Optimized Python base image
- Proper dependency caching
- Non-root user execution
- Health check configuration

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Guidelines

- Follow PEP 8 style guidelines
- Add type hints to function signatures
- Write docstrings for all public functions
- Include unit tests for new features
- Update documentation as needed

## Security Considerations

- Validate all input data using Pydantic models
- Implement rate limiting for production deployments
- Use environment variables for sensitive configuration
- Keep dependencies up to date
- Follow OWASP API security best practices

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Sairaj Bhosale**
- GitHub: [@SairajBhosale](https://github.com/SairajBhosale)

## Acknowledgments

- FastAPI framework by Sebastián Ramírez
- Uvicorn ASGI server
- Pydantic for data validation
- The Python community

## Support

For issues, questions, or contributions, please:
- Open an issue on GitHub
- Contact the repository maintainer

## Version History

- **v1.0.0** - Initial release with basic ML model deployment

---

**Note**: Make sure to update the model file, input schema, and prediction logic according to your specific use case before deploying to production.

**This README is AI generated**
