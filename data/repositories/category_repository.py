
import sqlite3
from logic.exceptions import DataAccessError
from contextlib import closing


class CategoryRepository:
    """Handles database operations for categories."""

    def __init__(self,database):
        """Initialize the repository with a database instance."""
        self.database=database

    def add_category(self,name,description=None):
        """Add a new category and return its ID."""
        try:
            with closing(self.database.db.cursor()) as cursor:
                t = ( name, description)

                cursor.execute("INSERT INTO Categories(name,description) values(?,?) ",t)
                category_id = cursor.lastrowid

            self.database.commit()
            return category_id
        
        except sqlite3.IntegrityError as error:
            self.database.rollback()

            if "Categories.name" in str(error):
                raise DataAccessError("This Category is already exists") from error

            raise DataAccessError(str(error)) from error

        except sqlite3.Error as error:
            self.database.rollback()
            raise DataAccessError(str(error)) from error

    def update_category(self,category_id, name, description):
        """Update a category and return whether a row was affected."""
        try:
            with closing(self.database.db.cursor()) as cursor:
                t = ( name, description,category_id)
                cursor.execute("UPDATE  Categories SET name = ? ,description=? WHERE category_id = ?",t)
                rows_affected = cursor.rowcount

            self.database.commit()
            if rows_affected > 0:
                return True
            else:
                return False 

        except sqlite3.IntegrityError as error:
            self.database.rollback()
        
            if "Categories.name" in str(error):
                raise DataAccessError("This Category is already exists") from error
        
            raise DataAccessError(str(error)) from error
        
        except sqlite3.Error as error:
                self.database.rollback()
                raise DataAccessError(str(error)) from error

    def get_category(self,category_id):
        """Retrieve a category by ID, or return None if not found."""
        try:
            with closing(self.database.db.cursor()) as cursor:
                cursor.execute(
                    "SELECT * FROM Categories WHERE category_id = ?",(category_id,))
                row = cursor.fetchone()
        
                if row is None:
                    return None
        
                return dict(row)
        except sqlite3.Error as error:
            raise DataAccessError(str(error)) from error

    def get_by_name(self,name):
        """Retrieve a category by name, or return None if not found."""
        try:
            with closing(self.database.db.cursor()) as cursor:
                cursor.execute("SELECT * FROM Categories WHERE name = ?",(name,))
                row = cursor.fetchone()
                    
                if row is None:
                    return None
                    
                return dict(row)
        except sqlite3.Error as error:
            raise DataAccessError(str(error)) from error

    def get_all_categories(self):
        """Return all categories ordered by name."""
        try:
            with closing(self.database.db.cursor()) as cursor:
                cursor.execute("SELECT * FROM Categories ORDER BY name ASC")
                rows = cursor.fetchall()

                return [dict(item) for item in rows]

        except sqlite3.Error as error:
            raise DataAccessError(str(error)) from error
