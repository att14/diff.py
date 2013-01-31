class Base(object):

    def __init__(self, old, new, color=False):
        self.old, self.new = old, new

    @property
    def output(self):
        raise NotImplementedError()


class NoneDiffer(Base):

    @property
    def output(self):
        if self.new is None:
            return str(None)
        return '<' + (self.old) + '>'


class BooleanDiffer(Base):

    @property
    def output(self):
        if self.old is self.new:
            return str(self.old)
        return '<' + str(self.old) + '>'


class IntegerDiffer(Base):

    @property
    def output(self):
        return StringDiffer(str(self.old), str(self.new)).output


class FloatDiffer(Base):
    pass


class LongDiffer(Base):
    pass


class ComplexDiffer(Base):
    pass


class StringDiffer(Base):

    def __init__(self, old, new):
        def pad_input():
            # XXX: StringAcceptanceTestCase.test_string_diff_len
            return (self.old.ljust(len(self.new), ' '), self.new) \
                if len(self.old) < len(self.new) \
                else (self.old, self.new.ljust(len(self.old), ' '))

        super(StringDiffer, self).__init__(old, new)
        self.old, self.new = pad_input()

    @property
    def output(self):
        highlighted = []
        prev_differed = False

        for char_old, char_new in zip(list(self.old), list(self.new)):
            if char_old == char_new:
                if prev_differed:
                    highlighted.append('>')
                highlighted.append(char_old)
                prev_differed = False
            else:
                if not prev_differed:
                    highlighted.append('<')
                highlighted.append(char_old)
                prev_differed = True

        if prev_differed:
            highlighted.append('>')

        return ''.join([char for char in highlighted])


class UnicodeDiffer(Base):
    pass


class TupleDiffer(Base):
    pass


class ListDiffer(Base):
    pass


class SetDiffer(Base):
    pass


class DictDiffer(Base):
    pass


class FunctionDiffer(Base):
    pass


class LambdaDiffer(Base):

    # XXX: This does not belong here. Just keeping it for refrence.
    # def isalambda(l):
    #   return isinstance(l, type(lambda: None)) and l.__name__ == '<lambda>'

    pass
