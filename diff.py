from __future__ import division
from difflib import SequenceMatcher

from lib import levenshtein

start = '<'
end = '>'


class DifferRegistrar(type):

    type_to_differ_cls = {}

    def __init__(cls, *args):
        cls.type_to_differ_cls[cls.differ_type] = cls

    @classmethod
    def get_differ(cls, old, new):
        return cls.type_to_differ_cls[type(old)](old, new)


class Base(object):

    __metaclass__ = DifferRegistrar

    differ_type = None

    def __init__(self, old, new, color=False):
        self.old, self.new = old, new

    @property
    def output(self):
        raise NotImplementedError()


class NoneDiffer(Base):

    differ_type = type(None)

    @property
    def output(self):
        if self.new is None:
            return str(None)
        return start + str(None) + end


class BooleanDiffer(Base):

    differ_type = bool

    @property
    def output(self):
        if self.old is self.new:
            return str(self.old)
        return start + str(self.old) + end


class IntegerDiffer(Base):

    differ_type = int

    def __init__(self, old, new):
        super(IntegerDiffer, self).__init__(str(old), str(new))

    @property
    def output(self):
        return StringDiffer(self.old, self.new).output.strip('"')


class FloatDiffer(IntegerDiffer):

    differ_type = float


class LongDiffer(IntegerDiffer):

    differ_type = long

    def __init__(self, old, new):
        super(LongDiffer, self).__init__(old, new)

    @property
    def output(self):
        return super(LongDiffer, self).output + 'L'


class ComplexDiffer(IntegerDiffer):

    differ_type = complex


class StringDiffer(Base):

    differ_type = str

    def __init__(self, old, new):
        super(StringDiffer, self).__init__(old, new)
        self.highlighted = [None for _ in range(len(self.old))]
        self.matches = sorted(SequenceMatcher(a=self.old,
                                              b=self.new).get_matching_blocks()[:-1],
                              key=lambda m: m.size,
                              reverse=True)

    @property
    def output(self):
        if (levenshtein(self.old, self.new) / len(self.old)) > 0.9:
            return '"<' + self.old + '>"'

        for match in self.matches:
            if match.size == 1 and match.a != match.b:
                continue

            for i in range(match.a, match.a + match.size):
                self.highlighted[i] = True

        result = []
        for char, highlight in zip(list(self.old), self.highlighted):
            if highlight is None:
                result.append(start + char + end)
            else:
                result.append(char)

        return '"' + ''.join(result).replace('><', '') + '"'


class UnicodeDiffer(Base):

    differ_type = unicode


class TupleDiffer(Base):

    differ_type = tuple

    @property
    def output(self):
        differs = []
        for old_item, new_item in zip(self.old, self.new):
            if old_item != new_item:
                differs.append(DifferRegistrar.get_differ(old_item, new_item))

        result = '('
        for differ in differs:
            result += differ.output + ', '
        return result.strip(', ') + ')'


class ListDiffer(Base):

    differ_type = list


class SetDiffer(Base):

    differ_type = set


class DictDiffer(Base):

    differ_type = dict


class FunctionDiffer(Base):

    differ_type = type(lambda x: None)


#class LambdaDiffer(Base):
#
#    # XXX: This does not belong here. Just keeping it for refrence.
#    # def isalambda(l):
#    #   return isinstance(l, type(lambda: None)) and l.__name__ == '<lambda>'
#
#    pass
