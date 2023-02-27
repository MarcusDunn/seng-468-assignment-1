FROM python:3.9-slim-bullseye

# install curl for healthcheck
RUN apt-get update && apt-get install -y curl

COPY venv /opt

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY main.py .
CMD ["uvicorn", "--port", "5000","--host", "0.0.0.0", "main:app"]