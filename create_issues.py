#!/usr/bin/env python3
"""
LabShare - create all GitHub issues at once.

Requirements:
  1) Install GitHub CLI: https://cli.github.com
  2) Log in:             gh auth login
  3) Run from inside the repo folder (or pass --repo):

       python create_issues.py --dry-run          # preview, creates nothing
       python create_issues.py                    # create for real
       python create_issues.py --repo USER/LabShare

Run it only ONCE, otherwise the issues will be duplicated.
"""
import argparse
import subprocess
import sys

OWNERS = {
    "D": ("Eldesouky", "owner: Eldesouky", "0e8a16"),
    "M": ("Marwan", "owner: Marwan", "fbca04"),
    "S": ("Elsaadany", "owner: Elsaadany", "d93f0b"),
    "V": ("Elsayed Mahmoud", "owner: Elsayed", "8250df"),
    "N": ("Nader", "owner: Nader", "f9843a"),
    "ALL": ("Whole team", "owner: team", "1d76db"),
}

PHASES = {
    0: ("phase 0: setup", "c5def5"),
    1: ("phase 1: database and models", "bfdadc"),
    2: ("phase 2: business logic", "d4c5f9"),
    3: ("phase 3: ui", "fef2c0"),
    4: ("phase 4: integration", "f9d0c4"),
    5: ("phase 5: testing", "e99695"),
    6: ("phase 6: delivery", "0052cc"),
}

