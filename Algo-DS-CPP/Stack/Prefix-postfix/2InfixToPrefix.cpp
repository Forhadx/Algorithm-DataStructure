/*
    stack< data_type >  var_name;
    push();
    pop();
    top();
    empty();
    size()
*/

#include <bits/stdc++.h>
using namespace std;

int pre(char x)
{

    if(x=='+' || x=='-')
        return 1;
    else if(x =='*' || x == '/')
            return 2;
    return 0;
}

int isOperand(char x)
{
    if(x == '+' || x=='-' || x=='*' || x=='/')
        return 0;
    else
        return 1;
}

char *InfixToPostfix (char *infix)
{
stack<char> stack;

    int i=0, j=0;
    char *postfix;
    int len = strlen(infix);
    postfix = (char *)malloc((len+2)*sizeof(char));
    while(infix[i]!='\0')
    {
        if(isOperand(infix[i]))
            postfix[j++]=infix[i++];
        else{
            if(pre(infix[i]) > pre(stack.top()))
               stack.push(infix[i++]);
            else
                postfix[j++] = stack.pop();
        }
    }
    while(stack.top()!=NULL)
        postfix[j++]=stack.pop();
    postfix[j]='\0';
    return postfix;
}


int main()
{
    char *infix = "a+b*c-d/e";


    char *postfix = InfixToPostfix(infix);
    printf("%s", postfix);
}

/*
    input:  {([a+b]*[c-d])/c}
    output: String is balance.

    input:  {(a+b) [c}
    output: String is not balance!

*/
