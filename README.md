LabShare

Laboratory Equipment Management & Reservation System

<p align="center">
  A Desktop Application for Managing Laboratory Equipment, Reservations, and Maintenance
</p>---

📌 Overview

LabShare is a Python-based desktop application designed to simplify the management of laboratory equipment, organize reservation processes, and monitor equipment maintenance.

The system provides a centralized platform where laboratory administrators can manage equipment, approve or reject reservation requests, track maintenance operations, and generate equipment utilization reports.

Researchers can browse available equipment, submit reservation requests, and monitor their reservation status.

LabShare aims to replace manual equipment management processes with a structured, reliable, and user-friendly system that reduces scheduling conflicts and improves resource utilization.

---

🎯 Project Objectives

- Centralize laboratory equipment management.
- Organize and streamline equipment reservation workflows.
- Prevent overlapping reservations.
- Track equipment availability and maintenance status.
- Implement role-based access control.
- Maintain reservation history and operational records.
- Generate equipment utilization reports.
- Apply software engineering principles through a modular and maintainable architecture.

---

✨ Core Features

🔐 Authentication & Authorization

- Secure user login using username and password.
- User authentication and input validation.
- Role-based access control.
- Separate permissions for administrators and researchers.

🧪 Equipment Management

- Add, update, search, and display equipment.
- Manage equipment categories.
- Track equipment condition and availability.
- Retire equipment without permanently deleting important records.

📅 Reservation Management

- Create equipment reservation requests.
- Approve or reject reservation requests.
- Track reservation status.
- Cancel reservations according to system rules.
- Prevent conflicting reservations.

🔧 Maintenance Management

- Report equipment faults.
- Create maintenance records.
- Track maintenance progress.
- Update equipment availability after maintenance completion.

📊 Reporting

- Generate Equipment Utilization Reports.
- Calculate reservation statistics.
- Track completed reservation hours.
- Export reports to CSV format.

📝 Reservation History

- Record reservation status changes.
- Track the user responsible for each change.
- Maintain historical records for system operations.

---

👥 User Roles

Administrator

Responsible for managing the system and its operational processes.

Permissions include:

- Managing equipment and categories.
- Viewing all reservation requests.
- Approving or rejecting reservations.
- Managing maintenance operations.
- Generating and exporting reports.

Researcher

Responsible for browsing equipment and making reservations.

Permissions include:

- Viewing available equipment.
- Searching by equipment name or category.
- Viewing equipment details and condition.
- Creating reservation requests.
- Viewing personal reservations.
- Cancelling eligible reservations.

---

🛠️ Technology Stack

Technology| Purpose
Python| Core programming language
Tkinter / ttk| Desktop graphical user interface
SQLite| Relational database
sqlite3| Database connectivity
CSV Module| Report export
Git| Version control
GitHub| Team collaboration and project management

---

🏗️ System Architecture

LabShare follows a Three-Tier Architecture to separate responsibilities and improve maintainability.

1. Presentation Layer

Responsible for displaying the graphical interface and receiving user input.

Main components:

- Login View
- Dashboard View
- Equipment View
- Reservation View
- Maintenance View
- Reports View

The presentation layer communicates with the business logic layer and does not execute SQL queries directly.

2. Business Logic Layer

Responsible for implementing system rules, validating inputs, and coordinating application operations.

Main components:

- Models
- Services
- Validators
- Custom Exceptions

Core services:

- "AuthService"
- "EquipmentService"
- "ReservationService"
- "MaintenanceService"
- "ReportService"

3. Data Access Layer

Responsible for database connectivity and data persistence.

Main components:

- Database configuration
- SQL schema
- Repositories

Repositories:

- "UserRepository"
- "CategoryRepository"
- "EquipmentRepository"
- "ReservationRepository"
- "MaintenanceRepository"
- "HistoryRepository"

Data Flow

Presentation Layer
        ↓
Business Logic Layer
        ↓
Data Access Layer
        ↓
SQLite Database

The results and errors are returned through the same layers in the opposite direction.

---

🗄️ Database Design

LabShare uses a relational SQLite database consisting of six interconnected tables.

Table| Description
"Users"| Stores user information and account roles
"Categories"| Stores equipment categories
"Equipment"| Stores equipment details and status
"Reservations"| Stores reservation requests and their statuses
"Maintenance"| Stores equipment maintenance records
"Reservation_History"| Tracks reservation status changes

Database Constraints

The database uses:

- Primary Keys ("PK")
- Foreign Keys ("FK")
- Unique Constraints ("UNIQUE")
- Required Fields ("NOT NULL")
- Validation Constraints ("CHECK")
- Foreign Key Enforcement

Equipment with existing records is retired instead of being permanently deleted.

---

⚙️ Business Rules

