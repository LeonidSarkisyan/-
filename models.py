import datetime
from dataclasses import dataclass


types_ext = {
    1: "Расход",
    2: "Доход"
}


@dataclass
class Transaction:
    date: str = ""
    value: int = 0
    type: str = "Расход"
    description: str = ""

    def __post_init__(self):
        if self.type not in ["Расход", "Доход"]:
            raise ValueError("Тип должен быть 'Расход' или 'Доход'")