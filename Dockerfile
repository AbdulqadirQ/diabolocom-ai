# EXPLANATION: To avoid using alpine and installing python on-top, this base image is used
# EXPLANATION: I'd like to improve this using a multi-stage build since the image is so big! (~4GB!)
FROM python:3.12-slim
WORKDIR /usr/local/app

COPY requirements.txt ./
# EXPLANATION: no-cache used to avoid any builds using old assets
RUN pip install --no-cache-dir -r ./requirements.txt

COPY src ./src
EXPOSE 8000

# EXPLANATION: running contianer as a non-privileged user to avoid access to kernal
RUN useradd app
# EXPLANATION: user requires access to these directories
RUN chown app:app -R /usr/local/app /home
USER app

# EXPLANATION: this is required by the model based on the docs, and errors without it
RUN export LD_LIBRARY_PATH=`python3 -c 'import os; import nvidia.cublas.lib; import nvidia.cudnn.lib; print(os.path.dirname(nvidia.cublas.lib.__file__) + ":" + os.path.dirname(nvidia.cudnn.lib.__file__))'`

# EXPLANATION: fastapi is run in production mode instead of 'dev'
CMD ["fastapi", "run", "src/main.py"]