The system enforces the following rules:

- A reservation cannot overlap with another active reservation for the same equipment.
- Equipment under maintenance or retired equipment cannot be reserved.
- Reservation start time must be in the future.
- Reservation end time must be later than the start time.
- The maximum reservation duration is seven days.
- Researchers can only view or cancel their own reservations.
- Reservation status transitions must follow the approved workflow.
- Reservation status changes must be recorded in the history table.

Reservation Statuses

Pending
Approved
Rejected
Cancelled
Completed

Equipment Statuses

Available
Under Maintenance
Retired

---

📂 Project Structure

LabShare/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── ui/
│   ├── app.py
│   ├── login_view.py
│   ├── dashboard_view.py
│   ├── equipment_view.py
│   ├── reservation_view.py
│   ├── maintenance_view.py
│   └── reports_view.py
│
├── logic/
│   ├── exceptions.py
│   ├── validators.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── equipment.py
│   │   ├── category.py
│   │   ├── reservation.py
│   │   ├── maintenance.py
│   │   └── history.py
│   │
│   └── services/
│       ├── auth_service.py
│       ├── equipment_service.py
│       ├── reservation_service.py
│       ├── maintenance_service.py
│       └── report_service.py
│
├── data/
│   ├── database.py
│   ├── schema.sql
│   │
│   └── repositories/
│       ├── user_repository.py
│       ├── category_repository.py
│       ├── equipment_repository.py
│       ├── reservation_repository.py
│       ├── maintenance_repository.py
│       └── history_repository.py
│
├── reports/
│   └── csv_exporter.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_equipment.py
│   └── test_reservations.py
│
└── diagrams/

---

🚀 Getting Started

Prerequisites

Make sure you have the following installed:

- Python 3.10 or later
- Git

Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/LabShare.git

Navigate to the project directory:

cd LabShare

Create a virtual environment:

python -m venv .venv

Activate the virtual environment.

Windows:

.venv\Scripts\activate

Linux / macOS:

source .venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

Run the application:

python main.py

«Note: The application requires its database schema to be initialized before use.»

---

🧪 Testing

LabShare includes tests for essential system operations.

The testing process focuses on:

- Authentication and authorization.
- Equipment management.
- Reservation validation.
- Reservation conflict detection.
- Invalid user inputs.
- Database operations.
- CSV report generation.

Run the tests using:

python -m unittest discover -s tests

---

🤝 Team Collaboration

The project is developed collaboratively using Git and GitHub.

Branching Strategy

Branch| Purpose
"main"| Stable and final version
"develop"| Integration branch
"feature/*"| Individual feature development

Development Workflow

1. Create a feature branch for the assigned task.
2. Implement the required functionality.
3. Test the changes locally.
4. Push the branch to GitHub.
5. Open a Pull Request targeting "develop".
6. Review the code before merging.
7. Test the integrated system.
8. Merge the stable version into "main".

Changes to shared database structures or function contracts must be coordinated with the team.

---

📋 Academic Requirements

The project demonstrates the practical application of:

- Three-Tier Architecture.
- Object-Oriented Programming (OOP).
- Relational Database Design.
- SQL Constraints and Relationships.
- CRUD Operations.
- Business Logic Implementation.
- Input Validation.
- Custom Exception Handling.
- Error Handling using "try/except".
- Automated or console-based testing.
- Data Export and Reporting.
- Git and GitHub Collaboration.

---

🗺️ Development Roadmap

The project is planned to be completed within 18 days, following these phases:

- Days 1–2: Planning, architecture, database design, and repository setup.
- Days 3–5: Database schema, models, and repositories.
- Days 6–10: Business logic, services, validation, and backend testing.
- Days 6–12: GUI development in parallel.
- Days 13–14: Integration and workflow testing.
- Days 15–16: System testing and bug fixing.
- Days 17–18: Documentation, diagrams, and final presentation.

---

🎓 Project Purpose

LabShare is an academic software engineering project developed to demonstrate the team's ability to design and implement a structured desktop application.

The project focuses on applying programming fundamentals, database concepts, OOP principles, software architecture, and collaborative development practices in a practical system.

The primary goal is to deliver a reliable and maintainable application that satisfies the academic requirements while preserving clean code organization and effective team integration.

---

👨‍💻 Contributors

Developed collaboratively by a team of five students.

- Team members: [Add team members]
- Institution: [Add university name]
- Department: [Add department name]

---

📄 License

This project was developed for academic purposes.

A license may be added if the project is intended for public distribution or reuse.

---

<p align="center">
  <b>LabShare — Simplifying Laboratory Resource Management</b>
</p>#LabShare #Python #SQLite #Tkinter #OOP #SoftwareEngineering #GitHub #DesktopApplication #DatabaseDesign #TeamProject
