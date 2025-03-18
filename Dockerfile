FROM python:3.12-slim
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

COPY src ./src
EXPOSE 8000

RUN useradd app
RUN chown app:app -R /usr/local/app /home
USER app

CMD ["fastapi", "run", "src/main.py"]