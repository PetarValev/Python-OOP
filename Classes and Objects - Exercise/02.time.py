class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def validate_and_update_time(self):
        if self.seconds > 59:
            self.seconds = 0
            self.minutes += 1

            if self.minutes > 59:
                self.minutes = 0
                self.hours += 1

                if self.hours > 23:
                    self.hours = 0

    def next_second(self) -> str:
        self.seconds += 1
        self.validate_and_update_time()
        return self.get_time()


clock = Time(23, 59, 59)

print(clock.next_second())