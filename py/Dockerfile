FROM python:3.12-slim

# Linux dependencies for building and running the project
RUN echo "Updating apt-get and installing Linux dependencies..."
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

#  Default Python dependencies library installation
RUN if [ -f requirements.txt ]; then \
        echo "Installing Python dependencies from requirements.txt"; \
        pip install --no-cache-dir -r requirements.txt; \
        echo "Generating requirements.lock file"; \
        python -m pip freeze > requirements.lock; \
    fi

EXPOSE 60100

CMD [""]