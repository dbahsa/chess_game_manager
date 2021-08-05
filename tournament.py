from dataclasses import dataclass, field

class Tournament:
    name: str
    location: str
    start_date: str
    description: str
    timer: str
    number_of_rounds: int = field(default=4)
    end_date = str
    