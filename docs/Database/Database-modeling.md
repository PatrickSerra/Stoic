# Stoic - Database Modeling Document

## Introduction

This document outlines the database modeling for the "Stoic" application. It includes the entities, relationships, and their attributes required for managing user diaries.

## Entities and Attributes

### 1. User
- **id**: `PK` - Unique identifier for each user.
- **username**: Unique - User's username.
- **email**: Unique - User's email address.
- **password**: String - Encrypted password.
- **role_id**: `FK` -> Role.id - Foreign key referencing the user's role.

### 2. Role
- **id**: `PK` - Unique identifier for each role.
- **name**: String - Name of the role (e.g., Admin, User).

### 3. Diary
- **id**: `PK` - Unique identifier for each diary.
- **title**: String - Title of the diary.
- **description**: Text - Description of the diary.
- **user_id**: `FK` -> User.id - Foreign key referencing the owner of the diary.

### 4. Page
- **id**: `PK` - Unique identifier for each page.
- **title**: String - Title of the page.
- **diary_id**: `FK` -> Diary.id - Foreign key referencing the diary to which the page belongs.

### 5. Entry
- **id**: `PK` - Unique identifier for each entry.
- **content**: Text - Content of the entry.
- **page_id**: `FK` -> Page.id - Foreign key referencing the page to which the entry belongs.

### 6. Category
- **id**: `PK` - Unique identifier for each category.
- **name**: String - Name of the category.

### 7. Tag
- **id**: `PK` - Unique identifier for each tag.
- **name**: String - Name of the tag.

### 8. Entry_Category (Join Table)
- **entry_id**: `FK` -> Entry.id - Foreign key referencing an entry.
- **category_id**: `FK` -> Category.id - Foreign key referencing a category.

### 9. Entry_Tag (Join Table)
- **entry_id**: `FK` -> Entry.id - Foreign key referencing an entry.
- **tag_id**: `FK` -> Tag.id - Foreign key referencing a tag.

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

### Glossary
- **Diary**: A collection of pages for storing entries.
- **Page**: A section within a diary used to organize entries.
- **Entry**: A single note or piece of content within a page.
                                                                           
                                                                            
                                                                           
                                                                            

