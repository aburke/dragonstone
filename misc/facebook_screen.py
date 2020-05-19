# Input:
# C1: bob@yahoo.com, bob@gmail.com
# C2: mary@facebook.com
# C3: bob@gmail.com, bob_1@hotmail.com
# C4: bob_1@hotmail.com, bob@abc.com, bob@bcd.com
# C5: mary@facebook.com
# C6: mark@gmail.com

# ########
# C7: bob@asf.com, bob@abc.com  
# C8: bob@asdff.com, bob@bcd.com 
# c9: bob@asf.com

# Output: (C1, C3, C4), (C2, C5), (C6)


from collections import defaultdict

def group_stuff(node_dict: dict):
    groups = defaultdict(set)
    for k, v in node_dict.items():
        for i in v:
            groups[i].add(k)

    unmerged_groups = [x for x in groups.values()]
    i = 1
    j = 0
    while i < len(unmerged_groups):
        if unmerged_groups[j].intersection(unmerged_groups[i]):
            unmerged_groups[j] = unmerged_groups[j].union(unmerged_groups[i])
            del unmerged_groups[i]
        else:
            i += 1
        if i >= len(unmerged_groups):
            j += 1
            i = j + 1 

    return unmerged_groups


if __name__ == "__main__":
    ip = {
        'c1': ['bob@yahoo.com', 'bob@gmail.com'],
        'c2': ['mary@facebook.com'],
        'c3': ['bob@gmail.com', 'bob_1@hotmail.com'],
        'c4': ['bob_1@hotmail.com', 'bob@abc.com', 'bob@bcd.com'],
        'c5': ['mary@facebook.com'],
        'c6': ['mark@gmail.com']
    }

    print(group_stuff(ip))
