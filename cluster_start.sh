#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Start the Kubernetes cluster using kind
minikube start

# load the location_finder_image:latest image into the cluster
minikube image load location_finder_image:latest

# Apply the Kubernetes configuration files
kubectl apply -f deployments.yaml
kubectl apply -f services.yaml
kubectl apply -f prometheus-config.yaml

# Wait for the pods to be ready before trying to access the service.
# This prevents a race condition where the service is accessed before the pods are running.
kubectl wait --for=condition=ready pod -l app=location-finder --timeout=180s

# start the services
minikube service location-finder-bcd2-service
echo "Kubernetes cluster started and services deployed successfully!"