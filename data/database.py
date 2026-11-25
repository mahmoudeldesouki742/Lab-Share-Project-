import sqlite3
from pathlib import Path


# Get the directory containing this file.
# This ensures the database path works regardless of the current working directory.
BASE_DIR = Path(__file__).resolve().parent
database_path = BASE_DIR / "labshare.db"


class Database:
    """
    Manages the SQLite database connection and its basic operations.

    This class provides a centralized connection that can be shared
    with different Repository classes across the application.
    """

    def __init__(self):
        # Initialize connection resources.
        self.db = None
        self.cursor = None

        try:
            # Establish a connection to the SQLite database.
            self.db = sqlite3.connect(database_path)

            # Allow accessing query results using column names.
            self.db.row_factory = sqlite3.Row

            # Create a cursor for executing SQL statements.
            self.cursor = self.db.cursor()

            # Enable foreign key constraints for this connection.
            self.cursor.execute("PRAGMA foreign_keys = ON")

        except sqlite3.Error:
            # Release any resources if the connection setup fails.
            self.close()

            # Re-raise the original exception to be handled by the caller.
            raise

    def commit(self):
        """Save all pending changes to the database."""
        self.db.commit()

    def rollback(self):
        """Cancel all uncommitted changes in the current transaction."""
        self.db.rollback()

    def close(self):
        """
        Close the cursor and database connection.

        This method checks whether each resource exists before closing it,
        preventing errors when cleanup is performed after partial initialization.
        """

        # Close the cursor if it exists.
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None

        # Close the database connection if it exists.
        if self.db is not None:
            self.db.close()
            self.db = None
