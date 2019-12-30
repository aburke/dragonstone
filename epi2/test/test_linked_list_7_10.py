import epi2.linked_list_7_10 as ll

def get_nodes():
    one = ll.Node(1, None)
    two = ll.Node(2, None)
    three = ll.Node(3, None)
    four = ll.Node(4, None)
    five = ll.Node(5, None)

    return one, two, three, four, five

def test_scenario1():
    expected = '2=>4=>1=>3=>5'
    one, two, three, four, five = get_nodes()
    one.next = three
    three.next = five
    five.next = two
    two.next = four
    acutal = ll.view(ll.even_odd_merge(one))
    assert expected == acutal

def test_scenario2():
    expected = '2=>4=>1=>3=>5'
    one, two, three, four, five = get_nodes()
    four.next = five
    three.next = four
    two.next = three
    one.next = two
    acutal = ll.view(ll.even_odd_merge(one))
    assert expected == acutal

def test_scenario3():
    expected = '4=>2'
    _, two, _, four, _ = get_nodes()
    four.next = two
    acutal = ll.view(ll.even_odd_merge(four))
    assert expected == acutal
