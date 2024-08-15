# Stoic - Database Modeling Document

## Introduction

This document outlines the database modeling for the "Stoic" application. It includes the entities, relationships, and their attributes required for managing user diaries.

## Entities and Attributes

### 1. User
- **user_id** (PK): Unique identifier for the user.
  - **Constraints**: Primary Key (PK)
  - **Type**: Integer
  - **Default**: Auto-incremented
- **username**: User's chosen username.
  - **Constraints**: Unique, Not Null
  - **Type**: String
  - **Default**: None
- **email**: User's email address.
  - **Constraints**: Unique, Not Null
  - **Type**: String
  - **Default**: None
- **password_hash**: Encrypted password for user authentication.
  - **Constraints**: Not Null
  - **Type**: String
  - **Default**: None
- **first_name**: User's first name.
  - **Constraints**: Nullable
  - **Type**: String
  - **Default**: None
- **last_name**: User's last name.
  - **Constraints**: Nullable
  - **Type**: String
  - **Default**: None
- **profile_picture**: URL or path to the user's profile picture.
  - **Constraints**: Nullable
  - **Type**: String
  - **Default**: None
- **bio**: A short biography or description provided by the user.
  - **Constraints**: Nullable
  - **Type**: Text
  - **Default**: None
- **created_at**: Date and time when the user profile was created.
  - **Constraints**: Not Null
  - **Type**: Timestamp
  - **Default**: Current timestamp
- **updated_at**: Date and time when the user profile was last updated.
  - **Constraints**: Not Null
  - **Type**: Timestamp
  - **Default**: Current timestamp

### 2. Role
- **id** (PK): Unique identifier for each role.
  - **Constraints**: Primary Key (PK)
  - **Type**: Integer
  - **Default**: Auto-incremented
- **name**: Name of the role (e.g., Admin, User).
  - **Constraints**: Not Null
  - **Type**: String
  - **Default**: None

### 3. Diary
- **diary_id** (PK): Unique identifier for each diary.
  - **Constraints**: Primary Key (PK)
  - **Type**: Integer
  - **Default**: Auto-incremented
- **user_id** (FK): Foreign key referencing the user who owns the diary.
  - **Constraints**: Foreign Key (FK)
  - **Type**: Integer
  - **Default**: None
- **year**: Year of the diary.
  - **Constraints**: Not Null
  - **Type**: Integer
  - **Default**: None
- **title**: Title of the diary.
  - **Constraints**: Not Null
  - **Type**: String
  - **Default**: None
- **created_at**: Date and time when the diary was created.
  - **Constraints**: Not Null
  - **Type**: Timestamp
  - **Default**: Current timestamp
- **updated_at**: Date and time when the diary was last updated.
  - **Constraints**: Not Null
  - **Type**: Timestamp
  - **Default**: Current timestamp

### 4. Page
- **page_id** (PK): Unique identifier for each page.
  - **Constraints**: Primary Key (PK)
  - **Type**: Integer
  - **Default**: Auto-incremented
- **diary_id** (FK): Foreign key referencing the diary to which the page belongs.
  - **Constraints**: Foreign Key (FK)
  - **Type**: Integer
  - **Default**: None
- **title**: Title of the page.
  - **Constraints**: Not Null
  - **Type**: String
  - **Default**: None
- **date**: Date associated with the page (e.g., a specific date for daily pages).
  - **Constraints**: Nullable
  - **Type**: Date
  - **Default**: None
- **created_at**: Date and time when the page was created.
  - **Constraints**: Not Null
  - **Type**: Timestamp
  - **Default**: Current timestamp
- **updated_at**: Date and time when the page was last updated.
  - **Constraints**: Not Null
  - **Type**: Timestamp
  - **Default**: Current timestamp

### 5. Entry
- **entry_id** (PK): Unique identifier for each entry.
  - **Constraints**: Primary Key (PK)
  - **Type**: Integer
  - **Default**: Auto-incremented
- **page_id** (FK): Foreign key referencing the page where the entry is located.
  - **Constraints**: Foreign Key (FK)
  - **Type**: Integer
  - **Default**: None
- **content**: Content of the entry.
  - **Constraints**: Not Null
  - **Type**: Text
  - **Default**: None
- **tags**: Tags associated with the entry (stored as a list or JSON).
  - **Constraints**: Nullable
  - **Type**: JSON or String
  - **Default**: None
- **created_at**: Date and time when the entry was created.
  - **Constraints**: Not Null
  - **Type**: Timestamp
  - **Default**: Current timestamp
- **updated_at**: Date and time when the entry was last updated.
  - **Constraints**: Not Null
  - **Type**: Timestamp
  - **Default**: Current timestamp

### 6. Category
- **category_id** (PK): Unique identifier for each category.
  - **Constraints**: Primary Key (PK)
  - **Type**: Integer
  - **Default**: Auto-incremented
- **user_id** (FK): Foreign key referencing the user who created the category.
  - **Constraints**: Foreign Key (FK)
  - **Type**: Integer
  - **Default**: None
- **name**: Name of the category.
  - **Constraints**: Not Null
  - **Type**: String
  - **Default**: None

### 7. Tag
- **tag_id** (PK): Unique identifier for each tag.
  - **Constraints**: Primary Key (PK)
  - **Type**: Integer
  - **Default**: Auto-incremented
- **user_id** (FK): Foreign key referencing the user who created the tag.
  - **Constraints**: Foreign Key (FK)
  - **Type**: Integer
  - **Default**: None
- **name**: Name of the tag.
  - **Constraints**: Not Null
  - **Type**: String
  - **Default**: None

### 8. Entry_Category (Join Table)
- **entry_id** (FK): Foreign key referencing an entry.
  - **Constraints**: Foreign Key (FK)
  - **Type**: Integer
  - **Default**: None
- **category_id** (FK): Foreign key referencing a category.
  - **Constraints**: Foreign Key (FK)
  - **Type**: Integer
  - **Default**: None

### 9. Entry_Tag (Join Table)
- **entry_id** (FK): Foreign key referencing an entry.
  - **Constraints**: Foreign Key (FK)
  - **Type**: Integer
  - **Default**: None
- **tag_id** (FK): Foreign key referencing a tag.
  - **Constraints**: Foreign Key (FK)
  - **Type**: Integer
  - **Default**: None

## Relationships

### User - Role
- **Type**: Many-to-One (N:1)
- **Description**: Many users can have a single role.

### User - Diary
- **Type**: One-to-Many (1:N)
- **Description**: A user can own multiple diaries.

### Diary - Page
- **Type**: One-to-Many (1:N)
- **Description**: A diary can contain multiple pages.

### Page - Entry
- **Type**: One-to-Many (1:N)
- **Description**: A page can have multiple entries.

### Entry - Category
- **Type**: Many-to-Many (N:N)
- **Description**: An entry can belong to multiple categories, and a category can have multiple entries.

### Entry - Tag
- **Type**: Many-to-Many (N:N)
- **Description**: An entry can have multiple tags, and a tag can be associated with multiple entries.

## Glossary
- **Diary**: A collection of pages for storing entries.
- **Page**: A section within a diary used to organize entries.
- **Entry**: A single note or piece of content within a page.

