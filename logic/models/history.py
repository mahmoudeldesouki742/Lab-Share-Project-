class ReservationHistory:
    def __init__(self , history_id,
        reservation_id,
        old_status,
        new_status,
        changed_by,
        changed_at=None,
        notes=None) :
        self.history_id = history_id
        self.reservation_id = reservation_id
        self.old_status = old_status
        self.new_status = new_status
        self.changed_by = changed_by
        self.changed_at = changed_at
        self.notes = notes

    @classmethod
    def from_dict(cls, row):
        """Create a ReservationHistory object from a dictionary or database row."""
        return cls(**dict(row))
    def to_dict(self):
        """Convert the reservation history object into a dictionary."""
        return dict(self.__dict__)
    