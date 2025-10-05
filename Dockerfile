# Gunakan base image yang ringan
FROM python:3.11-slim

# Set environment variable agar Python tidak membuat file .pyc dan buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install dependencies sistem minimal
RUN apt-get update && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Salin file requirements terlebih dahulu (untuk cache layer)
COPY source/requirements.txt .
COPY source/.env .


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file setelah install requirements (lebih efisien untuk rebuild)
COPY source .

# Perintah untuk menjalankan aplikasi
CMD ["python", "main.py"]