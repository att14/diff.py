from difflib import SequenceMatcher


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
        return '<' + str(None) + '>'


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


class FloatDiffer(IntegerDiffer):
    pass


class LongDiffer(Base):
    pass


class ComplexDiffer(Base):
    pass


class StringDiffer(Base):

    highlight_start = '<'
    highlight_end = '>'

    def __init__(self, old, new):
        super(StringDiffer, self).__init__(old, new)
        self.highlighted = [None for _ in range(len(self.old))]
        self.matches = sorted(SequenceMatcher(a=self.old,
                                              b=self.new).get_matching_blocks(),
                              key=lambda m: m.a)

    @property
    def output(self):
        print self.matches
        for match in self.matches:
            # XXX: Need more testing around this statement.
            #if match.size == 1 and match.a != match.b:
            #    continue

            for i in range(match.a, match.a + match.size):
                self.highlighted[i] = True

        result = []
        for char, highlight in zip(list(self.old), self.highlighted):
            if highlight is None:
                result.append('<' + char + '>')
            else:
                result.append(char)

        return ''.join(result).replace('><', '')


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
