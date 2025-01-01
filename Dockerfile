FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install uv
RUN uv install
COPY . ./
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

