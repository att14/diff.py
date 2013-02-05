import diff
import unittest


class NoneAcceptanceTestCase(unittest.TestCase):

    def test_none_diff(self):
        bool_diff = diff.BooleanDiffer(None, False)
        self.assertEqual('<None>', bool_diff.output)

    def test_none_same(self):
        bool_diff = diff.BooleanDiffer(None, None)
        self.assertEqual('None', bool_diff.output)


class BooleanAcceptanceTestCase(unittest.TestCase):

    def test_bool_diff(self):
        bool_diff = diff.BooleanDiffer(True, False)
        self.assertEqual('<True>', bool_diff.output)

    def test_bool_same(self):
        bool_diff = diff.BooleanDiffer(False, False)
        self.assertEqual('False', bool_diff.output)


class IntegerDifferAcceptanceTestCase(unittest.TestCase):

    def test_integer_diff(self):
        integer_diff = diff.IntegerDiffer(1234567890, 1234557890)
        self.assertEqual('12345<6>7890', integer_diff.output)

    def test_integer_diff_one_char(self):
        integer_diff = diff.IntegerDiffer(1234567890, 1024)
        self.assertEqual('1<23>4<567890>', integer_diff.output)

    def test_integer_same(self):
        integer_diff = diff.IntegerDiffer(1234567890, 1234567890)
        self.assertEqual('1234567890', integer_diff.output)

    def test_integer_diff_len(self):
        integer_diff = diff.IntegerDiffer(1234567890, 123456)
        self.assertEqual('123456<7890>', integer_diff.output)

        integer_diff = diff.IntegerDiffer(123456, 1234567890)
        self.assertEqual('123456', integer_diff.output)


class FloatDifferAcceptanceTestCase(unittest.TestCase):

    def test_float_diff(self):
        float_diff = diff.FloatDiffer(3.14529, 3.24529)
        self.assertEqual('3.<1>4529', float_diff.output)


class ComplexDifferAcceptanceTestCase(unittest.TestCase):

    def test_complex_diff(self):
        complex_diff = diff.ComplexDiffer(12j, 2j)
        self.assertEqual('<1>2j', complex_diff.output)

    def test_complex_addition(self):
        complex_diff = diff.ComplexDiffer(2+1j, 2j)
        self.assertEqual('<(2+1j)>', complex_diff.output)


class LongDifferAcceptanceTestCase(unittest.TestCase):

    def test_long_diff(self):
        long_diff = diff.LongDiffer(1234567890L, 12345L)
        self.assertEqual('12345<67890>L', long_diff.output)


class StringAcceptanceTestCase(unittest.TestCase):

    def test_string_diff(self):
        string_diff = diff.StringDiffer('this is the old string',
                                        'this is the new string')

        self.assertEqual('"this is the <old> string"', string_diff.output)

    def test_xxx(self):
        string_diff = diff.StringDiffer('bane is the string',
                                        'dean is the string')

        self.assertEqual('"<b>an<e> is the string"', string_diff.output)


    def test_one_char(self):
        string_diff = diff.StringDiffer('abcdefg', 'hialmn')
        self.assertEqual('"<abcdefg>"', string_diff.output)

        string_diff = diff.StringDiffer('abcdefghilm', 'hialmn')
        self.assertEqual('"<abcdefg>hilm"', string_diff.output)

    def test_string_diff_beginning(self):
        string_diff = diff.StringDiffer('this is the old string',
                                        'kiss is the old string')

        self.assertEqual('"<thi>s is the old string"', string_diff.output)

    def test_string_diff_end(self):
        string_diff = diff.StringDiffer('this is the old string',
                                        'this is the old strina')

        self.assertEqual('"this is the old strin<g>"', string_diff.output)

    def test_string_same(self):
        string_diff = diff.StringDiffer('this is the old string',
                                        'this is the old string')

        self.assertEqual('"this is the old string"', string_diff.output)

    def test_string_diff_len(self):
        string_diff = diff.StringDiffer('this is the old string',
                                        'this is the old')

        self.assertEqual('"this is the old< string>"', string_diff.output)

        string_diff = diff.StringDiffer('this is the old string',
                                        'this is the old strings')

        self.assertEqual('"this is the old string"', string_diff.output)

    def test_string_newline(self):
        string_diff = diff.StringDiffer('this is \nthe old string',
                                        'this is the old string')

        self.assertEqual('"this is <\n>the old string"', string_diff.output)

    def test_string_multiple_diff(self):
        string_diff = diff.StringDiffer('this is the old string',
                                        'this old the is string')

        self.assertEqual('"this <is> the <old> string"', string_diff.output)

        string_diff = diff.StringDiffer('this is the old string',
                                        'this new the is string')

        self.assertEqual('"this <is> the <old> string"', string_diff.output)

    def test_string_long_diff(self):
        string_diff = diff.StringDiffer('this is the old string',
                                        'this is abcdefg old string')

        self.assertEqual('"this is <the> old string"', string_diff.output)

    def test_string_empty(self):
        string_diff = diff.StringDiffer('this is the old string', '')
        self.assertEqual('"<this is the old string>"', string_diff.output)

    def test_string_contains_highlight_markers(self):
        string_diff = diff.StringDiffer('this is >< old string',
                                        'this is the old string')

        self.assertEqual('"this is <><> old string"', string_diff.output)

    def test_string_levenshtein(self):
        string1 = 'ZrBZyHZGUqkAqFuTnyfrvxVZbhFLkFExNCoqJLNhXLqqBuSpvMCKbKndacWJVwQaTxinMreutIqrcfAGvRrRllFowDiIsLQPNmMK'
        string2 = 'GTiZfTDkJUXhQmydpOVfkuqGGqWYTkRsVwJJsEejETSxSLuebcQvEgFlDiYzMqajSkjANBISPnRmZgbfLqPhRNnzJTUpYCcfqTMy'

        string_diff = diff.StringDiffer(string1, string2)

        self.assertEqual('"<%s>"' % string1, string_diff.output)

    def test_string_one_char_diff_end(self):
        # XXX: Should this highlight the c at the end?
        string_diff = diff.StringDiffer('abkxyeyec', 'abxyec')
        self.assertEqual('"ab<k>xye<yec>"', string_diff.output)


class TupleDifferAcceptanceTestCase(unittest.TestCase):

    def test_tuple_diff(self):
        tuple_diff = diff.TupleDiffer((12345, 'abcdefg'), (2345, 'abcefg'))
        self.assertEqual('(<1>2345, "abc<d>efg")', tuple_diff.output)


if __name__ == '__main__':
    unittest.main()
