# ⚙️ Service Management Python  

<h1 align="center">Hello 👋, I'm Alfredo</h1>  
<h3 align="center">Welcome To Service Management Python 🚀</h3>  

> Proyek ini adalah implementasi **Service Management** menggunakan **Python**.  
> Tujuannya untuk mengelola layanan (jobs, tasks, services) dengan mudah, dapat diintegrasikan dengan database, API, maupun sistem monitoring.  

---

## ✨ Features
- 📌 CRUD untuk manajemen service/job  
- 🗄️ Integrasi database (MongoDB, PostgreSQL)  
- ⚡ Dibangun dengan **Python 3.12+**  
- 🔧 Konfigurasi fleksibel menggunakan file `.env`  
- 🛠️ Struktur modular (config, service, controller)  

---

## 📦 Requirements  

- [Python](https://www.python.org/) **v3.12.3+**  
- Database & API sesuai kebutuhan  

---

## ⚙️ Installation  

Clone repo ini dan install dependency:  

```bash
# Clone repository
git clone https://github.com/dwiptrdo/svc-management.git

# Masuk ke direktori proyek
cd svc-management

# Install dependencies
pip install -r requirements.txt
```

## 🔑 Setup Environment

Buat file .env di root proyek dengan format berikut (sesuaikan kebutuhan):

```bash
ACCESS_TOKEN_EXPIRE_MINUTES=<00>
ALGORITHM=<algoritma>
SECRET_KEY=<secret_key>
MONGO_DB_NAME=<dbname>
MONGO_URL=mongodb://localhost:localhost100@localhost:1234/
POSTGRES_URL=postgresql://user:password@localhost:5432/mydb
PORT=1234
```

## ▶️ Run Project

Jalankan aplikasi dengan perintah:
```bash
python3 main.py
```

Jika menggunakan Uvicorn/FastAPI untuk REST API service:
```bash
uvicorn main:app --reload
```

## 📂 Project Structure
```
📦 svc-management
 ┣ 📂config     
 ┃ ┣ 📜db.py
 ┃ ┗ 📜env.py
 ┣ 📂controller 
 ┃ ┣ 📜article_controller.py
 ┃ ┗ 📜user_controller.py
 ┣ 📂middleware    
 ┃ ┗ 📜auth.py
 ┣ 📂models    
 ┃ ┣ 📜article_model.py
 ┃ ┣ 📜user_model.py
 ┃ ┗ 📜model.py
 ┣ 📂service      
 ┃ ┣ 📜article_service.py
 ┃ ┗ 📜user_service.py
 ┣ 📂utils      
 ┃ ┗ 📜utils.py
 ┗ 📜main.py    
```
## Author

👤 **dwiptrdo**


- Github: [@dwiptrdo](https://github.com/dwiptrdo)
- Instagram: [@_dwiptrdo](https://www.instagram.com/_dwiptrdo/)