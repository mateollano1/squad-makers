from typing import List, Tuple


class Math:
    @staticmethod
    def add(*, number: int) -> int:
        return number + 1

    def get_mcm_by_list(self, *, numbers: List[int]) -> int:
        a = numbers[0]
        b = numbers[1]
        mcm = self.__get_mcm_by_tuple(a=a, b=b)
        for number in range(2, len(numbers)):
            mcm = self.__get_mcm_by_tuple(a=mcm, b=numbers[number])
        return mcm

    def __get_mcm_by_tuple(self, *, a: int, b: int) -> int:
        maior, minor = self.__get_maior_minor(a=a, b=b)
        for common in range(1, minor + 1):
            if (common * maior) % minor == 0:
                return common * maior
        return common * maior

    def __get_maior_minor(self, *, a: int, b: int) -> Tuple[int, int]:
        if a >= b:
            return a, b
        return b, a


math_service = Math()
