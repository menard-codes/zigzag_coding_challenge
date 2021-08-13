from utils import reduce_to_letters


def is_palindrome(word: str) -> bool:
    """
    Identifies if the input word is palindromic or not.

        Parameter:
            word (str): The word to be tested.

        Returns:
            palindromic (bool): Tells if word input is a
                palindrome (True) or not (False).
    """

    simpler_lowercase_word = reduce_to_letters(word).lower()

    pointer1 = 0
    pointer2 = len(simpler_lowercase_word) - 1 if len(word) > 0 else 0

    while pointer1 <= pointer2:
        if len(word) == 0 or not simpler_lowercase_word[pointer1] == simpler_lowercase_word[pointer2]:
            return False
        else:
            pointer1 += 1
            pointer2 -= 1

    return True
