FROM python:3.13-slim

WORKDIR /app

# Install uv for dependency management
RUN pip install uv

COPY . ./

RUN uv pip install --system -e .
RUN chmod +x entrypoint.py

ENV PYTHONPATH=/app/src:$PYTHONPATH

ENTRYPOINT ["uv", "run", "./entrypoint.py"]
