from stack import *


def is_balance(lis):
    flag = True
    for el in lis:
        if el in '[{(':
            s.push(el)
        elif el in ']})':
            if s.is_empty():
                flag = False
                break
            a = s.pop()
            if a == '(' and el == ')':
                continue
            elif a == '[' and el == ']':
                continue
            elif a == '{' and el == '}':
                continue
            else:
                flag = False
                break
    return flag


if __name__ == '__main__':

    s = Stack()
    lis = input("Введите последовательность: ")
    if is_balance(lis) == True and s.is_empty():
        print("Сбалонсированно")
    else:
        print("Несбалансированно")

