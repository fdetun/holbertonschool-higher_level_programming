def search_replace(nl, search, replace):
    my_list = nl[:]
    for i in my_list:
        if i == 2:
            a = my_list.index(i)
            my_list.remove(i)
            my_list.insert(a, 98)
    return (my_list)
