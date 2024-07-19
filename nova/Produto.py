class Produto:
    def __init__(self, item_code, description, unit, price):
        self.item_code = item_code
        self.description = description
        self.unit = unit
        self.price = price

    def to_dict(self):
        return {
            "Item Code": self.item_code,
            "Description": self.description,
            "Unit": self.unit,
            "Price": self.price
        }
