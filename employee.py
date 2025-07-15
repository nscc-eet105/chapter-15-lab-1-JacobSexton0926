#Jacob Sexton 7/15/25

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    hours_worked: float
    hourly_rate: float

    def calc_pay(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Hours Worked: {self.hours_worked}\n"
            f"Hourly Rate: ${self.hourly_rate:.2f}"
        )

@dataclass
class Salesperson(Employee):
    weekly_sales: float
    commission_percent: float

    def calc_pay(self):
        base_pay = super().calc_pay()
        commission = self.weekly_sales * self.commission_percent
        return base_pay + commission

    def __str__(self):
        return (
            super().__str__() + "\n"
            f"Weekly Sales: ${self.weekly_sales:.2f}\n"
            f"Commission %: {self.commission_percent:.2%}"
        )
