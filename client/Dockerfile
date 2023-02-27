FROM python:3.12.0a5-slim-bullseye

COPY venv /opt

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY main.py .
CMD ["python", "main.py"]
