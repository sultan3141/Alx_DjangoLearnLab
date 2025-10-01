# Django Blog Project

## Overview
A simple blog application built with Django, featuring user authentication and full CRUD post management.

## User Authentication
- **Register**: `/register` → create a new account.
- **Login**: `/login` → log in with username & password.
- **Profile**: `/profile` → view/edit profile (email, username).
- **Logout**: `/logout` → logout securely.

## Blog Post Management (CRUD)
- **List Posts**: `/posts/` → anyone can view posts.
- **Post Detail**: `/posts/<id>/` → view full post.
- **Create Post**: `/posts/new/` → authenticated users only.
- **Edit Post**: `/posts/<id>/edit/` → only author can edit.
- **Delete Post**: `/posts/<id>/delete/` → only author can delete.

### Permissions
- Login required for create/edit/delete.
- Only post authors can modify their posts.

## Static Files
- CSS: `blog/static/css/styles.css`
- JS: `blog/static/js/scripts.js`
- Templates: `blog/templates/blog/`

## How to Run
```bash
python manage.py migrate
python manage.py runserver
