FROM python:3.11

# install curl for healthcheck
RUN apt-get update && apt-get install -y curl

COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY main.py .
CMD ["uvicorn", "--port", "5000","--host", "0.0.0.0", "main:app"]