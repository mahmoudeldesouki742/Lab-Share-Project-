from pathlib import Path


# ==============================
# Application Settings
# ==============================

APP_NAME = "LabShare"

WINDOW_TITLE = APP_NAME
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700


# ==============================
# Project Paths
# ==============================

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "labshare.db"


# ==============================
# Business Rules
# ==============================

MAX_RESERVATION_DAYS = 7

DATETIME_FORMAT = "%Y-%m-%d %H:%M"


# ==============================
# Allowed Values
# ==============================

ROLES = (
    "Admin",
    "Researcher",
)

EQUIPMENT_STATUSES = (
    "Available",
    "Under Maintenance",
    "Retired",
)

RESERVATION_STATUSES = (
    "Pending",
    "Approved",
    "Rejected",
    "Cancelled",
    "Completed",
)

MAINTENANCE_STATUSES = (
    "Open",
    "In Progress",
    "Completed",
)