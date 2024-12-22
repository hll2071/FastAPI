FROM python:3.10

WORKDIR /fastapi

COPY . /fastapi

COPY .env /fastapi/.env


EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
