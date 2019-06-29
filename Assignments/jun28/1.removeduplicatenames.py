
names = ["Alex","John","Mary","Steve","John", "Steve"]

def remove_duplicates(array):
    dups_removed = []
    for name in array:
        if name not in dups_removed:
            dups_removed.append(name)
    print(dups_removed)

remove_duplicates(names)