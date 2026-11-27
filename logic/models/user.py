from Config import ROLES
from logic.exceptions import ValidationError

class User:
    """Represents a single user record."""

    def __init__(self , user_id , username , password_hash , fullname , role , created_at = None):
        """Initialize a user with its basic information."""

        # Validate the user role.
        if role not in ROLES:
            raise ValidationError(
                f"Invalid role: {role}. "
                f"Must be one of {ROLES}."
            )
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.fullname = fullname
        self.role = role
        self.created_at = created_at
    @classmethod
    def from_dict(cls, row):
        """Create a User object from a dictionary or database row."""
        return cls(**dict(row))
    def  is_admin(self):
        """Check if the user has an admin role."""
        return self.role == "Admin"
    def  is_researcher(self):
            """Check if the user has a researcher role."""
            return self.role == "Researcher"
    def __repr__(self):
        """Return a safe string representation of the user."""
        return f"User({self.user_id}, {self.username}, {self.role})"
