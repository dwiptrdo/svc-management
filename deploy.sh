#!/bin/bash

# --- KONFIGURASI VPS ---
VPS_USER="vps100"
VPS_HOST="103.197.188.152"
REGISTRY_HOST="103.197.188.152:5110"
VPS_PORT=22
APP_NAME="svc-management"
REMOTE_DIR="/home/vps100/env-path"
TAG="latest"
PORT=61611

# --- BUILD IMAGE SECARA LOKAL ---
echo "🚧 Membuat Docker image..."
docker build -t $APP_NAME .

# --- TAGGING DAN PUSH KE REGISTRY ---
echo "📦 Tagging image ke registry..."
docker tag $APP_NAME:$TAG $REGISTRY_HOST/$APP_NAME:$TAG

echo "🚀 Mengirim image ke registry..."
docker push $REGISTRY_HOST/$APP_NAME:$TAG

# --- KIRIM FILE .env KE VPS ---
echo "📤 Mengirim file .env ke VPS..."
ssh -p $VPS_PORT $VPS_USER@$VPS_HOST "mkdir -p $REMOTE_DIR"
scp -P $VPS_PORT source/.env $VPS_USER@$VPS_HOST:$REMOTE_DIR/$APP_NAME.env

# --- SSH KE VPS UNTUK DEPLOY ---
echo "🛠 Deploying di VPS..."
ssh -p $VPS_PORT $VPS_USER@$VPS_HOST << EOF
sudo docker pull $REGISTRY_HOST/$APP_NAME:$TAG

# Hentikan container lama jika ada
sudo docker rm -f $APP_NAME || true

# Jalankan container baru
sudo docker run -d \
  -p $PORT:$PORT \
  --restart always \
  --name $APP_NAME \
  --env-file $REMOTE_DIR/$APP_NAME.env \
  --log-opt max-size=50m \
  $REGISTRY_HOST/$APP_NAME:$TAG
EOF

echo "✅ Deployment selesai!"