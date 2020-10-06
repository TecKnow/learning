# Roman numeral conversion algorithm from Paul Winkler,
# licensed under the PSF License and available at the following URL:
# https://code.activestate.com/recipes/81611-roman-numerals/
from functools import total_ordering
from typing import Union


@total_ordering
class RomanNumeral:

    @staticmethod
    def roman_to_int(input_string: str) -> int:
        """
        Convert a roman numeral to an integer.

        >>> r = list(range(1, 4000))
        >>> nums = [RomanNumeral.int_to_roman(i) for i in r]
        >>> ints = [RomanNumeral.roman_to_int(n) for n in nums]
        >>> print(r == ints)
        1

        >>> RomanNumeral.roman_to_int('VVVIV')
        Traceback (most recent call last):
         ...
        ValueError: input is not a valid roman numeral: VVVIV
        >>> RomanNumeral.roman_to_int(1)
        Traceback (most recent call last):
         ...
        TypeError: expected string, got <class 'int'>
        >>> RomanNumeral.roman_to_int('a')
        Traceback (most recent call last):
         ...
        ValueError: input is not a valid roman numeral: A
        >>> RomanNumeral.roman_to_int('IL')
        Traceback (most recent call last):
         ...
        ValueError: input is not a valid roman numeral: IL
        """
        if not isinstance(input_string, str):
            raise TypeError("expected string, got %s" % type(input_string))
        input_string = input_string.upper()
        nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        ints = [1000, 500, 100, 50, 10, 5, 1]
        places = []
        for c in input_string:
            if c not in nums:
                raise ValueError("input is not a valid roman numeral: %s" % input_string)
        for i in range(len(input_string)):
            c = input_string[i]
            value = ints[nums.index(c)]
            # If the next place holds a larger number, this value is negative.
            try:
                next_value = ints[nums.index(input_string[i + 1])]
                if next_value > value:
                    value *= -1
            except IndexError:
                # there is no next place.
                pass
            places.append(value)
        cur_sum = 0
        for n in places:
            cur_sum += n
        return cur_sum
        # Easiest test for validity...
        # if RomanNumeral.int_to_roman(cur_sum) == input_string:
        #     return cur_sum
        # else:
        #     raise ValueError('input is not a valid roman numeral: %s' % input_string)

    @staticmethod
    def int_to_roman(input_int: int) -> str:
        """
        Convert an integer to Roman numerals.

        Examples:
        >>> RomanNumeral.int_to_roman(0)
        Traceback (most recent call last):
        ValueError: Argument must be between 1 and 3999

        >>> RomanNumeral.int_to_roman(-1)
        Traceback (most recent call last):
        ValueError: Argument must be between 1 and 3999

        >>> RomanNumeral.int_to_roman(1.5)
        Traceback (most recent call last):
        TypeError: expected integer, got <class 'float'>

        >>> for i in range(1, 21): print (RomanNumeral.int_to_roman(i))
        ...
        I
        II
        III
        IV
        V
        VI
        VII
        VIII
        IX
        X
        XI
        XII
        XIII
        XIV
        XV
        XVI
        XVII
        XVIII
        XIX
        XX
        >>> print( RomanNumeral.int_to_roman(2000))
        MM
        >>> print( RomanNumeral.int_to_roman(1999))
        MCMXCIX
        """
        if not isinstance(input_int, int):
            raise TypeError("expected integer, got %s" % type(input_int))
        if not 0 < input_int < 4000:
            raise ValueError("Argument must be between 1 and 3999")
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = ""
        for i in range(len(ints)):
            count = int(input_int / ints[i])
            result += nums[i] * count
            input_int -= ints[i] * count
        return result

    @staticmethod
    def from_int(value: int):
        return RomanNumeral(value)

    def __init__(self, source: Union[int, str]):
        if isinstance(source, self.__class__):
            source = source.int_value
        self.int_value = source if isinstance(source, int) else self.roman_to_int(source)
        self.roman_numeral = source if isinstance(source, str) else self.int_to_roman(source)

    def __int__(self):
        return self.int_value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.roman_numeral}')"

    def __str__(self):
        return self.roman_numeral

    def __add__(self, other):
        try:
            return RomanNumeral(int(self) + int(other))
        except ValueError:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, str):
            try:
                return int(self) == int(RomanNumeral(other))
            except ValueError:
                pass
        try:
            return int(self) == int(other)
        except ValueError:
            return NotImplemented

    def __gt__(self, other):
        try:
            return int(self) > int(other)
        except ValueError:
            return NotImplemented