# (id, phase, title, files, depends_on, description, [checklist])
TASKS = [
    # ======================= PHASE 0: SETUP =======================
    ("N-1", 0, "Implement custom exceptions",
     ["logic/exceptions.py"], [],
     "Create the shared exception hierarchy used by every layer of LabShare. "
     "All other members depend on this file, so it must be delivered first (days 1-2). "
     "Every exception must inherit from LabShareError and accept a clear, human-readable message "
     "so the UI can display it directly to the user.",
     ["LabShareError as the base class",
      "ValidationError, AuthenticationError, NotFoundError",
      "PermissionError, ConflictError, DataAccessError",
      "Each exception accepts a message and has a docstring explaining when to raise it",
      "Share the file with the team in the first two days"]),

    ("D-1", 0, "Create project configuration and requirements",
     ["config.py", "requirements.txt"], [],
     "Create the central configuration module and the dependency list. config.py should hold the "
     "database file path, application name and business constants (for example the maximum "
     "reservation duration of 7 days) so no magic numbers are scattered across the code. "
     "requirements.txt should list external packages, or contain a comment stating that only the "
     "standard library is used.",
     ["DB_PATH, APP_NAME and window settings in config.py",
      "MAX_RESERVATION_DAYS = 7 and allowed status lists as constants",
      "requirements.txt created (or documented as standard-library only)",
      "Confirm python main.py can import config without errors"]),

    ("D-2", 0, "Design the ERD and database schema with the team",
     ["diagrams/ (draft ERD)"], [],
     "Design the six tables (Users, Categories, Equipment, Reservations, Maintenance, "
     "Reservation_History) including columns, data types, primary keys, foreign keys and "
     "constraints. Agree on the exact spelling of every status value (Available, Under Maintenance, "
     "Retired, Pending, Approved, Rejected, Cancelled, Completed) with Marwan and Nader before any "
     "code is written, because their code depends on these values.",
     ["Columns and types defined for all six tables",
      "PK, FK, UNIQUE, NOT NULL and CHECK constraints listed",
      "Status values agreed with Marwan and Nader",
      "Draft ERD committed to diagrams/",
      "Design approved by the team"]),

    # ======================= PHASE 1: DATABASE AND MODELS =======================
    ("D-3", 1, "Write schema.sql and database.py (deliver by day 3)",
     ["data/schema.sql", "data/database.py"], ["D-2"],
     "Implement the approved schema in SQL and create the database connection module. "
     "database.py must enable foreign key enforcement (PRAGMA foreign_keys = ON) on every "
     "connection and provide helpers to get a connection and initialize the database from schema.sql. "
     "Include seed data (one admin, one researcher, a few categories and equipment) so everyone can "
     "test immediately. The whole team is blocked until this is delivered.",
     ["All six tables created with constraints",
      "PRAGMA foreign_keys = ON on every connection",
      "get_connection() and init_db() functions",
      "Seed data: admin, researcher, categories, equipment",
      "Verified that every teammate can run the init locally"]),

    ("D-4", 1, "Implement UserRepository",
     ["data/repositories/user_repository.py"], ["D-3"],
     "Implement all database access for the Users table. The repository only executes SQL and "
     "returns structured data; validation and business rules belong to the service layer. "
     "All queries must be parameterized.",
     ["add_user(...)",
      "get_by_id(user_id) and get_by_username(username)",
      "get_all_users()",
      "Parameterized queries only",
      "Raise DataAccessError when the database operation fails"]),

    ("D-5", 1, "Implement CategoryRepository",
     ["data/repositories/category_repository.py"], ["D-3"],
     "Implement database access for the Categories table: create, read and update categories. "
     "Category names must be unique, so a duplicate insert should be reported clearly "
     "to the service layer.",
     ["add_category, update_category",
      "get_category(id) and get_all_categories()",
      "Unique name handled (UNIQUE constraint error translated to a clear exception)",
      "Parameterized queries only"]),

    ("D-6", 1, "Implement EquipmentRepository",
     ["data/repositories/equipment_repository.py"], ["D-3"],
     "Implement database access for the Equipment table, including search and status updates. "
     "Equipment that has related reservations or maintenance records must never be deleted; "
     "it is retired by changing its status to Retired. Search should work by equipment name "
     "and by category.",
     ["add_equipment, update_equipment",
      "get_equipment(id) and get_all_equipment()",
      "search_equipment(keyword) by name or category",
      "update_status(equipment_id, status)",
      "No hard delete for equipment with related records"]),

    ("M-1", 1, "Create Reservation and ReservationHistory models",
     ["logic/models/reservation.py", "logic/models/history.py"], ["D-2", "N-1"],
     "Create the model classes for reservations and reservation history. Their attributes must match "
     "the schema exactly. Include status constants and light validation inside the class "
     "(for example rejecting an unknown status) using the custom exceptions.",
     ["Reservation class with all schema fields",
      "ReservationHistory class (old status, new status, changed_by, changed_at, notes)",
      "Status constants shared with the service layer",
      "Basic validation raising ValidationError"]),

    ("M-2", 1, "Implement HistoryRepository",
     ["data/repositories/history_repository.py"], ["D-3", "M-1"],
     "Implement database access for the Reservation_History table. Every reservation status change "
     "must be stored here, so this repository is called by the reservation service whenever a "
     "status changes.",
     ["add_history_record(reservation_id, old_status, new_status, changed_by, notes)",
      "get_history_for_reservation(reservation_id)",
      "Parameterized queries only"]),

    ("M-3", 1, "Implement ReservationRepository with conflict detection",
     ["data/repositories/reservation_repository.py"], ["D-3", "M-1"],
     "Implement database access for the Reservations table. It must include the overlap query used "
     "to prevent double booking: a conflict exists when new_start < existing_end AND "
     "new_end > existing_start for the same equipment, considering only Pending and Approved "
     "reservations. Status updates and history inserts must be executed inside a single "
     "transaction so data stays consistent.",
     ["add_reservation and get_reservation(id)",
      "get_by_user(user_id) and get_all()",
      "find_conflicts(equipment_id, start, end) for Pending/Approved only",
      "update_status() together with the history record in one transaction",
      "Raise DataAccessError on failure"]),

    ("N-3", 1, "Create the Maintenance model",
     ["logic/models/maintenance.py"], ["D-2", "N-1"],
     "Create the Maintenance model class with attributes matching the Maintenance table: the "
     "equipment, the reporting user, issue description, status and dates. Add status constants "
     "and light validation using the custom exceptions.",
     ["Maintenance class with all schema fields",
      "Maintenance status constants",
      "Basic validation raising ValidationError"]),

    ("N-4", 1, "Implement MaintenanceRepository",
     ["data/repositories/maintenance_repository.py"], ["D-3", "N-3"],
     "Implement database access for the Maintenance table: creating records, updating their "
     "status and querying them. It also needs a query that returns open maintenance records for a "
     "piece of equipment, which the maintenance service uses to decide the equipment status.",
     ["add_maintenance(...)",
      "update_status(maintenance_id, status)",
      "get_maintenance(id) and get_all()",
      "get_open_by_equipment(equipment_id)",
      "Parameterized queries only"]),

    ("V-1", 1, "Create Equipment and Category models",
     ["logic/models/equipment.py", "logic/models/category.py"], ["D-2", "N-1"],
     "Create the Equipment and Category model classes. Attributes must match the schema. "
     "Add validation inside the models (name must not be empty, status must be one of Available, "
     "Under Maintenance or Retired) and raise ValidationError for invalid data.",
     ["Equipment class with all schema fields",
      "Category class",
      "Status constants for equipment",
      "Validation raising ValidationError"]),

    ("S-1", 1, "Create the User model",
     ["logic/models/user.py"], ["D-2"],
     "Create the User model class with id, username, password hash, full name and role. "
     "The role must be validated as either Admin or Researcher. The model must never expose or "
     "print the password hash.",
     ["User class with all schema fields",
      "Role validation (Admin / Researcher)",
      "Helper methods such as is_admin()",
      "Password hash is never printed or returned to the UI"]),

    # ======================= PHASE 2: BUSINESS LOGIC =======================
    ("N-2", 2, "Implement validators",
     ["logic/validators.py"], ["N-1"],
     "Implement reusable validation functions shared by all services: required text, string length, "
     "date and time parsing, date ranges, positive numbers, and username/password format. "
     "All of them raise ValidationError with a clear message. Agree on the needed functions with "
     "Eldesouky and Marwan before writing them.",
     ["validate_required(value, field_name)",
      "validate_date_range(start, end)",
      "validate_username and validate_password",
      "All validators raise ValidationError",
      "Function list agreed with Eldesouky and Marwan"]),

    ("D-7", 2, "Implement EquipmentService",
     ["logic/services/equipment_service.py"], ["D-5", "D-6", "N-1", "N-2"],
     "Implement the equipment business logic following the function contracts in the README. "
     "The service validates input, applies the rules (for example a Retired item cannot be edited "
     "back to Available without a reason), manages categories, and raises the proper custom "
     "exceptions. It also exposes category management used by the equipment UI.",
     ["create_equipment(data), get_equipment(id), get_all_equipment()",
      "update_equipment(id, data) and retire_equipment(id)",
      "search_equipment(keyword)",
      "Category create / update / list methods",
      "Validation and exceptions on every method"]),

    ("D-8", 2, "Write equipment tests",
     ["tests/test_equipment.py"], ["D-7"],
     "Write unit tests for the equipment feature, including invalid input tests required by the "
     "academic checklist. Tests must run with python -m unittest discover -s tests and use a "
     "temporary database so real data is not touched.",
     ["Create equipment with valid data",
      "Invalid input (empty name, invalid status)",
      "Retire equipment instead of deleting",
      "Search by keyword"]),

    ("S-2", 2, "Implement AuthService",
     ["logic/services/auth_service.py"], ["S-1", "D-4", "N-1", "N-2"],
     "Implement login and registration following the README contracts. Passwords must be hashed "
     "(for example with hashlib and a salt) and never stored or compared as plain text. "
     "Login returns a User object including its role so the UI can build role-based navigation. "
     "Invalid credentials raise AuthenticationError.",
     ["login(username, password)",
      "register(user_data)",
      "Password hashing and verification",
      "Role and permission helpers",
      "Raise AuthenticationError / ValidationError appropriately"]),

    ("S-3", 2, "Write authentication tests",
     ["tests/test_auth.py"], ["S-2"],
     "Write unit tests for authentication, including invalid input cases.",
     ["Successful login",
      "Wrong password",
      "Unknown username",
      "Empty username or password",
      "Duplicate username on register"]),

    ("M-4", 2, "ReservationService part 1: create and list reservations",
     ["logic/services/reservation_service.py"], ["M-3", "D-6", "N-1", "N-2"],
     "Implement the first half of the reservation service: creating and listing reservations. "
     "create_reservation must validate that the start time is in the future, the end time is after "
     "the start time and the duration does not exceed 7 days. It must reject equipment that is "
     "Under Maintenance or Retired and detect overlapping reservations by raising ConflictError. "
     "New reservations start with the Pending status and must write a history record.",
     ["create_reservation(user_id, equipment_id, start_time, end_time, purpose)",
      "Time validation (future start, end after start, max 7 days)",
      "Equipment availability check",
      "Conflict detection raising ConflictError",
      "get_user_reservations(user_id) and get_all_reservations()"]),

    ("M-5", 2, "ReservationService part 2: approve, reject, cancel, complete",
     ["logic/services/reservation_service.py"], ["M-2", "M-4"],
     "Implement the status transition logic of the reservation service. Only the transitions "
     "allowed in the README are valid (Pending to Approved/Rejected/Cancelled, Approved to "
     "Completed/Cancelled); Rejected, Cancelled and Completed are final. Every change must be "
     "recorded in Reservation_History. Researchers can only cancel their own reservations "
     "(PermissionError otherwise).",
     ["approve_reservation(reservation_id, admin_id)",
      "reject_reservation(reservation_id, admin_id, reason)",
      "cancel_reservation(reservation_id, user_id)",
      "complete_reservation(reservation_id, admin_id)",
      "Transition validation and ownership checks",
      "History record written for every status change"]),

    ("M-6", 2, "Write reservation tests",
     ["tests/test_reservations.py"], ["M-5"],
     "Write unit tests covering the reservation rules, including invalid scenarios.",
     ["Successful reservation",
      "Overlapping reservation raises ConflictError",
      "Start time in the past or duration over 7 days",
      "Reservation for Retired / Under Maintenance equipment",
      "Invalid status transition",
      "Cancelling another user's reservation"]),

    ("N-5", 2, "Implement MaintenanceService",
     ["logic/services/maintenance_service.py"], ["N-4", "D-6", "M-3", "N-2"],
     "Implement the maintenance business logic. Creating a maintenance record must set the equipment "
     "status to Under Maintenance; completing it must return the equipment to Available (unless "
     "another maintenance record is still open). A maintenance request must be rejected if the "
     "equipment has an overlapping Approved reservation.",
     ["create_maintenance(data)",
      "complete_maintenance(maintenance_id)",
      "get_all_maintenance()",
      "Update equipment status on create and complete",
      "Block maintenance that conflicts with Approved reservations"]),

    ("S-5", 2, "Implement CSV exporter",
     ["reports/csv_exporter.py"], [],
     "Implement CSV export for report data using the csv module. It can be developed and tested "
     "with sample data before the report service is ready. File errors (invalid path, file open in "
     "another program) must be handled with try/except and reported clearly.",
     ["export_csv(report_data, file_path)",
      "Clear column headers",
      "try/except around file writing",
      "Tested with sample data"]),

    ("S-6", 2, "Implement ReportService",
     ["logic/services/report_service.py"], ["M-3", "D-6", "S-5"],
     "Implement the Equipment Utilization Report. For each piece of equipment in the selected "
     "period it returns the equipment name, total number of reservations and total completed "
     "reservation hours. It can optionally be filtered by a single equipment id.",
     ["generate_usage_report(start_date, end_date, equipment_id=None)",
      "Total reservations per equipment",
      "Total completed hours per equipment",
      "Date range validation",
      "export_csv wired in through csv_exporter"]),

    # ======================= PHASE 3: UI =======================
    ("V-2", 3, "Build main application window, navigation and sidebar",
     ["main.py", "ui/app.py"], [],
     "Create the application entry point and the main Tkinter window that switches between views. "
     "Includes the sidebar with the current page highlighted. Review the existing "
     "ui/dashboard_view.py and the existing sidebar work before adding anything; do not rewrite "
     "what is already done. Use placeholder screens until the other views are ready.",
     ["main.py starts the app and initializes the database",
      "ui/app.py with a view-switching mechanism",
      "Sidebar with active page indicator",
      "Existing dashboard reviewed, not rewritten",
      "Placeholder screens for views not yet ready"]),

    ("S-4", 3, "Connect login view to AuthService",
     ["ui/login_view.py"], ["S-2"],
     "The login screen is already built. Review it and connect it to the real AuthService.login, "
     "show clear success and error messages from the custom exceptions, and hand the logged-in "
     "user (with role) to the main application. No SQL in this file.",
     ["Call AuthService.login on submit",
      "Show error messages for AuthenticationError / ValidationError",
      "Pass the logged-in user to ui/app.py",
      "Existing design preserved"]),

    ("V-3", 3, "Role-based navigation after login",
     ["ui/app.py", "ui/dashboard_view.py"], ["V-2", "S-4"],
     "After a successful login, show the correct navigation based on the user role. Administrators "
     "see equipment, reservations, maintenance and reports; researchers see only equipment browsing "
     "and their own reservations. Unauthorized screens must not be reachable.",
     ["Admin menu: equipment, reservations, maintenance, reports",
      "Researcher menu: equipment, my reservations",
      "Dashboard content depends on role",
      "Logout returns to the login screen"]),

    ("V-4", 3, "Equipment view: admin interface",
     ["ui/equipment_view.py"], ["V-1", "D-7"],
     "Build the administrator part of the equipment screen: a table of equipment with add, edit "
     "and retire actions, plus search and filtering by category and status. Use EquipmentService "
     "only; no SQL. Show success and error messages for every action.",
     ["Equipment table (Treeview)",
      "Add and edit forms",
      "Retire button with confirmation",
      "Search and filters by category and status",
      "Success and error messages"]),

    ("V-5", 3, "Equipment view: category management",
     ["ui/equipment_view.py"], ["V-4"],
     "Add category management to the admin side of the equipment screen: list categories, add and "
     "edit them, with a first-level check that the name is not empty or duplicated before calling "
     "the service.",
     ["Category list",
      "Add and edit category",
      "Duplicate / empty name feedback",
      "Category filter in the equipment table refreshes after changes"]),

    ("V-6", 3, "Equipment view: researcher interface",
     ["ui/equipment_view.py"], ["V-4"],
     "Add the researcher mode to the same equipment screen. Researchers can browse equipment, "
     "search by name or category and see details and condition. Available and unavailable equipment "
     "must be clearly distinguished, and admin actions (add, edit, retire) must be hidden.",
     ["Read-only equipment table for researchers",
      "Search by name or category",
      "Equipment details panel",
      "Clear Available / Unavailable indication",
      "Admin actions hidden"]),

    ("N-6", 3, "Maintenance view",
     ["ui/maintenance_view.py"], ["N-5"],
     "Build the maintenance screen for administrators: list maintenance requests, create a new "
     "request for a piece of equipment, view request details, update the status and mark "
     "maintenance as completed. Also show which equipment is currently under maintenance. "
     "Use MaintenanceService only.",
     ["Maintenance requests table",
      "New request form",
      "Details panel",
      "Update status / complete maintenance",
      "Show equipment currently under maintenance",
      "Success and error messages"]),

    ("N-7", 3, "Reservation view: admin interface",
     ["ui/reservation_view.py"], ["M-5"],
     "Build the administrator part of the reservation screen: a table of all reservations with "
     "their statuses and details, approve and reject actions (reject requires a reason), cancel "
     "according to permissions, and a clear message when a conflict occurs. Use ReservationService "
     "only.",
     ["All reservations table with status",
      "Reservation details",
      "Approve and reject (with reason dialog)",
      "Cancel according to permissions",
      "Show conflict / error messages"]),

    ("N-8", 3, "Reservation view: researcher 'My Reservations'",
     ["ui/reservation_view.py"], ["N-7", "M-4"],
     "Add the researcher mode to the reservation screen. Researchers can create a reservation "
     "(choose equipment, start, end, purpose), see only their own reservations with status, and "
     "cancel eligible ones. Admin actions must be hidden.",
     ["Create reservation form",
      "My reservations table (own data only)",
      "Cancel eligible reservation",
      "Validation messages from ReservationService",
      "Admin actions hidden"]),

    ("S-7", 3, "Reports view",
     ["ui/reports_view.py"], ["S-6"],
     "Build the reports screen for administrators. The user picks a date range, the usage report is "
     "shown in a table, and an Export CSV button saves it through the CSV exporter with a "
     "success or error message.",
     ["Date range selection",
      "Results table",
      "Export CSV button with file dialog",
      "Success and error messages"]),

    ("V-7", 3, "Connect dashboard to real data",
     ["ui/dashboard_view.py"], ["D-7", "M-4", "N-5"],
     "The dashboard is already designed. Connect it to real data through the services: number of "
     "equipment, number of reservations and equipment under maintenance. The content must match "
     "the user's role.",
     ["Equipment count",
      "Reservations count",
      "Under-maintenance count",
      "Role-based content",
      "Existing design preserved"]),

    ("V-8", 3, "Manual test of navigation and permissions",
     ["ui/ (all views)"], ["V-3", "V-6", "V-7"],
     "Manually test every screen for navigation and permissions, for both Admin and Researcher "
     "accounts. Report bugs to the owner of the relevant file instead of editing it.",
     ["Navigate through every screen",
      "Verify admin permissions",
      "Verify researcher permissions",
      "Report bugs as issues to file owners"]),

    # ======================= DIAGRAMS =======================
    ("D-9", 6, "Final ERD diagram",
     ["diagrams/"], ["D-3"],
     "Create the final Entity Relationship Diagram matching the implemented schema.sql.",
     ["All six tables and relationships",
      "PK/FK marked",
      "Matches schema.sql exactly"]),

    ("M-7", 6, "Architecture diagram",
     ["diagrams/"], [],
     "Create the system architecture diagram showing the three layers (Presentation, Business "
     "Logic, Data Access) and the data flow between them.",
     ["Three layers with their components",
      "Data flow arrows",
      "Matches the final project structure"]),

    ("S-8", 6, "Use case diagram",
     ["diagrams/"], [],
     "Create the use case diagram for the Administrator and Researcher roles covering all "
     "main system features.",
     ["Admin and Researcher actors",
      "All use cases from the README",
      "Include / extend relations where relevant"]),

    ("N-9", 6, "Activity diagram",
     ["diagrams/"], [],
     "Create an activity diagram of the reservation lifecycle from creation through approval or "
     "rejection to completion or cancellation, including the conflict check.",
     ["Start to end flow",
      "Decision points (conflict, approve/reject)",
      "Matches the status transition rules"]),

    # ======================= TEAM PHASES =======================
    ("ALL-1", 4, "Integration: connect all views, services and repositories",
     ["Whole project"], ["V-8", "N-8", "S-7", "N-6"],
     "Integrate all layers and verify the application works end to end. Run the complete scenarios "
     "below and confirm the architecture rules: no SQL in ui/ and no GUI code in data/.",
     ["Full scenario: login, add equipment, reserve, approve, complete, export report CSV",
      "Maintenance scenario: equipment cannot be reserved while under maintenance and returns to "
      "Available after completion",
      "No SQL in ui/ and no GUI code in data/",
      "Merge integrated work into develop"]),

    ("ALL-2", 5, "Final testing",
     ["tests/"], ["ALL-1"],
     "Run the full test suite and test permissions, invalid input and CSV export across the "
     "whole application.",
     ["python -m unittest discover -s tests passes",
      "Researcher cannot see or cancel other users' reservations",
      "Invalid input tested in every screen",
      "CSV export tested"]),

    ("ALL-3", 6, "Final delivery",
     ["README.md", "diagrams/"], ["ALL-2", "D-9", "M-7", "S-8", "N-9"],
     "Prepare the final delivery: update documentation, finish all four diagrams, prepare the "
     "two-minute demo and merge develop into main after the last successful test run.",
     ["README updated to reflect the final state",
      "Four diagrams complete: ERD, Architecture, Use Case, Activity",
      "Two-minute demo prepared",
      "Merge develop into main"]),
]

