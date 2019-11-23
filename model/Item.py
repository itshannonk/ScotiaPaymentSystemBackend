class Item:
    name: str
    price: float
    id : int

    def __init__(self, name: str, price: float, id: int):
        self.name = name
        self.price = price
        self.id = id

