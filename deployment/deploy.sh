#!/bin/bash

# EXPLANATION: A script for easy deployment of the Kubernetes resources
#              It'd be better to have a --no-dry-run flag for the deployment
#              otherwise the script runs in dry-run mode for checking config
kubectl create -f kubernetes/mongodb-secret.yaml
kubectl create -f kubernetes/mongodb.yaml
kubectl create -f kubernetes/app-configmap.yaml
kubectl create -f kubernetes/transcription-app.yaml
kubectl create -f kubernetes/transcription-frontend.yaml
