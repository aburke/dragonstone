from enum import Enum
from collections import namedtuple

class State(Enum):
    open = 1
    closed = 2

Point = namedtuple('Point', ['val', 'state'])

class Interval(object):

    def __init__(self, p1, p2):
        self.p1, self.p2 = sorted([p1, p2], key = lambda p: p.val)

    def __repr__(self):
        left_b = '[ ' if self.p1.state == State.closed else '( '
        right_b = ' ]' if self.p2.state == State.closed else ' )'
        return left_b + str(self.p1.val) + ', ' + str(self.p2.val) + right_b

    def __eq__(self, other):
        return all([
            self.p1.val == other.p1.val,
            self.p1.state == other.p1.state,
            self.p2.val == other.p2.val,
            self.p2.state == other.p2.state
        ])


def compute_union(intervals):
    consolidation = []
    if intervals:
        ordered_intrvls = sorted(intervals, key = lambda intrvl: intrvl.p1.val)
        start, end = ordered_intrvls[0].p1, ordered_intrvls[0].p2
        for i in range(1, len(ordered_intrvls)):
            intrvl = ordered_intrvls[i]

            if intrvl.p1.val == start.val and intrvl.p1.state == State.closed:
                start = Point(start.val, State.closed)

            if intrvl.p1.val <= end.val and intrvl.p2.val >= end.val:
                state = intrvl.p2.state
                if intrvl.p2.val == end.val and end.state == State.closed:
                    state = state.closed
                end = Point(intrvl.p2.val, state)
            elif intrvl.p1.val > end.val:
                consolidation.append(Interval(start, end))
                start, end = intrvl.p1, intrvl.p2

        consolidation.append(Interval(start, end))

    return consolidation

