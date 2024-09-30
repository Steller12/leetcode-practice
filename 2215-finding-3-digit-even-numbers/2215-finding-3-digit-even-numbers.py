class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        even_numbers = set()  

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            hundreds, tens, units = num // 100, (num // 10) % 10, num % 10

            available_digits = digits.copy()

            if hundreds in available_digits:
                available_digits.remove(hundreds)
                if tens in available_digits:
                    available_digits.remove(tens)
                    if units in available_digits:
                        even_numbers.add(num)
        return sorted(even_numbers)