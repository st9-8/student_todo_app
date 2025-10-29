modifie par Marlon
# 📝 Django TODO App - Backend Exercise

A practical web development exercise focused on building a complete Django backend for a TODO application. The frontend templates are provided, allowing students to concentrate on models, views, forms, and Django architecture.

## 🎯 Learning Objectives

By completing this exercise, students will practice:

- Creating Django models with various field types
- Implementing CRUD operations (Create, Read, Update, Delete)
- Working with Django views (Function-Based or Class-Based)
- Handling forms and form validation
- Setting up URL routing
- Working with Django ORM for database operations
- Understanding the Django MVT (Model-View-Template) architecture

## 📋 Project Requirements

### Features to Implement

Your TODO app must support the following operations:

1. **Create a Task**
   - Title (required)
   - Description (optional)
   - Due Date (optional)
   - Due Time (optional)

2. **Display All Tasks**
   - List view with all tasks
   - Show completion status
   - Display task metadata

3. **Display Single Task**
   - Detailed view of individual task
   - Show all task information

4. **Update a Task**
   - Edit existing task details
   - Update completion status

5. **Delete a Task**
   - Remove task from database

6. **Mark Task as Complete/Incomplete**
   - Toggle completion status
   - Visual indication of completed tasks

## 🗂️ Project Structure

```
todo_project/
│
├── todo_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── task_list.html
│   │   ├── task_detail.html
│   │   └── task_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # ← YOU IMPLEMENT THIS
│   ├── views.py           # ← YOU IMPLEMENT THIS
│   ├── forms.py           # ← YOU IMPLEMENT THIS
│   ├── urls.py            # ← YOU IMPLEMENT THIS
│   └── tests.py           # ← BONUS: Write tests
│
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- uv (Python package installer)
- Git
- GitHub account

### Getting the Project

1. **Fork this repository**
   - Click the "Fork" button at the top right of this repository
   - This creates a copy of the project in your GitHub account

2. **Clone your forked repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/student_todo_app.git
   cd student_todo_app
   ```
   Replace `YOUR_USERNAME` with your GitHub username and `student_todo_app` with the actual repository name.

### Installation

1. **Install uv** (if not already installed)
   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Create a virtual environment with uv**
   ```bash
   uv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Django**
   ```bash
   uv add django
   ```

5. **Install Django**
   ```bash
   uv pip install django
   ```

6. **Create Django project** (if not already created)
   ```bash
   django-admin startproject todo_project .
   ```

6. **Create Django app**
   ```bash
   python manage.py startapp todo_app
   ```

7. **Add templates to the app**
   - Create a `templates` folder inside `todo_app`
   - Add the provided HTML files (base.html, task_list.html, task_detail.html, task_form.html)

## 📄 Template Files Overview

The project includes four pre-built HTML templates that provide a complete, responsive frontend for your TODO app. Your job is to build the backend that powers these templates.

- **base.html** - Base Template
The foundation template that all other templates extend from. It includes:

   - Header with app branding and navigation
   - Navigation bar with links to all tasks and create new task
   - Message display area for Django messages (success, error, info)
   - Footer
   - Common CSS styling with gradient backgrounds and modern UI elements
   - Reusable button styles and utilities

- **task_list.html** - Display All Tasks
The main dashboard showing all tasks. Features include:

   - Task statistics dashboard (Total, Pending, Completed)
   - Filter buttons to show All, Pending, or Completed tasks
   - Task cards with checkbox for quick completion toggle
   - Displays task title, description, due date/time, and status badge
   - Action buttons (View, Edit, Delete) for each task
   - Empty state message when no tasks exist
   - JavaScript functionality for filtering and AJAX toggle

- **task_detail.html** - Display Single Task
A detailed view of a single task. Shows:

   - Complete task information in a card layout
   - Status indicator (Completed/Pending) with visual badge
   - Task description with proper formatting
   - Due date and time in separate metadata cards
   - Action buttons to mark complete/incomplete, edit, or delete
   - Back button to return to task list

- **task_form.html** - Create/Update Task Form
A form for creating new tasks or editing existing ones. Includes:

   - Clean, user-friendly form layout with proper labels
   - All task fields (title, description, due date, due time)
   - Required field indicators and optional field labels
   - Client-side validation with visual feedback
   - Character counter for title field
   - Auto-resizing textarea for description
   - Date picker with minimum date set to today
   - Checkbox for completion status (only shown when editing)
   - Form help text and error message display
   - Cancel button to return without saving

All templates are fully styled with CSS and include JavaScript for enhanced user experience. They use Django template syntax and expect specific URL names and context variables that you'll need to implement in your backend.

## Resources

- https://docs.djangoproject.com/en/4.2/ref/templates/language/
- https://docs.djangoproject.com/en/4.2/topics/templates/
- https://docs.djangoproject.com/en/4.2/topics/forms/

## 🎉 Good Luck!

Remember: The goal is to learn Django architecture and best practices. Don't hesitate to experiment and try different approaches. Happy coding! 🚀
