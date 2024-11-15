from dataclasses import dataclass
from datetime import date

@dataclass
class UserInfo:
    name: str
    address: str
    city: str
    state: str
    zip_code: str
    phone: str
    date: date = date.today()

    def get_formatted_address(self) -> str:
        return f"{self.city}, {self.state} {self.zip_code}" 