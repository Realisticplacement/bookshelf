# Bookshelf 📚

A production-ready backend for a digital eBook platform built with Django and Django REST Framework (DRF). It provides catalog management, role-based access control (RBAC), secure file uploads/downloads, user reviews, and download logging.

---

## Features

- **Hybrid Authentication**: Email/password registration with a unique `username` profile.
- **Role-Based Access Control (RBAC)**:
  - **Reader**: Browse catalog, securely download files, and leave ratings/reviews.
  - **Librarian**: All Reader capabilities plus create books and manage only books/files they uploaded.
  - **Admin (Superuser)**: Full global control over metadata, configuration, and audit logs.
- **Relational Catalog Management**: Models for `Book`, `Author`, `Category`, `Series`, and `Tag`, with performance tuned via `select_related` and `prefetch_related`.
- **Secure File Delivery**: Accepts only `.pdf` and `.epub`, updates atomic download counters, and logs user download history.
- **Documentation Ready**: Organized with standard DRF patterns and compatible with OpenAPI/Swagger tooling.

---

## Tech Stack

- **Framework**: Django
- **API Engine**: Django REST Framework (DRF)
- **Database**: SQLite (development) — PostgreSQL compatible
- **Authentication**: Token-based (`rest_framework.authtoken`)

---

## Architecture & Project Structure

The project is split into modular Django apps to separate concerns:

```text
├── accounts/    # Custom user model, registration, authentication
├── books/       # Book, Author, Category, Series, Tag models and APIs
├── files/       # eBook uploads, validation, downloads, counters
└── reviews/     # Ratings, comments, and review-related APIs
```

Below is a concise directory of the active API endpoints (copyable into README.md).

---

### Complete API Endpoints Directory

#### Accounts & Authentication (`accounts` app)

Manual routes for authentication and profile management.

| HTTP Method | Endpoint | Description | Access |
| --- | --- | --- | --- |
| POST | /api/auth/register/ | Register account (email, username, password, role) | Public |
| POST | /api/auth/login/ | Exchange email + password for an auth token | Public |

#### Catalog Management (`books` app)

Exposed via DRF routers and viewsets.

| HTTP Method | Endpoint | Description | Access |
| --- | --- | --- | --- |
| GET | /api/books/ | List books (supports filtering) | Public / Reader |
| POST | /api/books/ | Create a book | Librarian / Admin |
| GET | /api/books/{id}/ | Retrieve book metadata | Public / Reader |
| PUT | /api/books/{id}/ | Replace a book | Owner Librarian / Admin |
| PATCH | /api/books/{id}/ | Partially update a book | Owner Librarian / Admin |
| DELETE | /api/books/{id}/ | Delete a book | Owner Librarian / Admin |

##### Authors

| HTTP Method | Endpoint | Description | Access |
| --- | --- | --- | --- |
| GET | /api/books/authors/ | List authors | Public / Reader |
| POST | /api/books/authors/ | Create an author | Librarian / Admin |
| GET/PUT/PATCH/DELETE | /api/books/authors/{id}/ | Manage an author | Librarian / Admin |

##### Categories

| HTTP Method | Endpoint | Description | Access |
| --- | --- | --- | --- |
| GET | /api/books/categories/ | List categories | Public / Reader |
| POST | /api/books/categories/ | Create a category | Librarian / Admin |
| GET/PUT/PATCH/DELETE | /api/books/categories/{id}/ | Manage a category | Librarian / Admin |

##### Series

| HTTP Method | Endpoint | Description | Access |
| --- | --- | --- | --- |
| GET | /api/books/series/ | List series | Public / Reader |
| POST | /api/books/series/ | Create a series | Librarian / Admin |
| GET/PUT/PATCH/DELETE | /api/books/series/{id}/ | Manage a series | Librarian / Admin |

##### Tags

| HTTP Method | Endpoint | Description | Access |
| --- | --- | --- | --- |
| GET | /api/books/tags/ | List tags | Public / Reader |
| POST | /api/books/tags/ | Create a tag | Librarian / Admin |
| GET/PUT/PATCH/DELETE | /api/books/tags/{id}/ | Manage a tag | Librarian / Admin |

#### File Controls & Tracking (`files` app)

Binary attachments, custom download actions, and download history.

| HTTP Method | Endpoint | Description | Access |
| --- | --- | --- | --- |
| GET | /api/files/ | List file records | Librarian / Admin |
| POST | /api/files/ | Upload `.pdf` / `.epub` (linked to Book) | Owner Librarian / Admin |
| GET/PUT/PATCH/DELETE | /api/files/{id}/ | Manage a file record | Owner Librarian / Admin |
| GET | /api/files/{id}/download/ | Custom download action: serves binary, increments counter, logs history | Authenticated |
| GET | /api/files/history/ | View account download history (Admins see all) | Authenticated / Admin |

#### Reviews & Community Ratings (`reviews` app)

Crowdsourced ratings and feedback.

| HTTP Method | Endpoint | Description | Access |
| --- | --- | --- | --- |
| GET | /api/reviews/ | List reviews | Public / Reader |
| POST | /api/reviews/ | Submit a score (1–5) and comment | Authenticated |
| GET | /api/reviews/{id}/ | Retrieve a review | Public / Reader |
| PUT/PATCH | /api/reviews/{id}/ | Update a personal review | Review Owner |
| DELETE | /api/reviews/{id}/ | Delete a review | Review Owner / Admin |

---

## Permission & Ownership Isolation Layer

The application enforces object-level security to preserve audit integrity:

- **Information isolation**: Authenticated users can view books and access their own downloads. Librarians may modify only objects they uploaded (checked via an `uploaded_by` relation).
- **Download ledger controls**: Users can view only their own download ledger entries; aggregated audit endpoints are restricted to Admin (superuser) roles.
