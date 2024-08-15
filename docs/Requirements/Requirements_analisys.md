# Stoic - Requirements Document

## Introduction

### Purpose
The purpose of this document is to outline the functional and non-functional requirements for the "Stoic" application. "Stoic" is a web application designed to provide users with a secure and intuitive platform for managing personal diaries.

### Scope
"Stoic" will be a web-based application utilizing Vue.js for the frontend, FastAPI for the backend, and Docker for containerization.

### Definitions, Acronyms, and Abbreviations
- **SPA**: Single Page Application
- **API**: Application Programming Interface
- **CRUD**: Create, Read, Update, Delete
- **JWT**: JSON Web Token
- **Docker**: Containerization platform

### References
- IEEE 830: Standard for Software Requirements Specifications
- [Vue.js Documentation](https://vuejs.org/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)

## Overall Description

### Product Perspective
"Stoic" will be a standalone application for diary management with a Vue.js frontend, FastAPI backend, and Docker containerization.

### Product Functions
1. **User Management**
   - Register and authenticate users
   - Password recovery and reset
   - User profile management

2. **Diary Management**
   - Create, edit, delete, and view diaries

3. **Page Management**
   - Create, edit, delete, and view pages within a diary

4. **Entry Management**
   - Write, edit, delete, and view diary entries

5. **Search Functionality**
   - Search entries by keyword

6. **Categorization**
   - Create, manage, and assign categories to entries

7. **Tagging**
   - Create, manage, and assign tags to entries

8. **Export/Import**
   - Export diaries and entries to JSON or PDF
   - Import diaries and entries from JSON or PDF

9. **Security**
   - User authentication with JWT
   - Role-based access control

10. **Notification System**
    - Basic email notifications

### User Classes and Characteristics
- **End Users**: Individuals managing diaries
- **Administrators**: Users managing system settings and user accounts

### Operating Environment
- **Frontend**: Browser-based application using Vue.js
- **Backend**: API service using FastAPI
- **Containerization**: Docker
- **Database**: PostgreSQL or SQLite

### Design and Implementation Constraints
- Containerization using Docker
- Frontend with Vue.js
- Backend with FastAPI

### User Documentation
- **User Manual**: Instructions for end-users
- **API Documentation**: Developer guides for API usage

## Functional Requirements

### User Management
1. Register, login, and logout
2. Password recovery and reset
3. Profile management

### Diary Management
1. Create, edit, delete, and view diaries

### Page Management
1. Create, edit, delete, and view pages

### Entry Management
1. Create, edit, delete, and view entries

### Search Functionality
1. Keyword search

### Categorization
1. Create, manage, and assign categories

### Tagging
1. Create, manage, and assign tags

### Export/Import
1. Export to JSON or PDF
2. Import from JSON or PDF

### Security
1. JWT authentication
2. Role-based access control

### Notification System
1. Basic email notifications

## Non-Functional Requirements

### Performance Requirements
- Handle up to 1000 concurrent users

### Security Requirements
- Encryption of data in transit and storage

### Usability Requirements
- User-friendly interface
- Responsive and accessible frontend

### Reliability Requirements
- 99.9% uptime
- Backup and recovery processes

### Maintainability Requirements
- Modular and well-documented code
- Automated testing

### Portability Requirements
- Docker containerization for deployment

## Appendices

### Glossary
- **Diary**: A collection of pages for storing entries.
- **Page**: A section within a diary used to organize entries.
- **Entry**: A single note or piece of content within a page.

