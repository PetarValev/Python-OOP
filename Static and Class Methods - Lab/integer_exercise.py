class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value: float) -> None or str:
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer_value = 0
        for i in range(len(value)):
            if i > 0 and roman_numerals[value[i]] > roman_numerals[value[i - 1]]:
                integer_value += roman_numerals[value[i]] - 2 * roman_numerals[value[i - 1]]
            else:
                integer_value += roman_numerals[value[i]]

        return cls(integer_value)

    @classmethod
    def from_string(cls, value):
        try:
            return cls(int(str(value)))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
