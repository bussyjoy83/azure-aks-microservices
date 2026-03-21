# Cloud-Native Microservices with AKS Deployment

This project demonstrates the end-to-end deployment of a containerized microservices application on Azure Kubernetes Service (AKS) using Docker for containerization, Azure Container Registry (ACR) for image management, and Terraform for Infrastructure as Code (IaC) provisioning.

The solution reflects real-world cloud-native design principles, emphasizing scalability, modularity, and automated infrastructure deployment.

The application is built using a three-tier microservices architecture:

- **Frontend** – HTML/CSS web application serving the user interface
- **Backend** – Python REST API handling business logic and service communication
- **Database** – PostgreSQL relational database for persistent storage


## Infrastructure Components

Azure Kubernetes Service (AKS) for container orchestration
Azure Container Registry (ACR) for secure image storage
Terraform for declarative infrastructure provisioning
Docker for container build and packaging

## Deployment Guide

### Build Docker Images


docker build -t bussyjoy01.azurecr.io/frontend:v1

docker build -t bussyjoy01.azurecr.io/backend:v2

Built images
![docker image](docs/docker%20image.png)


## Push Images to Azure Container Registry


docker build -t bussyjoy01.azurecr.io/frontend:v1

docker build -t bussyjoy01.azurecr.io/backend:v2

Images in ACR
![image in acr1](docs/images%20in%20acr1.png)

![images in acr2](docs/images%20in%20acr2.png)


## Provisioned Azure Kubernetes Services (AKS) with Terraform

terraform plan
![terraform plan](docs/terraform%20plan.png)

terraform apply
![terraform apply](docs/terraform%20apply.png)

### Deploy to Kubernetes

- Apply the Kubernetes manifests in order:
- kubectl apply -f k8s/database/
- kubectl apply -f k8s/backend/
- kubectl apply -f k8s/frontend/


## AKS Nodes and Pods After deployment

kubectl get nodes
![kubectl get nodes](docs/kubectl%20get%20nodes.png)

kubectl get pods
![kubectl get pods](docs/kubectl%20get%20pods.png)

## Service Access

- Frontend: Exposed via LoadBalancer (External IP)
- Backend: Internal ClusterIP service
- Database: Internal ClusterIP service


Service IPs
![service ips](docs/service%20ips.png)

## Application Access

Browser image
![browser image](docs/browser%20image.png)

## Key Skills Demonstrated

- Azure Kubernetes Service (AKS)
- Azure Container Registry (ACR)
- Docker & Containerization
- Kubernetes (Deployments, Services, Namespaces)
- Infrastructure as Code with Terraform
- Microservices Architecture
- Cloud Networking & Load Balancing


## Repository Structure

```
azure-aks-microservices
├── README.md
├── backend
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── docs
│   ├── Browser image.png
│   ├── Images in ACR.png
│   ├── Screenshot 2026-02-13 113229.png
│   ├── Service IPs.png
│   ├── docker image.png
│   ├── kubectl get deployments.png
│   ├── kubectl get nodes.png
│   ├── kubectl get pods.png
│   ├── kubectl get svc.png
│   ├── terraform apply.png
│   ├── terraform plan.png
│   └── tree.png
├── frontend
│   ├── Dockerfile
│   ├── health.html
│   └── index.html
├── k8s
│   ├── backend
│   │   ├── backend-deployment.yaml
│   │   └── backend-service.yaml
│   ├── database
│   │   ├── postgres-deployment.yaml
│   │   ├── postgres-pvc.yaml
│   │   ├── postgres-secret.example.yaml
│   │   ├── postgres-secret.yaml
│   │   └── postgres-service.yaml
│   ├── frontend
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── namespaces.yaml
└── terraform
    ├── acr.tf
    ├── main.tf
    ├── outputs.tf
    ├── provider.tf
    ├── terraform.tfstate
    ├── terraform.tfstate.backup
    ├── terraform.tfvars
    └── variables.tf


Author
Oloye Busayo

Azure Cloud Engineer

Certifications

•  Ms-900 - Microsoft 365 fundamantals
•  AZ-900 - Microsoft Azure Fundamentals
•  AZ-104 - Microsoft Azure Administrator in view

