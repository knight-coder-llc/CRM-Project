# Django CRM System

A robust Customer Relationship Management (CRM) system built with Django 6.0, designed to help businesses manage their relationships with customers, leads, and sales opportunities efficiently.

## Features

*   **Dashboard**: Overview of your CRM activities.
*   **Account Management**: store and manage company details, including industry, contact info, and addresses.
*   **Contact Management**: Maintain individual contacts associated with specific accounts.
*   **Lead Tracking**: Track potential customers through various stages (New -> Contacted -> Qualified -> Lost) and sources.
*   **Opportunity Pipeline**: Manage sales deals with value tracking and stage progression (Prospecting, Negotiation, Closed Won/Lost).
*   **Django Admin**: Full administrative control over all data models.

## Tech Stack

*   **Backend**: Python, Django 6.0
*   **Database**: SQLite (Default, easy to switch to PostgreSQL/MySQL)
*   **Frontend**: Django Templates (HTML/CSS)

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

*   Python 3.10+
*   Git

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/knight-coder-llc/CRM-Project.git
    cd CRM-Project
    ```

2.  **Create and activate a virtual environment**
    *   **Windows**:
        ```powershell
        python -m venv venv
        .\venv\Scripts\Activate
        ```
    *   **Mac/Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for Admin access)**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server**
    ```bash
    python manage.py runserver
    ```

7.  **Access the application**
    *   Main Site: `http://127.0.0.1:8000/`
    *   Admin Panel: `http://127.0.0.1:8000/admin/`

## Project Structure

*   `crm/`: Main application containing models, views, and templates.
*   `django_crm/`: Project configuration and settings.
*   `db.sqlite3`: Local development database.
*   `manage.py`: Django's command-line utility.

## License

This project is open source and available under the [MIT License](LICENSE).