DOD = """## Definition of Done
- [ ] Code tested locally
- [ ] Pull Request opened against `develop` and reviewed by another member
- [ ] No SQL in `ui/` and no GUI code in `data/`
- [ ] Function contracts in the README unchanged
- [ ] Close this issue and move on to the next task"""


def owner_key(task_id):
    return task_id.split("-")[0]


def build_body(task):
    tid, _phase, title, files, deps, desc, checklist = task
    owner = OWNERS[owner_key(tid)][0]
    out = [f"**Owner:** {owner}", "", "## Task", title, "", "## Description", desc, "",
           "## File(s)"]
    out += [f"- `{f}`" for f in files]
    out += ["", "## Depends on"]
    if deps:
        out += [f"- `{d}`" for d in deps]
        out.append("")
        out.append("Do not start until the tasks above are done.")
    else:
        out.append("- Nothing, you can start immediately.")
    out += ["", "## Checklist"]
    out += [f"- [ ] {c}" for c in checklist]
    out += ["", DOD]
    return "\n".join(out)


def run(cmd, dry):
    if dry:
        print("DRY:", " ".join(cmd[:6]), "...")
        return True
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERROR:", r.stderr.strip())
        return False
    if r.stdout.strip():
        print(r.stdout.strip())
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", help="USER/REPO (optional)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    repo = ["--repo", args.repo] if args.repo else []

    for _k, (_n, label, color) in OWNERS.items():
        run(["gh", "label", "create", label, "--color", color, "--force"] + repo, args.dry_run)
    for _i, (label, color) in PHASES.items():
        run(["gh", "label", "create", label, "--color", color, "--force"] + repo, args.dry_run)

    for task in TASKS:
        tid, phase, title, *_ = task
        labels = [OWNERS[owner_key(tid)][1], PHASES[phase][0]]
        cmd = ["gh", "issue", "create",
               "--title", f"[{tid}] {title}",
               "--body", build_body(task),
               "--label", ",".join(labels)] + repo
        if not run(cmd, args.dry_run):
            sys.exit("Stopped because of an error. Check the message above "
                     "(usually you need to run: gh auth login).")

    print(f"\nDone. Issues created: {len(TASKS)}")


if __name__ == "__main__":
    main()
