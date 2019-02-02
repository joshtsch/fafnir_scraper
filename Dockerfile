FROM python:3.7.2
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT ["python"]
