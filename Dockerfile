FROM python:3.12
EXPOSE 5000
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
WORKDIR /app
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
