# ✨ Django TodoList — Track Tasks. Stay Ahead.  
> *Minimalist design, powerful productivity.*  

![Made with Django](https://img.shields.io/badge/Built%20With-Django%203.2-092E20?style=for-the-badge&logo=django&logoColor=white)  
![Made with Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)  
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-Responsive%20Design-38B2AC?style=for-the-badge&logo=tailwind-css)

---

## 🎯 Overview  

This is a full-featured, user-friendly **TodoList web application** that lets individuals manage their daily priorities across different categories. It emphasizes **clarity**, **control**, and **clean design**, making it the perfect starter or showcase project.

Whether you're organizing your personal life or work routine — this app keeps everything on track.

---

## 💡 Highlights  

- 🎟️ **Personalized Dashboards** — All tasks filtered by user  
- 📦 **Category-Based Organization** — Work, Life, and Everything Else  
- 🗓️ **Due Date & Deadline Tracking** — Because time matters  
- 📱 **Tailwind-Powered UI** — Mobile-first and beautifully responsive  
- 📊 **Smart Stats** — Visual insights into your task breakdown  
- 🔐 **Auth-Ready** — Login, Register, and secure routes

---

## 📸 Visual Glimpse
| Dashboard                     | 
|------------------------------|
|  ![20](https://github.com/user-attachments/assets/0b741e5e-c892-4e11-81ab-bbd1c268371f)| 
|  ![21](https://github.com/user-attachments/assets/da669121-df73-4821-9dba-c0e210c34da2)| 
|  ![22](https://github.com/user-attachments/assets/63f2227d-f189-425d-8e87-86535573ca4c)| 
|  ![23](https://github.com/user-attachments/assets/8ec6b48c-46c3-4828-9c7e-56931774884e)| 
|  ![24](https://github.com/user-attachments/assets/944c218b-7e1a-4e76-8002-07b3b0c91163)| 
|  ![25](https://github.com/user-attachments/assets/95c2ff6c-df70-4f9f-956a-a81114e4e85a)| 
|  ![27](https://github.com/user-attachments/assets/b3e2b59f-81bc-4fa4-a4df-fbf622c30e51)| 





---

## 🛠️ Tech Behind the Scenes

| Layer         | Tools/Tech                      |
|---------------|---------------------------------|
| **Backend**   | Django 3.2                      |
| **Database**  | SQLite (dev) / PostgreSQL (prod)|
| **Frontend**  | Tailwind CSS 2.2+               |
| **Auth**      | Django’s default auth system    |


---

## 🧪 Run It Locally

```bash
# Clone it
git clone https://github.com/yourusername/django-todolist-app.git
cd django-todolist-app

# Set up a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows


# Install required packages
pip install -r requirements.txt

# Migrate database & create admin
python manage.py migrate
python manage.py createsuperuser

# Run the app
python manage.py runserver

```
## 🧭 App Flow

```mermaid
graph TD
    A[🟢 User Login/Register] --> B[📋 View Dashboard]
    B --> C[➕ Add Task]
    B --> D[🔍 Filter by Category or Status]
    B --> E[🖊️ Edit / 🗑️ Delete Task]
    C --> F[📅 Assign Due Date]
    F --> G[✅ Mark as Complete]
    G --> H[📊 Task Stats Updated]
