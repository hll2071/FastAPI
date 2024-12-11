FROM python:3.10

WORKDIR /app

COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

EXPOSE 8000


RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]