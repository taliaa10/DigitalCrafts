
names = ["Alex","John","Mary","Steve","John", "Steve"]

def remove_duplicates(array):
    dups_removed = []
    for name in array:
        if name not in dups_removed:
            dups_removed.append(name)
    else:
        names = dups_removed
        print(names)

remove_duplicates(names)