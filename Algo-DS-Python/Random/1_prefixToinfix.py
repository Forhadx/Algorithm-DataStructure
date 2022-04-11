# prefix to infix

def prefixToInfix(s):
    stack = []
    operators = ['+', '-', '*', '/', '^']
    s = s[::-1]

    for i in s:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            temp = '(' + a + i + b + ')'
            stack.append(temp)

        else:
            stack.append(i)
    
    return stack[0]
 
# Driver code
if __name__=="__main__":
    s = "*-A/BC-/AKL"
    print(prefixToInfix(s))   # ((A-(B/C))*((A/K)-L))
     