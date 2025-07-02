Event Management WebApp
===========================

A full-featured Event Management Web Application built with Django! This platform allows users to create, manage, and browse events — perfect for community organizers, business events, and more.

Developed by @nueladesope (https://github.com/nueladesope)

---

Features
-----------

- 📝 Event creation & editing  
- 📅 Browse upcoming events  
- 🔍 Search/filter events by date or keyword  
- 🔐 User authentication and registration  
- 🖼️ Upload event images (media support)  
- ⚙️ Admin dashboard for managing users & events

---

🛠️ Tech Stack
--------------

- Backend: Django (Python)  
- Frontend: HTML, CSS, JavaScript (Bootstrap or similar)  
- Database: SQLite (default) or PostgreSQL  
- Templating Engine: Django Templates  
- Authentication: Django's built-in auth system

---

🚀 Getting Started
-------------------

Follow these steps to run the project locally:

1. Clone the Repository
git clone https://github.com/nueladesope/event-management-webapp.git
cd event-management-webapp


2. Set Up a Virtual Environment
python -m venv env
source env/bin/activate # On Windows: env\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt


4. Configure Environment Variables

Create a `.env` file in the root directory and add the following (if using python-decouple or django-environ):
  
DEBUG=True
SECRET_KEY=your_django_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3 # or your PostgreSQL URI


5. Run Migrations
python manage.py makemigrations
python manage.py migrate

6. Create a Superuser (admin)
python manage.py createsuperuser


7. Run the Development Server
python manage.py runserver
Then visit: http://127.0.0.1:8000

---

📁 Project Structure
--------------------
event-management-webapp/

├── events/ # Core event app (models, views, forms)

├── templates/ # HTML templates

├── static/ # CSS, JS, images

├── manage.py

└── README.md


🗂️ Environment & Tools
------------------------

- Python 3.9+  
- Django 4.x  
- Virtualenv or Pipenv  
- SQLite or PostgreSQL  
- Bootstrap (for frontend UI)

🔧 Future Improvements
-----------------------

- ✅ RSVP system for event attendees  
- ✅ Email notifications/reminders  
- ✅ User profiles with avatars  
- ✅ Pagination and filtering  
- ✅ Calendar view integration

🤝 Contributing
----------------

Contributions are welcome!

1. Fork the repo  
2. Create a new branch (`git checkout -b feature/my-feature`)  
3. Commit your changes (`git commit -am 'Add feature'`)  
4. Push to your branch (`git push origin feature/my-feature`)  
5. Create a Pull Request 🚀

🙌 Acknowledgements
---------------------

- Django (https://www.djangoproject.com/)  
- Bootstrap (https://getbootstrap.com/)  
- Font Awesome (https://fontawesome.com/)  
- SQLite (https://www.sqlite.org/)

  ---

⭐️ Show your support
----------------------

If you like this project, give it a ⭐️ on GitHub and share it with others!
