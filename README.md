# 🐍 Alx Django LearnLab – Backend Development Projects & Practice

This repository contains my **ALX Backend Development practice projects** built with **Python** and **Django REST Framework**.  
It serves as a learning lab where I experiment with APIs, authentication, database modeling, and advanced backend features.

---

## 📂 Repository Structure

Each folder is a standalone Django project or practice module:

- **`social_media_api/`**
  - A mini social media backend with:
    - User registration & login (token authentication)
    - Profile management
    - Follow/unfollow functionality
    - Posts & notifications
  - 🚀 [Live Demo on Render](https://alx-djangolearnlab1.onrender.com)

- **`django_blog/`**
  - A simple blog application
  - CRUD operations for posts
  - User authentication and admin management

- **`api_project/`**
  - Introductory API project
  - Focus on serializers, viewsets, and RESTful design

- **`advanced-api-project/`**
  - More complex API features
  - Pagination, filtering, and permissions

- **`advanced_features_and_security/`**
  - Security best practices
  - Authentication, authorization, and advanced DRF features

---

## 🚀 Live Deployment

The **Social Media API** is deployed on Render:  
👉 [https://alx-djangolearnlab1.onrender.com](https://alx-djangolearnlab1.onrender.com)

⚠️ Note: Free Render instances may take **30–50 seconds to wake up** after inactivity.

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Django 5.x**
- **Django REST Framework**
- **SQLite (dev)** / **PostgreSQL (production)**
- **Render** for deployment

---

## 📌 Example Usage (Social Media API)

### Register
```bash
curl -X POST https://alx-djangolearnlab1.onrender.com/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "sultan", "password": "my45my45"}'
