from Stack import Stack

def parChecker(str):
    s = Stack()
    index = 0
    flag = True
    while index < len(str) and flag:
        symbol = str[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if symbol == ')':
                if s.isEmpty():
                    flag = False
                else:
                    s.pop()
            else:
                flag = False
        
        index += 1
    
    if flag and s.isEmpty():
        return True
    else:
        return False

    
print(parChecker('((())))'))
print(parChecker('(((1)))'))
print(parChecker('((()))'))