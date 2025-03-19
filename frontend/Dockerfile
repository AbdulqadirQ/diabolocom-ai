# EXPLANATION: very similar to the main API Dockerfile
FROM python:3.12-slim
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

COPY src ./src
# EXPLANATION: an attempt to disable CORS for testing to see if that'd fix the front-end connrection issue
COPY .streamlit/ ./.streamlit/
EXPOSE 8501

RUN useradd app
USER app

CMD ["streamlit", "run", "src/frontend.py"]
