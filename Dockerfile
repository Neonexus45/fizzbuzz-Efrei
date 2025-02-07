FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN pip install pytest
CMD ["unitest", "test.py"]