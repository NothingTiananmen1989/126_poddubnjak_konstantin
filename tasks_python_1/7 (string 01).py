st, subst = input(), input()
def search_substr(st, substr):
    if subst in st:
        return "Есть контакт!"
    else:
        return "Мимо!"
print(search_substr(st, subst))