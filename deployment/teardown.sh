#!/bin/bash

kubectl delete -f kubernetes/transcription-app.yaml
kubectl delete -f kubernetes/mongodb-configmap.yaml
kubectl delete -f kubernetes/mongodb.yaml
kubectl delete -f kubernetes/mongodb-secret.yaml
