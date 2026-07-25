FROM python:3.12-slim

WORKDIR /app

# Instala uv
RUN pip install uv

COPY pyproject.toml uv.lock ./

# Instala dependências usando uv
RUN uv sync --frozen

COPY . .

CMD ["uv", "run", "python", "src/main.py"]