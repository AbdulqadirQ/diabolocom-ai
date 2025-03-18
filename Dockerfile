FROM python:3.12-slim
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

COPY src ./src
EXPOSE 8000

RUN useradd app
RUN chown app:app -R /usr/local/app /home
USER app

RUN export LD_LIBRARY_PATH=`python3 -c 'import os; import nvidia.cublas.lib; import nvidia.cudnn.lib; print(os.path.dirname(nvidia.cublas.lib.__file__) + ":" + os.path.dirname(nvidia.cudnn.lib.__file__))'`

CMD ["fastapi", "run", "src/main.py"]