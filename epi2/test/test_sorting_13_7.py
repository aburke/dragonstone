from epi2.sorting_13_7 import compute_union, Interval, Point, State

def test_scenario1():
    intervals = {
        '(0, 3)': Interval(Point(0, State.open), Point(3, State.open)),
        '[1, 1]': Interval(Point(1, State.closed), Point(1, State.closed)),
        '[2, 4]': Interval(Point(2, State.closed), Point(4, State.closed)),
        '[3, 4)': Interval(Point(3, State.closed), Point(4, State.open)),
        '[5, 7)': Interval(Point(5, State.closed), Point(7, State.open)),
        '[7, 8)': Interval(Point(7, State.closed), Point(8, State.open)),
        '[8, 11)': Interval(Point(8, State.closed), Point(11, State.open)),
        '(9, 11]': Interval(Point(9, State.open), Point(11, State.closed)),
        '(12, 16]': Interval(Point(12, State.open), Point(16, State.closed)),
        '[12, 14]': Interval(Point(12, State.closed), Point(14, State.closed)),
        '(13, 15)': Interval(Point(13, State.open), Point(15, State.open)),
        '(16, 17)': Interval(Point(16, State.open), Point(17, State.open))
    }
    expected = [
        Interval(Point(0, State.open), Point(4, State.closed)),
        Interval(Point(5, State.closed), Point(11, State.closed)),
        Interval(Point(12, State.closed), Point(17, State.open))
    ]
    assert compute_union(intervals.values()) == expected