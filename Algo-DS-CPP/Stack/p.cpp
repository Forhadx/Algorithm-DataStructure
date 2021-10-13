#include <bits/stdc++.h>
using namespace std;

int isBalance(string str)
{
    stack<char> stack;
    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] == '(' || str[i] == '{' || str[i] == '[')
        {
            stack.push(str[i]);
        }
        if (str[i] == ')' || str[i] == '}' || str[i] == ']')
        {
            if (stack.empty())
                return -1;
            if (stack.top() == '(' && str[i] == ')' ||
                stack.top() == '{' && str[i] == '}' ||
                stack.top() == '[' && str[i] == ']')
            {
                stack.pop();
            }
        }
    }

    if(stack.empty()) return 1;
    else return -1;
}

int main()
{
    string str = "{([a+b]*[c-d])/c}";
    int x = isBalance(str);
    if(x == 1) cout<<"String is balance.";
    else cout<<"String is not balance!";
}