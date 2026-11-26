
import sys
import tempfile
from pathlib import Path


# Path to the folder containing database.py and schema.sql
DATABASE_DIR = Path(r"D:\LabShare-Project\data")

# Add the database folder to Python import path
sys.path.insert(0, str(DATABASE_DIR))

from database import Database


# Create a temporary database outside the project
with tempfile.TemporaryDirectory() as temp_dir:

    test_db_path = Path(temp_dir) / "test.db"

    db = Database(db_path=test_db_path)

    try:
        print("=== Database Tests ===\n")

        # Test 1: Initialize schema for the first time
        db.init_schema()
        print("[PASS] First schema initialization")

        # Test 2: Initialize schema for the second time
        db.init_schema()
        print("[PASS] Second schema initialization")

        # Test 3: Check created tables
        cursor = db.db.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            AND name NOT LIKE 'sqlite_%'
        """)

        tables = cursor.fetchall()

        print("\n=== Tables Found ===")

        for table in tables:
            print(f"- {table['name']}")

        print(f"\nTotal tables: {len(tables)}")

        # Test 4: Check foreign key activation
        foreign_keys = db.db.execute(
            "PRAGMA foreign_keys"
        ).fetchone()[0]

        print(
            "\nForeign keys enabled:",
            foreign_keys == 1
        )

        # Final result
        print("\n=== Final Result ===")

        if len(tables) == 6 and foreign_keys == 1:
            print("[PASS] All tests passed successfully!")
        else:
            print("[FAIL] Some tests need investigation.")

    except Exception as error:
        print("\n[ERROR] Test failed!")
        print(type(error).__name__, error)

    finally:
        db.close()
        print("\nDatabase connection closed.")
