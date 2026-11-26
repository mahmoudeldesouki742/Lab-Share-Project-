
from Config import RESERVATION_STATUSES
from logic.exceptions import ValidationError


class Reservation:
    """Represents a single reservation record."""

    def __init__(
        self,
        reservation_id,
        user_id,
        equipment_id,
        start_time,
        end_time,
        purpose,
        status="Pending",
        rejection_reason=None,
        created_at=None
    ):
        """Initialize a reservation with its basic information."""

        # Validate the reservation status.
        if status not in RESERVATION_STATUSES:
            raise ValidationError(
                f"Invalid status: {status}. "
                f"Must be one of {RESERVATION_STATUSES}."
            )

        # Assign reservation attributes.
        self.reservation_id = reservation_id
        self.user_id = user_id
        self.equipment_id = equipment_id
        self.start_time = start_time
        self.end_time = end_time
        self.purpose = purpose
        self.status = status
        self.rejection_reason = rejection_reason
        self.created_at = created_at

    @classmethod
    def from_dict(cls, row):
        """Create a Reservation object from a dictionary or database row."""
        return cls(**dict(row))

    def to_dict(self):
        """Convert the reservation object into a dictionary."""
        return dict(self.__dict__)

    def is_final(self):
        """Check whether the reservation has reached a final status."""
        return self.status in ("Rejected", "Cancelled", "Completed")