FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install pytest
CMD ["python3", "calculator.py"]
