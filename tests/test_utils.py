from utils import reduce_to_letters


class TestStringReducer:

    def test_reduce_from_space(self):
        assert reduce_to_letters(
            'lorem ipsum dolor') == 'loremipsumdolor'

    def test_reduce_from_punctuations(self):
        assert reduce_to_letters('Hello_world!') == 'Helloworld'

    def test_reduce_from_numbers(self):
        assert reduce_to_letters('h3Ll0 W0R1D') == 'hLlWRD'
