# Alx Django LearnLab – Social Media API

A Django REST Framework–based social media API with authentication, posts, and notifications.  
Deployed live on **Render**.

---

## 🚀 Live Demo

The project is deployed on Render and can be accessed here:  
👉 [Alx Django LearnLab – Live Deployment](https://alx-djangolearnlab1.onrender.com)

---

## 🔎 Features

- **Accounts App**
  - User registration (`/accounts/register/`)
  - Login with token authentication (`/accounts/login/`)
  - Profile view & update (`/accounts/profile/`)
  - Follow / Unfollow users

- **Posts App**
  - Create, list, and manage posts

- **Notifications App**
  - Real‑time notifications when users follow each other

- **Admin Panel**
  - `/admin/` for managing users, posts, and notifications

---

## ⚠️ Notes

- This is an **API‑only backend**. Endpoints like `/accounts/login/` expect a **POST request** with JSON data (username & password).  
  If you visit them directly in the browser, you’ll see a `405 Method Not Allowed` message.
- Use tools like **Postman**, **cURL**, or a frontend client to interact with the API.
- Since this is a free Render instance, the server may take **30–50 seconds to “wake up”** after inactivity.

---

## 📌 Example Usage

### Register
```bash
curl -X POST https://alx-djangolearnlab1.onrender.com/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "sultan", "password": "test1234"}'
