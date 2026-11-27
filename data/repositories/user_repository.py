import sqlite3
from logic.exceptions import DataAccessError
from contextlib import closing


class UserRepository:
    """Handles database operations for users."""

    def __init__(self, database):
        """Initialize the repository with a database instance."""
        self.database = database

    def add_user(self, username, password_hash, full_name, role):
        """Add a new user and return their ID."""
        try:
            with closing(self.database.db.cursor()) as cursor:
                t = (username, password_hash, full_name, role)

                # Insert the new user into the database.
                cursor.execute(
                    "INSERT INTO Users(username, password_hash, full_name, role) VALUES (?, ?, ?, ?)",
                    t
                )
                user_id = cursor.lastrowid

            self.database.commit()
            return user_id

        except sqlite3.IntegrityError as error:
            self.database.rollback()

            if "Users.username" in str(error):
                raise DataAccessError("Username already exists") from error

            raise DataAccessError(str(error)) from error

        except sqlite3.Error as error:
            self.database.rollback()
            raise DataAccessError(str(error)) from error

    def get_by_id(self, user_id):
        """Retrieve a user by ID, or return None if not found."""
        try:
            with closing(self.database.db.cursor()) as cursor:
                cursor.execute(
                    "SELECT * FROM Users WHERE user_id = ?",
                    (user_id,)
                )
                row = cursor.fetchone()

                if row is None:
                    return None

                return dict(row)

        except sqlite3.Error as error:
            raise DataAccessError(str(error)) from error

    def get_by_username(self, username):
        """Retrieve a user by username, or return None if not found."""
        try:
            with closing(self.database.db.cursor()) as cursor:
                cursor.execute(
                    "SELECT * FROM Users WHERE username = ?",
                    (username,)
                )
                row = cursor.fetchone()

                if row is None:
                    return None

                return dict(row)

        except sqlite3.Error as error:
            raise DataAccessError(str(error)) from error

    def get_all_users(self):
        """Return all users without their password hashes."""
        try:
            with closing(self.database.db.cursor()) as cursor:
                cursor.execute(
                    """
                    SELECT user_id, username, full_name, role, created_at
                    FROM Users
                    """
                )
                rows = cursor.fetchall()

                return [dict(item) for item in rows]

        except sqlite3.Error as error:
            raise DataAccessError(str(error)) from error
