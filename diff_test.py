import unittest

import diff


class BooleanAcceptanceTestCase(unittest.TestCase):

    def test_bool_diff(self):
        bool_diff = diff.BooleanDiffer(True, False)
        self.assertEqual('<True>', bool_diff.output)

    def test_bool_same(self):
        bool_diff = diff.BooleanDiffer(False, False)
        self.assertEqual('False', bool_diff.output)


class NoneAcceptanceTestCase(unittest.TestCase):

    def test_none_diff(self):
        bool_diff = diff.BooleanDiffer(None, False)
        self.assertEqual('<None>', bool_diff.output)

    def test_bool_same(self):
        bool_diff = diff.BooleanDiffer(None, None)
        self.assertEqual('None', bool_diff.output)


class StringAcceptanceTestCase(unittest.TestCase):

    def test_string_diff(self):
        string_diff  = diff.StringDiffer('this is the old string',
                                         'this is the new string')

        self.assertEqual('this is the <old> string', string_diff.output)

    def test_string_diff_beginning(self):
        string_diff  = diff.StringDiffer('this is the old string',
                                         'kiss is the old string')

        self.assertEqual('<thi>s is the old string', string_diff.output)

    def test_string_diff_end(self):
        string_diff  = diff.StringDiffer('this is the old string',
                                         'this is the old strina')

        self.assertEqual('this is the old strin<g>', string_diff.output)

    def test_string_same(self):
        string_diff  = diff.StringDiffer('this is the old string',
                                         'this is the old string')

        self.assertEqual('this is the old string', string_diff.output)

    def test_string_diff_len(self):
        string_diff = diff.StringDiffer('this is the old string',
                                       'this is the old')

        self.assertEqual('this is the old< string>', string_diff.output)

    def test_string_newline(self):
        string_diff  = diff.StringDiffer('this is \nthe old string',
                                         'this is the old string')

        self.assertEqual('this is <the old string>', string_diff.output)


class IntegerDifferAcceptanceTestCase(unittest.TestCase):

    def test_integer_diff(self):
        integer_diff = diff.IntegerDiffer(1234567890, 1234557890)
        self.assertEqual('12345<6>7890', integer_diff.output)

    def test_integer_diff_beginning(self):
        integer_diff = diff.IntegerDiffer(1234567890, 1234567890)
        self.assertEqual('1234567890', integer_diff.output)


if __name__ == '__main__':
    unittest.main()
