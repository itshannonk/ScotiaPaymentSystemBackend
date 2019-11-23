class Status:
    issued: bool
    paid: bool
    delivered: bool

    def __init__(self, issued: bool, paid: bool, delivered: bool):
        self.issued = issued
        self.paid = paid
        self.delivered = delivered

