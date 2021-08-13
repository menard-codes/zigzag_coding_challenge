from palindromes import is_palindrome


class TestLevelOne:

    def test_palindrome(self):
        assert is_palindrome('mom') == True
        assert is_palindrome('noon') == True
        assert is_palindrome('rotator') == True

    def test_palindrome_with_space(self):
        assert is_palindrome('top spot') == True
        assert is_palindrome('race car') == True
        assert is_palindrome('never odd or even') == True

    def test_palindrome_with_punctuation(self):
        assert is_palindrome('red rum, sir, is murder') == True
        assert is_palindrome("don't nod") == True
        assert is_palindrome('no_lemon,_no melon')

    def test_palindrome_with_casing(self):
        assert is_palindrome('Step on no pets.') == True
        assert is_palindrome('I did, did I?') == True
        assert is_palindrome('Eva, can I see bees in a cave?')

    def test_non_palindrome(self):
        assert is_palindrome('python') == False
        assert is_palindrome('mommy') == False
        assert is_palindrome('abracadabra') == False
