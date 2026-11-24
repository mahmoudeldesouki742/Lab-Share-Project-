
<div align="center">

# 🧪 LabShare

### Laboratory Equipment Management & Reservation System

A Python desktop application for managing laboratory equipment, reservations, and maintenance operations.

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/GUI-Tkinter%20%2F%20ttk-orange" alt="Tkinter / ttk" />
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Version%20Control-Git%20%26%20GitHub-181717?logo=github&logoColor=white" alt="Git and GitHub" />
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow" alt="In development" />
</p>

</div>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Project Objectives](#-project-objectives)
- [Features and Modules](#-features-and-modules)
- [User Roles and Permissions](#-user-roles-and-permissions)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [Database Design](#-database-design)
- [Business Rules](#-business-rules)
- [Object-Oriented Design](#-object-oriented-design)
- [Project Structure](#-project-structure)
- [Function Contracts](#-function-contracts)
- [Team Collaboration](#-team-collaboration)
- [Team Responsibilities](#-team-responsibilities)
- [Getting Started](#-getting-started)
- [Testing](#-testing)
- [Development Timeline](#-development-timeline)
- [Academic Evaluation Checklist](#-academic-evaluation-checklist)
- [Project Outcomes](#-project-outcomes)
- [Documentation](#-documentation)
- [Contributors](#-contributors)
- [License](#-license)

---

## 📖 Overview

**LabShare** is a Python-based desktop application designed to organize laboratory equipment, reservation requests, and maintenance operations in one centralized system.

The application is intended to support two main types of users:

- **Administrators**, who manage equipment, review reservation requests, oversee maintenance, and generate utilization reports.
- **Researchers**, who browse equipment, submit reservation requests, and manage their own bookings.

LabShare aims to replace fragmented or manual laboratory management processes with a structured workflow that helps reduce scheduling conflicts, improve equipment availability tracking, and maintain reliable operational records.

> **Project status:** LabShare is currently in development. The modules and workflows described in this README represent the project's planned design and requirements; individual features should be considered complete only when implemented and tested.

## 🎯 Project Objectives

- Centralize laboratory equipment information and management.
- Organize equipment reservation workflows.
- Prevent overlapping reservations.
- Track equipment availability and maintenance status.
- Apply role-based access control.
- Maintain reservation history and operational records.
- Generate equipment utilization reports.
- Apply software engineering principles through a modular architecture.

## ✨ Features and Modules

### 1. 🔐 Authentication and Authorization

- Log in using a username and password.
- Validate user credentials and input.
- Identify user roles and permissions.
- Provide separate access levels for administrators and researchers.

### 2. 🧰 Equipment Management

- Add new equipment records.
- Update equipment information.
- Search for and display equipment.
- Manage equipment categories.
- Track equipment condition and availability.
- Retire equipment instead of permanently deleting records that may have related data.

**Equipment statuses**

| Status | Description |
|---|---|
| `Available` | The equipment is available for reservation. |
| `Under Maintenance` | The equipment is currently being maintained. |
| `Retired` | The equipment is permanently out of service. |

### 3. 📅 Reservation Management

- Create reservation requests.
- Approve or reject reservation requests.
- View reservation details.
- Cancel eligible reservations.
- Track reservation status.
- Prevent overlapping reservations for the same equipment.

**Reservation statuses**

| Status | Description |
|---|---|
| `Pending` | Waiting for approval. |
| `Approved` | The reservation has been approved. |
| `Rejected` | The reservation has been rejected. |
| `Cancelled` | The reservation has been cancelled. |
| `Completed` | The reservation has been completed. |

### 4. 🔧 Maintenance Management

- Report equipment faults.
- Create maintenance records.
- Update maintenance status.
- Track maintenance progress.
- Mark maintenance operations as completed.
- Update equipment availability according to its condition.

### 5. 📊 Reports and Analytics

The planned **Equipment Utilization Report** includes:

- Equipment name.
- Total number of reservations.
- Total completed reservation hours.
- Reservation statistics.

Reports can be exported to CSV format.

### 6. 📝 Reservation History

The system maintains a record of reservation status changes, including:

- Previous reservation status.
- New reservation status.
- User responsible for the change.
- Date and time of the change.
- Additional notes.

---

## 👥 User Roles and Permissions

LabShare defines two primary user roles.

### 🛡️ Administrator

Administrators are responsible for managing the system and its operational processes.

| Area | Permissions |
|---|---|
| Authentication | Log in to the system. |
| Dashboard | View the administrative dashboard. |
| Equipment | Add, update, search, and display equipment. |
| Categories | Manage equipment categories. |
| Reservations | View all reservation requests. |
| Approval | Approve or reject reservation requests. |
| Cancellation | Cancel reservations according to system rules. |
| Maintenance | Manage maintenance operations. |
| Reports | View and export equipment utilization reports. |

### 🔬 Researcher

Researchers can browse equipment and manage their own reservation requests.

| Area | Permissions |
|---|---|
| Authentication | Log in to the system. |
| Equipment | Browse available equipment. |
| Search | Search by equipment name or category. |
| Details | View equipment information and condition. |
| Reservations | Create reservation requests. |
| My Reservations | View personal reservations. |
| Cancellation | Cancel eligible personal reservations. |

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language. |
| Tkinter / ttk | Desktop graphical user interface. |
| SQLite | Relational database. |
| `sqlite3` | Python database connectivity. |
| `csv` | CSV report export. |
| Git | Version control. |
| GitHub | Collaboration and source code management. |

---

## 🏗️ System Architecture

LabShare is designed around a **three-tier architecture**. Each layer has a distinct responsibility to keep the codebase modular, maintainable, and easier to test.

### 1. 🖥️ Presentation Layer

Responsible for displaying information and receiving user input.

**Main components**

- `login_view.py`
- `dashboard_view.py`
- `equipment_view.py`
- `reservation_view.py`
- `maintenance_view.py`
- `reports_view.py`

**Responsibilities**

- Display application screens.
- Receive and present user input.
- Display success and error messages.
- Call the appropriate business logic functions.
- Keep SQL queries out of the user interface.

### 2. ⚙️ Business Logic Layer

Responsible for processing data and enforcing application rules.

**Main components**

- Models
- Services
- Validators
- Custom exceptions

**Core services**

- `AuthService`
- `EquipmentService`
- `ReservationService`
- `MaintenanceService`
- `ReportService`

**Responsibilities**

- Validate user input.
- Enforce business rules.
- Verify user permissions.
- Coordinate operations involving multiple database tables.
- Handle application-level errors.

### 3. 🗄️ Data Access Layer

Responsible for database connectivity and SQL operations.

**Main components**

- `database.py`
- `schema.sql`
- Repositories

**Core repositories**

- `UserRepository`
- `CategoryRepository`
- `EquipmentRepository`
- `ReservationRepository`
- `MaintenanceRepository`
- `HistoryRepository`

**Responsibilities**

- Execute SQL queries.
- Insert, retrieve, and update records.
- Perform permitted deletion operations.
- Manage database transactions.
- Return structured data to the business logic layer.

### 🔄 Application Data Flow

```text
┌─────────────────────────┐
│    Presentation Layer   │
│       (Tkinter UI)      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Business Logic Layer  │
│ Models / Services /     │
│ Validators / Exceptions │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     Data Access Layer   │
│       Repositories      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      SQLite Database    │
└─────────────────────────┘
```

Results and errors return through the same layers in the opposite direction.

**Architecture rule:** The presentation layer must not contain SQL queries, and the data access layer must not contain GUI-related code.

---

## 🗃️ Database Design

LabShare uses a relational SQLite database planned around six interconnected tables.

| Table | Description |
|---|---|
| `Users` | Stores user information and account roles. |
| `Categories` | Stores equipment categories. |
| `Equipment` | Stores equipment details and status. |
| `Reservations` | Stores reservation requests. |
| `Maintenance` | Stores equipment maintenance records. |
| `Reservation_History` | Stores reservation status changes. |

### 🔗 Database Relationships

- One user can have multiple reservations.
- One user can report multiple maintenance issues.
- One user can make multiple reservation status changes.
- One category can contain multiple equipment items.
- One equipment item can have multiple reservations.
- One equipment item can have multiple maintenance records.
- One reservation can have multiple history records.

### 🔒 Database Constraints

The database design must include:

- **Primary keys (`PK`)** for all tables.
- **Foreign keys (`FK`)** to enforce relationships.
- **`UNIQUE` constraints** for fields that must be unique.
- **`NOT NULL` constraints** for required fields.
- **`CHECK` constraints** to validate values and statuses.
- **Foreign key enforcement** on every SQLite database connection.

Equipment with related records should not be permanently deleted. Instead, its status should be changed to `Retired`.

### 📐 Entity Relationship Overview

```text
Users ─────────────< Reservations >──────────── Equipment
  │                       │                         │
  │                       ▼                         │
  │              Reservation_History               │
  │                                                 │
  └─────────────< Maintenance >─────────────────────┘

Categories ─────────────< Equipment
```

The detailed ERD and other project diagrams will be maintained in the `diagrams/` directory.

---

## 📏 Business Rules

All business rules must be implemented in the **business logic layer**, rather than directly in the GUI.

### 1. Reservation Conflict Prevention

A reservation cannot be created if another reservation for the same equipment overlaps with the requested time interval and has a status of `Pending` or `Approved`.

The overlap condition is:

```python
new_start < existing_end and new_end > existing_start
```

### 2. Equipment Availability

Equipment cannot be reserved if its status is:

- `Under Maintenance`
- `Retired`

### 3. Reservation Time Validation

- The reservation start time must be in the future.
- The reservation end time must be later than the start time.
- The maximum reservation duration is seven days.

### 4. Reservation Ownership

Researchers cannot view or cancel reservations belonging to other researchers.

### 5. Reservation Status Transitions

Only the following status transitions are allowed:

| Current Status | Allowed Next Status |
|---|---|
| `Pending` | `Approved` |
| `Pending` | `Rejected` |
| `Pending` | `Cancelled` |
| `Approved` | `Completed` |
| `Approved` | `Cancelled` |

`Rejected`, `Cancelled`, and `Completed` are final reservation states.

Every reservation status change must be recorded in the `Reservation_History` table.

---

## 🧩 Object-Oriented Design

The project applies Object-Oriented Programming (OOP) to organize data and functionality into reusable classes.

### Model Classes

- `User`
- `Category`
- `Equipment`
- `Reservation`
- `Maintenance`
- `ReservationHistory`

### Service Classes

- `AuthService`
- `EquipmentService`
- `ReservationService`
- `MaintenanceService`
- `ReportService`

### Custom Exceptions

- `LabShareError`
- `ValidationError`
- `AuthenticationError`
- `NotFoundError`
- `PermissionError`
- `ConflictError`
- `DataAccessError`

At least three classes must be implemented with appropriate data validation and custom exception handling.

---

## 📂 Project Structure

The following is the planned project directory structure:

```text
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
```

---

## 🔌 Function Contracts

To reduce integration conflicts, all team members must follow the agreed function names, parameters, and return structures.

### `EquipmentService`

```python
create_equipment(data)
get_equipment(equipment_id)
get_all_equipment()
update_equipment(equipment_id, data)
retire_equipment(equipment_id)
search_equipment(keyword)
```

### `ReservationService`

```python
create_reservation(
    user_id,
    equipment_id,
    start_time,
    end_time,
    purpose
)

approve_reservation(reservation_id, admin_id)

reject_reservation(
    reservation_id,
    admin_id,
    reason
)

cancel_reservation(reservation_id, user_id)

complete_reservation(reservation_id, admin_id)

get_user_reservations(user_id)
get_all_reservations()
```

### `MaintenanceService`

```python
create_maintenance(data)
complete_maintenance(maintenance_id)
get_all_maintenance()
```

### `ReportService`

```python
generate_usage_report(
    start_date,
    end_date,
    equipment_id=None
)

export_csv(report_data, file_path)
```

### `AuthService`

```python
login(username, password)
register(user_data)
```

> **Separation of responsibilities:** Repositories return structured data and handle database operations. Services validate input, enforce business rules, coordinate operations, and raise appropriate exceptions.

---

## 🤝 Team Collaboration

LabShare is developed collaboratively using Git and GitHub to organize contributions and reduce code conflicts.

### 🌿 Branching Strategy

| Branch | Purpose |
|---|---|
| `main` | Stable project version. |
| `develop` | Integration branch for completed features. |
| `feature/*` | Individual feature branches. |

### 🔄 Development Workflow

1. Each team member creates a branch for the assigned task.
2. The required functionality is implemented.
3. The code is tested locally.
4. A Pull Request is opened targeting `develop`.
5. Another team member reviews the changes.
6. Approved changes are merged into `develop`.
7. The integrated system is tested before changes are merged into `main`.

Database design and shared function contracts must not be changed without coordinating with the rest of the team.

### 👨‍💻 Shared Team Expectations

All team members are expected to:

- Understand the overall project architecture.
- Participate in integrating different components.
- Review and test each other's code.
- Follow the agreed file and function naming conventions.
- Contribute to project documentation.
- Participate in preparing the final presentation.

Task division does not mean that members work independently without integration. Development and integration should happen continuously.

---

## 👨‍👩‍👧‍👦 Team Responsibilities

The project is divided into five main areas of responsibility.

### Member 1 — Authentication and Dashboard

**Responsibilities**

- Design the login interface.
- Implement authentication logic.
- Create the `User` model.
- Design the dashboard.
- Implement role-based navigation.

**Assigned files**

```text
ui/login_view.py
ui/dashboard_view.py
logic/models/user.py
logic/services/auth_service.py
```

### Member 2 — Equipment Management

**Responsibilities**

- Design the equipment management interface.
- Implement equipment CRUD operations.
- Manage equipment categories.
- Validate equipment data.
- Implement equipment and category models and services.

**Assigned files**

```text
ui/equipment_view.py
logic/models/equipment.py
logic/models/category.py
logic/services/equipment_service.py
```

### Member 3 — Reservations, Maintenance, and Reports

**Responsibilities**

- Design reservation, maintenance, and reports interfaces.
- Implement reservation and maintenance logic.
- Implement CSV report export.

**Assigned files**

```text
ui/reservation_view.py
ui/maintenance_view.py
ui/reports_view.py

logic/models/reservation.py
logic/models/maintenance.py

logic/services/reservation_service.py
logic/services/maintenance_service.py
logic/services/report_service.py

reports/csv_exporter.py
```

### Member 4 — Database Design

**Responsibilities**

- Design the database.
- Create the ERD.
- Configure database connectivity.
- Write the SQL schema.
- Implement table constraints and relationships.
- Implement user, category, and equipment repositories.

**Assigned files**

```text
data/database.py
data/schema.sql

data/repositories/user_repository.py
data/repositories/category_repository.py
data/repositories/equipment_repository.py
```

### Member 5 — Data Access and Integration

**Responsibilities**

- Implement reservation, maintenance, and history repositories.
- Implement validators.
- Implement custom exceptions.
- Help integrate the different system layers.

**Assigned files**

```text
data/repositories/reservation_repository.py
data/repositories/maintenance_repository.py
data/repositories/history_repository.py

logic/validators.py
logic/exceptions.py
logic/models/history.py
```

---

## 🚀 Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Make sure the following tools are installed:

- [Python 3.10 or later](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads/)

### 1. Clone the Repository

Replace `YOUR-USERNAME` with the repository owner's GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/LabShare.git
```

### 2. Navigate to the Project Directory

```bash
cd LabShare
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows (PowerShell / Command Prompt)**

```powershell
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python main.py
```

> **Note:** Database initialization must be completed before running the application.

---

## 🧪 Testing

The project includes tests for essential application operations.

Testing should cover:

- Authentication and authorization.
- Equipment management.
- Reservation creation and validation.
- Reservation conflict detection.
- Invalid user input.
- Database operations.
- CSV report export.

Run the test suite from the project root:

```bash
python -m unittest discover -s tests
```

---

## 🗓️ Development Timeline

The project is planned to be completed within **18 days**.

| Phase | Timeline | Main Tasks |
|---|---:|---|
| Planning and Setup | Days 1–2 | Architecture, ERD, repository setup, and function contracts. |
| Database and Core Components | Days 3–5 | SQLite schema, database connection, models, and repositories. |
| Business Logic | Days 6–10 | Services, business rules, validators, exceptions, and backend tests. |
| GUI Development | Days 6–12 | Login, dashboard, equipment, reservations, maintenance, and reports. |
| Integration | Days 13–14 | Connect the GUI, services, and repositories. |
| Testing | Days 15–16 | Validation, conflict detection, permissions, and CSV export. |
| Final Delivery | Days 17–18 | README, diagrams, presentation, and final fixes. |

---

## ✅ Academic Evaluation Checklist

The project is expected to satisfy the following academic requirements:

- [ ] Implement a three-tier architecture using separate files.
- [ ] Create at least three related database tables with primary keys, foreign keys, and constraints.
- [ ] Implement at least three classes.
- [ ] Implement custom exceptions for input validation.
- [ ] Implement CRUD operations or logical deletion.
- [ ] Implement search functionality.
- [ ] Implement at least two business rules in the business logic layer.
- [ ] Use `try` / `except` for error handling.
- [ ] Display success and error messages to the user.
- [ ] Generate and export at least one report to CSV.
- [ ] Implement at least three console-based tests, including invalid-input tests.
- [ ] Prepare project documentation.
- [ ] Create four project diagrams.
- [ ] Prepare a two-minute demonstration.

---

## 🎓 Project Outcomes

LabShare is intended to demonstrate the team's ability to:

1. Design a structured software architecture.
2. Build a relational database.
3. Apply Object-Oriented Programming.
4. Separate application responsibilities.
5. Implement business rules and validation.
6. Integrate graphical interfaces with a database.
7. Test application workflows and handle errors.
8. Collaborate effectively using Git and GitHub.

The primary focus is to satisfy the academic requirements while maintaining organized code, reliable functionality, and smooth integration between team members.

---

## 📄 Documentation

Additional project documentation and diagrams are maintained in the `diagrams/` directory.

The documentation may include:

- System Architecture Diagram.
- Entity Relationship Diagram (ERD).
- Use Case Diagram.
- Activity Diagram.

---

## 👥 Contributors

Developed by a team of **five students**.

- **University:** Benha University
- **Faculty:** Faculty of Computers and Artificial Intelligence
- **Project Type:** Academic Software Engineering Project

---

## 📜 License

This project is currently developed for academic purposes.

No open-source license has been specified yet. If the project is later distributed or intended for reuse, an appropriate license should be added.

---

<div align="center">

**LabShare**

*Organizing laboratory resources through structured management.*

</div>
