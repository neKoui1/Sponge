# Stack

Last in First out (LIFO)

Browser's Back button

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
```
Validate Parenteses

```python
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
```

https://leetcode.cn/problems/valid-parentheses/
```python
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        return self.items.pop()
    def push(self, item):
        self.items.append(item)
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]

class Solution(object):


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        index = 0
        flag = True
        while flag and index < len(s):
            x = s[index]
            if x == '(' or x == '[' or x == '{':
                stack.push(x)
            else:
                if x == ')':
                    if stack.isEmpty():
                        return False
                    elif stack.peek() == '(':
                        stack.pop()
                    else:
                        return False
                elif x == ']':
                    if stack.isEmpty():
                        return False
                    elif stack.peek() == '[':
                        stack.pop()
                    else:
                        return False
                elif x == '}':
                    if stack.isEmpty():
                        return False
                    elif stack.peek() == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            index += 1
        if flag and stack.isEmpty():
            return True
        else:
            return False

```
Modified

why no SWITCH...
```python
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        return self.items.pop()
    def push(self, item):
        self.items.append(item)
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        index = 0
        while index < len(s):
            x = s[index]
            if x in '([{':
                stack.push(x)
            else:
                if stack.isEmpty():
                    return False
                if (x == ')' and stack.peek() == '(') or (x == ']' and stack.peek() == '[') or (x == '}' and stack.peek() == '{'):
                    stack.pop()
                else:
                    return False
            index += 1
        if stack.isEmpty():
            return True
        else:
            return False
```

HEX CONVERTER

DEC -> BIN

A *positive* number is a *necessity* in this function

```python
from Stack import Stack

def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base
    resString = ''
    while not remstack.isEmpty():
        resString += digits[remstack.pop()]
    return resString

def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber //= 2
    binString = ''
    while not remstack.isEmpty():
        binString += str(remstack.pop())
    return binString

print(divideBy2(100))

print(baseConverter(100, 2))
print(baseConverter(100, 8))
print(baseConverter(100, 10))
print(baseConverter(100, 16))
```