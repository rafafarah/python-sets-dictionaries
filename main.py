def test_extend_list():
    user_data_science = [15, 23, 43, 56]
    user_machine_learning = [13, 23, 56, 42]

    watched = []
    watched = user_data_science.copy()
    watched.extend(user_machine_learning)
    # final list has duplicated elements
    print(watched)

def test_set():
    user_data_science = {15, 23, 43, 56}
    user_machine_learning = {13, 23, 56, 42}
    # a set has no duplicated element
    # set has no index access/no order
    watched_union = user_machine_learning | user_data_science
    watched_intesec = user_machine_learning & user_data_science
    watched_diff = user_machine_learning - user_data_science
    watched_exclusive = user_machine_learning ^ user_data_science
    print(watched_exclusive)
    for user in watched_exclusive:
        print(user)

def test_modifying_set():
    user = {1, 5, 76, 34, 52, 13, 17}
    print(len(user))
    user.add(765)
    print(len(user))

    # frozenset is a not mutable set
    frozen = frozenset(user)
    print(frozen)

def test_dictionary():
    # creating dictionary from constructor, not usual
    # dic = dict(jorge = 1, doge = 2, name = 2, come = 1,)
    dic = {
        "jorge" : 1,
        "doge" : 2,
        "name" : 2,
        "come" : 1,
    }

    # adding to dic
    dic["jefferson"] = 1
    print(dic)
    # removing from dic
    del dic["jefferson"]
    print(dic)

    print(dic["doge"])
    # set allows to define a default value if key isn't present
    print(dic.get("asfd", 0))

def test_iterate_dict():
    dic = {
        "jorge" : 1,
        "doge" : 2,
        "name" : 2,
        "come" : 1,
    }
    # print dict keys
    for elem in dic:
        print(elem)
    print()
    # print dict values
    for elem in dic.values():
        print(elem)
    print()
    # print dict couple
    for elem in dic.items():
        print(elem)
    print()
    # print dict couple anpacked
    for key, value in dic.items():
        print(key, ":", value)


if __name__ == "__main__":
    test_iterate_dict()
