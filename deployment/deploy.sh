#!/bin/bash

kubectl create -f kubernetes/mongodb-secret.yaml
kubectl create -f kubernetes/mongodb.yaml
kubectl create -f kubernetes/mongodb-configmap.yaml
kubectl create -f kubernetes/transcription-app.yaml
