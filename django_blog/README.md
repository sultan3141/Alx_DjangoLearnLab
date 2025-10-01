## User Authentication

- **Register**: `/register` → Create account with username, email, and password.
- **Login**: `/login` → Login with credentials.
- **Profile**: `/profile` → View and update profile details.
- **Logout**: `/logout` → Logout securely.

### Security
- Passwords stored using Django’s hashing system.
- CSRF protection enabled on all forms.
- Only authenticated users can access `/profile`.
