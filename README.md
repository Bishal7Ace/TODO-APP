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
