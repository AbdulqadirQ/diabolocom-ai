#!/bin/bash

kubectl create -f kubernetes/mongodb-secret.yaml
kubectl create -f kubernetes/mongodb.yaml
kubectl create -f kubernetes/app-configmap.yaml
kubectl create -f kubernetes/transcription-app.yaml
kubectl create -f kubernetes/transcription-frontend.yaml
