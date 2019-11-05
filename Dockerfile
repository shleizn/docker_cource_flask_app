FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN apk add --no-cache bash
CMD ["python", "app.py"]