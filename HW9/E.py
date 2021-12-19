def unique_occurences(arr):
    dict_count_unique_occurrences = {}

    for element in arr:
        if element not in dict_count_unique_occurrences:
            dict_count_unique_occurrences[element] = 1
        else:
            dict_count_unique_occurrences[element] += 1

    set_count_unique_occurences = set()

    for key in dict_count_unique_occurrences:
        the_count = dict_count_unique_occurrences[key]
        if the_count in set_count_unique_occurences:
            return False
        else:
            set_count_unique_occurences.add(the_count)

    return True
a = [int (i) for i in input().split()]
print(unique_occurences(a))