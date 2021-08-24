FROM python:3.9
WORKDIR .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--root-path", "/api"]