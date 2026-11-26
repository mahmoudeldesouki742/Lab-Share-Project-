class LabShareError(Exception):
    """
    Base exception for all LabShare application errors.
    All custom exceptions should inherit from this class.
    """
    
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class ValidationError(LabShareError):
    """
    Raised when the provided input or data is invalid.
    """

class AuthenticationError(LabShareError):
    """
    Raised when user authentication fails.
    """

class NotFoundError(LabShareError):
    """
    Raised when a requested resource does not exist.
    """

class PermissionError(LabShareError):
    """
    Raised when a user does not have permission
    to perform a requested operation.
    """

class ConflictError(LabShareError):
    """
    Raised when an operation conflicts with existing data.
    """

class DataAccessError(LabShareError):
    """
    Raised when an error occurs while accessing data.
    """