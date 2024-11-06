from sys import exit as SYSEXIT

# поиск
def inclStr(list:list,txt:str): # есть ли строка среди элементов списка
    for item in list:
        if item == txt: return True
    return False

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
