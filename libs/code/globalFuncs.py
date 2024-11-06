from sys import exit as SYSEXIT

# глобальные
def readFile(file:str):
    with open(file,'r',encoding='utf-8') as f: return [line.strip() for line in f]

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
