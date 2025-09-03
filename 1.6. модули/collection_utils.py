
def unique_elements(lst):
    z = []
    for i in lst:
        if i not in z:
            z.append(i)
    print(z)

def count_occurrences(lst):
    lst_dict = dict.fromkeys(lst, "elem")
    count = 0
    for i in lst:
        count +=1
    print(f"количество элементов = {count}")
    return lst_dict

from random import choice
z = choice(["😀", "😁", "😇", "🙃", "🤣"])