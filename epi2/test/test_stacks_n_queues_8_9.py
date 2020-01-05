import epi2.stacks_n_queues_8_9 as sq

def test_scenario1():
    q = sq.Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert 1 == q.dequeue()

def test_scenario2():
    q = sq.Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    q.enqueue(4)
    q.enqueue(5)
    q.dequeue()
    q.enqueue(6)
    assert q.dequeue() == 4

def test_scenario3():
    q = sq.Queue()
    q.enqueue(1)
    q.dequeue()
    try:
        q.dequeue()
    except Exception as e:
        assert isinstance(e, sq.EmptyQueueException)

    assert q.is_empty()