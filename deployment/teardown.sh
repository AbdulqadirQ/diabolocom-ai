#!/bin/bash

# EXPLANATION: A script for easy teardown of the Kubernetes resources
#              It'd be better to have a --no-dry-run flag for the teardown
#              otherwise the script runs in dry-run mode for checking config
kubectl delete -f kubernetes/transcription-frontend.yaml
kubectl delete -f kubernetes/transcription-app.yaml
kubectl delete -f kubernetes/app-configmap.yaml
kubectl delete -f kubernetes/mongodb.yaml
kubectl delete -f kubernetes/mongodb-secret.yaml
