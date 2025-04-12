✅ TODO-APP
A powerful and visually appealing task management app built with Django, Tailwind CSS, and SQLite. Designed for productivity, packed with features, and secured with authentication.

🚀 Features
💡 Personalized Dashboards
Each user has their own task board — see only what matters to you.

📦 Category-Based Organization
Separate tasks into categories like Work, Personal, or Urgent for easy management.

🗓️ Due Date & Deadline Tracking
Never miss a task — track deadlines and due dates with ease.

📱 Tailwind-Powered UI
Mobile-first, responsive, and clean interface powered by Tailwind CSS.

📊 Smart Stats
Visual breakdowns of your task data to keep you informed and motivated.

🔐 Auth-Ready
Full authentication system: Login, Register, Logout, and protected routes.

🛠 Tech Stack
Backend: Django 3.2, Python 3.8+

Frontend: Tailwind CSS

Database: SQLite

Authentication: Django built-in auth

Others: Breeze-inspired UI flow

📂 Project Structure
bash
Copy
Edit
├── category/             # Task categories
├── login_registration/   # Auth views and forms
├── media/avatars/        # User profile images
├── profiles/             # User profile management
├── theme/                # Tailwind theme and static files
├── todoapp/              # Main Django app settings
├── todolist/             # Core task management logic
├── db.sqlite3            # SQLite database
└── manage.py             # Django project runner
🧪 How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/Bishal7Ace/TODO-APP.git
cd TODO-APP
Create a virtual environment:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run migrations:

bash
Copy
Edit
python manage.py migrate
Start the server:

bash
Copy
Edit
python manage.py runserver
Access at http://127.0.0.1:8000/

📸 Screenshots
Add some UI screenshots here (optional but great for visual impact)


📄 License
MIT License
