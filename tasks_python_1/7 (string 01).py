st, subst = input(), input()
def search_substr(subst, st):
    if subst in st:
        return "Есть контакт!"
    else:
        return "Мимо!"
print(search_substr(subst, st))