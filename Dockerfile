FROM python:3.9-slim-bookworm
WORKDIR /flask-docker

RUN python3 -m pip install --upgrade pip

COPY requirement.txt requirement.txt

RUN pip3 install -r requirement.txt

COPY . .

CMD ["python3" , "-m", "flask", "run", "--host=0.0.0.0"]

