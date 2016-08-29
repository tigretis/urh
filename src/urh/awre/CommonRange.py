import numpy as np


class CommonRange(object):
    def __init__(self, start: int, end: int, bits: str):
        """

        :param start: Start of the common range
        :param end: End of the common range
        :param value: Value of the common range e.g. 0xcafe
        """
        self.start = start
        self.end = end
        self.bits = bits
        self.messages = set()
        """:type: set of int """

    @property
    def hex_value(self):
        padded_bits = self.bits
        while len(padded_bits) % 4 != 0:
            padded_bits += "0"

        return "{0:x}".format(int(padded_bits, 2))

    def __eq__(self, other):
        if isinstance(other, CommonRange):
            return self.start == other.start and self.end == other.end and self.bits == other.bits
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, CommonRange):
            if self.start != other.start:
                return self.start < other.start
            else:
                return self.end <= other.end
        else:
            return -1

    def __repr__(self):
        return "{}-{} {} ({})".format(self.start,  self.end, self.hex_value, len(self.messages))