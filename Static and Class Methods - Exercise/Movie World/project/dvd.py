class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def mapper(month_number: int) -> str or None:
        mapping = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        if month_number in mapping.keys():
            return mapping[int(month_number)]

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month_number, year = date.split(".")
        month_name = DVD.mapper(int(month_number))
        return cls(name, id, int(year), month_name, age_restriction)

    def __repr__(self) -> str:
        rented_status = "rented" if self.is_rented else "not rented"
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})"
                f" has age restriction {self.age_restriction}. Status: {rented_status}")


ui = DVD("Yovo", 11294821, 1999, "December", 18)

print(ui)
