# 13.7 Compute the union of intervals
from collections import namedtuple

class Interval(object):

    def __init__(self, left_state, left_num, right_num, right_state):
        self.left_state = left_state
        self.left_num = left_num
        self.right_num = right_num
        self.right_state = right_state

    def __str__(self):
        return self.left_state + str(self.left_num) + ', ' + str(self.right_num) + self.right_state

    def __repr__(self):
        return self.__str__()


def compute_union_intrvls(intervals):
    intervals = sorted(intervals, key = lambda x: x.left_num)
    union_of_intervals = set()
    new_intrvl = intervals[0]
    for intrvl in intervals[1:]:
        if intrvl.left_num <= new_intrvl.right_num and intrvl.right_num >= new_intrvl.right_num:
            new_intrvl.right_state = ']'

            if intrvl.right_state == ')' and intrvl.right_num > new_intrvl.right_num:
                new_intrvl.right_state = ')'

            new_intrvl.right_num = intrvl.right_num

        elif intrvl.left_num > new_intrvl.right_num:
            union_of_intervals.add(new_intrvl)
            new_intrvl = intrvl
        elif intrvl.left_state =='[' and intrvl.left_num == new_intrvl.left_num:
            new_intrvl.left_state = '['

    union_of_intervals.add(new_intrvl)

    return sorted(union_of_intervals, key = lambda x: x.left_num)


# 13.7 Compute the union of intervals [REDUX] <----- better than the first one

Point = namedtuple('Point', ('val', 'closed'))

class Interval(object):

    def __init__(self, p1 = None, p2 = None):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        b1 = '[' if self.p1.closed else '('
        b2 = ']' if self.p2.closed else ')'

        return f"{b1}{str(self.p1.val)}, {str(self.p2.val)}{b2}"

    def __repr__(self):
        return self.__str__() 

def merge_intervals(intervals):
    merged_intervals = []

    if intervals:
        intervals = sorted(intervals, key = lambda x: x.p1)
        mi = Interval(intervals[0].p1, intervals[0].p2)

        for intrvl in intervals[1:]:
            if (intrvl.p1.val <= mi.p2.val and intrvl.p2.val >= mi.p2.val) or intrvl.p1.val == mi.p2.val:
                mi.p1 = Point(
                    val = mi.p1.val,
                    closed = intrvl.p1.closed if mi.p1.val == intrvl.p1.val and intrvl.p1.closed else mi.p1.closed
                )

                mi.p2 = Point(
                    val = intrvl.p2.val,
                    closed = mi.p2.closed if mi.p2.val == intrvl.p2.val and mi.p2.closed else intrvl.p2.closed
                )

            elif intrvl.p1.val > mi.p2.val:
                merged_intervals.append(mi)
                mi = Interval(intrvl.p1, intrvl.p2)

        merged_intervals.append(mi)

    return merged_intervals

# 13.10 Implement fast sorting algorithm for lists

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        top = self
        while top:
            print(top.val)
            top = top.next


def sort_list(top):
    dummy_head = Node(float('-inf'))
    dummy_head.next = top

    while top and top.next:
        if top.val > top.next.val:
            pre, target = dummy_head, top.next

            while pre.next.val < target.val:
                pre = pre.next

            top.next, target.next, pre.next = target.next, pre.next, target
        else:
            top = top.next

    return dummy_head.next
        

    
if __name__ == '__main__':
    intervals = [
        Interval(Point(5, True), Point(10, True)),
        Interval(Point(2, False), Point(7, False)),
        Interval(Point(20, True), Point(30, True)),
        Interval(Point(10, False), Point(14, False)),
        Interval(Point(29, False), Point(34, True)),
        Interval(Point(30, False), Point(31, False)),
    ] 

    print(merge_intervals(intervals))

    # a = Node(10)
    # b = Node(7)
    # c = Node(2)
    # d = Node(7)
    # e = Node(6)

    # a.next = b
    # b.next = c
    # c.next = d
    # d.next = e

    # new = sort_list(a)
    # new.traverse()     

    # res = compute_union_intrvls({
    #     Interval('(', 16, 17, ')'),
    #     Interval('(', 13, 15, ')'),
    #     Interval('(', 12, 16, ']'),
    #     Interval('[', 12, 14, ']'),
    #     Interval('[', 2, 4, ']'),
    #     Interval('[', 1, 1, ']'),
    #     Interval('[', 3, 4, ')'),
    #     Interval('(', 0, 3, ')'),
    #     Interval('[', 5, 7, ')'),
    #     Interval('[', 8, 11, ')'),
    #     Interval('[', 7, 8, ')'),
    #     Interval('(', 9, 11, ']'),
    # })
    # print(res)
    



