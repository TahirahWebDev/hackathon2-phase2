FROM python:3.11

WORKDIR /code

# Copy requirements or pyproject.toml
COPY ./pyproject.toml /code/pyproject.toml
RUN pip install .

# Copy the rest of the backend code
COPY . /code

# Hugging Face uses port 7860 by default
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "7860"]