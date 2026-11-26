
import sqlite3
from pathlib import Path


# Get the directory containing this file.
# This ensures the database path works regardless of the current working directory.
BASE_DIR = Path(__file__).resolve().parent
database_path = BASE_DIR / "labshare.db"
schema_sql_path=BASE_DIR/"schema.sql"


class Database:
    """
    Manages the SQLite database connection and its basic operations.

    This class provides a centralized connection that can be shared
    with different Repository classes across the application.
    """

    def __init__(self, db_path=None):
        # Initialize connection resources.
        self.db = None
        

        try:
            if db_path is None:
                db_path=database_path
            # Establish a connection to the SQLite database.
            self.db = sqlite3.connect(db_path)

            # Allow accessing query results using column names.
            self.db.row_factory = sqlite3.Row

            # Enable foreign key constraints for this connection.
            self.db.execute("PRAGMA foreign_keys = ON")

        except sqlite3.Error:
            # Release any resources if the connection setup fails.
            self.close()

            # Re-raise the original exception to be handled by the caller.
            raise
    def init_schema(self):
        """Create all tables by executing schema.sql (safe to call repeatedly)."""
        schema_sql = schema_sql_path.read_text(encoding="utf-8")
        self.db.executescript(schema_sql)

    def commit(self):
        """Save all pending changes to the database."""
        self.db.commit()

    def rollback(self):
        """Cancel all uncommitted changes in the current transaction."""
        self.db.rollback()

    def close(self):
        """
        Close the database connection.
        """
        if self.db is not None:
            self.db.close()
            self.db = None
    