def power_set(base):
    p_set = []
    def helper(sub):
        if sub not in p_set:
            p_set.append(sub)
            left_over = [x for x in base if x not in sub]
            for k in left_over:
                helper(sub.union({k}))

    for e in base:
        helper({e})

    p_set.append(set())
    return p_set

def epi_power_set(input_set):
    input_set = list(input_set)

    def helper(tb_select, select_sf):
        if tb_select == len(input_set):
            p_set.append(list(select_sf))
            return

        helper(tb_select + 1, select_sf)
        helper(tb_select + 1, select_sf + [input_set[tb_select]])

    p_set = []
    helper(0, [])
    return p_set          