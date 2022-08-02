user_input = int(input())
lst = []
number = 55

while user_input != number:
    lst.append(user_input)
    user_input = int(input())
print(len(lst), sum(lst), round(sum(lst) / len(lst)), sep="\n")
