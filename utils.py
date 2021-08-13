from re import findall


def reduce_to_letters(string: str) -> str:
    """
    Removes special characters, numbers, punctuations, etc.
    from the string input.

        Parameter:
            string (str): The string to be reduced to letters
            only and covert into lowercase.

        Returns:
            reduced_string (str): The reduced version of the string
    """

    letters_regex = r'[A-Za-z]+'
    reduced_string = ''.join(findall(letters_regex, string))
    return reduced_string
