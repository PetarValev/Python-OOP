class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str) -> None:
        if 5 > len(value) or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        is_digit = len([d for d in value if d.isdigit()]) > 0
        is_upper_case = len([c for c in value if c.isupper()]) > 0
        is_valid_lenght = len(value) >= 8
        if not is_valid_lenght or not is_digit or not is_upper_case:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

