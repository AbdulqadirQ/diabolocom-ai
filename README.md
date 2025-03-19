# How to run
## Pre-requisites
1. existing Kubernetes cluster with `kubectl` installed

## Deployment
1. From the root of the repository and within a Kubernetes cluster, run `source deployment/deploy.sh`
2. If using minikube, run the following which should open the webpage in your browser: `minikube service transcription-service`.

    Otherwise, type `kubectl get svc transcription-service`, and enter the `EXTERNAL-IP` with the external port into your browser. For example:
    ```
    NAME                    TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
    transcription-service   LoadBalancer   10.98.58.17   192.168.0.80     8000:30001/TCP   12s
    ```
    Here the URI `192.168.0.80:30001` can be entered into a browser
3. The API base URL can now be used with the `/docs` endpoint to access the easy-to-use fastapi documentation for trying out each of the endpoints

NOTE: unfortunately the front-end does not connect with the API within docker containers, so isn't operational just yet. However please see 'Running Transcription Frontend natively' below to understand how it should work.

## Teardown
1. To destroy the deployment, run the following from the root of the repository: `source deployment/teardown.sh`

# Development
## Buildng and running Docker image
- The docker image can be built using the following from the root of the repository: `docker build -t ghcr.io/abdulqadirq/diabolocom-ai:latest .`

- The docker image can be run using the following from the root of the repository: `docker run -d -p 8000:8000 ghcr.io/abdulqadirq/diabolocom-ai:latest`

## Running Transcription app natively
The following steps can be taken from the root of the repository to run the app natively:
1. `pip install -r requirements.txt`
2.  ```
    docker run -d --name mongodb \
    -e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
    -e MONGO_INITDB_ROOT_PASSWORD=secret \
    -p 27017:27017 \
    mongo:8.0.5-noble
    ```
3.  ```
    export LD_LIBRARY_PATH=`python3 -c 'import os; import nvidia.cublas.lib; import nvidia.cudnn.lib; print(os.path.dirname(nvidia.cublas.lib.__file__) + ":" + os.path.dirname(nvidia.cudnn.lib.__file__))'`
    ```
4. `fastapi dev main.py`

## Running Transcription Frontend natively
The following steps can be taken from the /frontend directory to run the frontend natively:
1. `pip install -r requirements.txt`
2. `export API_BASE_URL=<MY_API_BASE_URL>`
3. `streamlit run src/frontend.py`

# Ideal Improvements
1. Fix front-end of application
2. Pytest for testing api endpoints
3. Add additional logging
4. Use of strong typing within python code
5. Run scripts in dry-run mode by default, and add flag for --no-dry-run
6. Change the API docker build into a multi-stage build due to the large size
7. Use DNS for a more friendly service URL
8. Add REST API validation & error logging
9. Experiment and set resource limits for containers
