# prefix to inifx

def postfixToInfix(s):
    stack = []
    operators = ['+', '-', '*', '/', '^']


    for i in s:
        
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            temp = '(' + b + i + a + ')'
            stack.append(temp)

            if len(s)-1 and len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                temp = '(' + b + '*' + a + ')'
                stack.append(temp)

        else:
            stack.append(i)
        
    return stack[0]


# Driver code
if __name__=="__main__":
    # s = "ab*c+"
    s = "ab+cd-"
    print(postfixToInfix(s))   # ABC/-AK/L-*

























# class Solution:
#     def countPoints(self, points, queries):
#         ans = []
#         for q in range(len(queries)):
#             l = 0
#             print(queries[q],'------')
#             for p in range(len(points)):
#                 if (points[p][0] >= abs(queries[q][0]-queries[q][2]) and points[p][0] <= queries[q][0]+queries[q][2]) and (points[p][1] >= abs(queries[q][1]-queries[q][2]) and points[p][1] <= queries[q][1]+queries[q][2]):
#                     print(points[p][0],' ',points[p][1],'=> ',points[p]) 
#                     l = l + 1
#             ans.append(l)
        
#         # print('ans: ',ans)

# s = Solution()


# s.countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]])
