"""
This is the status of the Invoice: whether it's issued, paid, delivered.
"""


class Status:
    issued: bool
    paid: bool
    delivered: bool

    def __init__(self, issued: bool, paid: bool, delivered: bool):
        self.issued = issued
        self.paid = paid
        self.delivered = delivered

    """
    Converts the Status into a DICT just so it's easier to convert into a JSON file later.
    """
    def getstatus(self):
        return {
            "Issued": self.issued,
            "Paid": self.paid,
            "Delivered": self.delivered
        }
