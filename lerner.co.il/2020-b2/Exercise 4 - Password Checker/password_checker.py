from string import punctuation
from typing import Tuple, Mapping, Callable


def create_password_checker(min_uppercase: int = 0,
                            min_lowercase: int = 0,
                            min_punctuation: int = 0,
                            min_digits: int = 0) -> Callable[
                                [str], Tuple[bool, Mapping[str, int]]]:
    def check_function(password: str) -> Tuple[bool, Mapping[str, int]]:
        result_dict = dict()
        result_dict['uppercase'] = len([x for x in password if x.isupper()]) - min_uppercase
        result_dict['lowercase'] = len([x for x in password if x.islower()]) - min_lowercase
        result_dict['punctuation'] = len([x for x in password if x in punctuation]) - min_punctuation
        result_dict['digits'] = len([x for x in password if x.isdigit()]) - min_digits
        good_password = all(value >= 0 for value in result_dict.values())
        return good_password, result_dict

    return check_function
