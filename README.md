# End-to-End MLOps Pipeline for House Price Prediction

## 📌 Project Overview

This project demonstrates a complete End-to-End MLOps Pipeline for House Price Prediction using Machine Learning, Docker, Kubernetes, CI/CD automation, and monitoring tools.

The objective of this project is to simulate a real-world production ML deployment workflow where:

* A Machine Learning model is trained for house price prediction
* The model is exposed through a FastAPI REST API
* The application is containerized using Docker
* Kubernetes is used for orchestration and deployment
* GitHub Actions automates CI/CD workflows
* Prometheus and Grafana are used for monitoring and visualization

---

# 🚀 Features

* Machine Learning model for house price prediction
* REST API using FastAPI
* Docker containerization
* Kubernetes deployment
* CI/CD pipeline using GitHub Actions
* Docker Hub image push automation
* Monitoring with Prometheus
* Visualization dashboards with Grafana
* Scalable microservice-style deployment

---

# 🧠 Tech Stack

| Category             | Tools/Technologies |
| -------------------- | ------------------ |
| Programming Language | Python             |
| Machine Learning     | Scikit-learn       |
| API Framework        | FastAPI            |
| Containerization     | Docker             |
| Orchestration        | Kubernetes         |
| CI/CD                | GitHub Actions     |
| Monitoring           | Prometheus         |
| Visualization        | Grafana            |
| Container Registry   | Docker Hub         |

---

# 🏗️ Project Architecture

```text
Developer Pushes Code
        ↓
GitHub Actions CI/CD Pipeline
        ↓
Docker Image Build
        ↓
Docker Hub Push
        ↓
Kubernetes Deployment
        ↓
FastAPI Application Running
        ↓
Prometheus Monitoring
        ↓
Grafana Dashboard Visualization
```

---

# 📂 Project Structure

```text
mlops-pipeline/
│
├── .github/workflows/
│   └── main.yml
│
├── api/
│   └── main.py
│
├── docker/
│   └── Dockerfile.api
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── training/
│   ├── train.py
│   ├── retrain_pipeline.py
│   ├── drift_detection.py
│   └── data/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Machine Learning Model

The project uses a Machine Learning model to predict house prices based on:

* Area
* Number of Bedrooms

### ML Workflow

1. Data Loading
2. Data Preprocessing
3. Model Training
4. Model Serialization
5. API Deployment

---

# 🐳 Docker Containerization

The application is containerized using Docker to ensure:

* Environment consistency
* Easy deployment
* Scalability
* Portability across systems

### Build Docker Image

```bash
docker build -t akshaysutar10/mlops-api -f docker/Dockerfile.api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 akshaysutar10/mlops-api
```

---

# ☸️ Kubernetes Deployment

Kubernetes is used to manage container orchestration.

### Kubernetes Features Used

* Deployments
* Pods
* Services
* Replica Management

### Apply Kubernetes Configuration

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Check Running Pods

```bash
kubectl get pods
```

### Check Services

```bash
kubectl get services
```

---

# 🔄 CI/CD Pipeline

GitHub Actions is used to automate:

* Docker image build
* Docker image push
* Continuous Integration workflow

### Workflow Includes

* Checkout Repository
* Docker Login
* Build Docker Image
* Push Image to Docker Hub

---

# 📊 Monitoring with Prometheus & Grafana

## Prometheus

Prometheus collects:

* Application metrics
* Kubernetes metrics
* Pod performance metrics
* System health information

## Grafana

Grafana visualizes:

* CPU usage
* Memory usage
* Pod status
* Node health
* Cluster monitoring dashboards

---

# ▶️ Running the Project

## 1. Clone Repository

```bash
git clone https://github.com/10-Akshay/mlops-pipeline.git
cd mlops-pipeline
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run FastAPI Application

```bash
uvicorn api.main:app --reload
```

## 4. Open API Docs

```text
http://localhost:8000/docs
```

---

# 📈 Monitoring Setup

## Install Monitoring Stack

```bash
helm install monitoring prometheus-community/kube-prometheus-stack
```

## Access Grafana

```bash
kubectl port-forward svc/monitoring-grafana 3000:80
```

Open:

```text
http://localhost:3000
```

---

# 🧪 API Testing

The FastAPI Swagger UI can be used for testing prediction APIs.

### Example Input

```json
{
  "area": 1200,
  "bedrooms": 3
}
```

### Example Output

```json
{
  "predicted_price": 450000
}
```

---

# 🌍 Real-World Use Cases

This architecture is similar to production systems used in:

* Real Estate Platforms
* FinTech Applications
* Recommendation Systems
* Cloud-native ML Platforms
* AI-based Prediction Systems

---

# 📌 Future Improvements

* Real-time data streaming with Kafka
* Automated model retraining
* Cloud deployment on AWS
* Terraform infrastructure automation
* Auto-scaling with Kubernetes HPA
* Advanced alerting system

---

# 👨‍💻 Author

Akshay Sutar

GitHub: [https://github.com/10-Akshay](https://github.com/10-Akshay)

---

# ⭐ Conclusion

This project demonstrates practical implementation of Machine Learning Operations (MLOps) concepts including deployment automation, container orchestration, CI/CD workflows, and monitoring in a production-style environment.
