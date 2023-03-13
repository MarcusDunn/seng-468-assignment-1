FROM python:3.11

COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY main.py .
CMD ["python", "main.py"]
