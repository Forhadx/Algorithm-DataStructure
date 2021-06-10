#include <iostream>
using namespace std;

#define MAX 1000

class Stack
{
private:
    int top;
    int S[MAX];

public:
    Stack()
    {
        top = -1;
    }
    void push(int x);
    int pop();
    int peek(int pos);
    int stackTop();
    int isFull();
    int isEmpty();
    void Display();
};

void Stack::push(int x)
{
    if (isFull())
    {
        cout << "Stack overflow. ";
    }
    else
    {
        S[++top] = x;
    }
}

int Stack::pop()
{
    if (isEmpty())
    {
        cout << "Stack Underflow. ";
        return 0;
    }
    else
    {
        int x = S[top--];
        return x;
    }
}

int Stack::peek(int pos)
{
    if (top - pos + 1 < 0)
    {
        cout << "Invalid Index" << endl;
        return -1;
    }
    else
    {
        return S[top - pos + 1];
    }
}

int Stack::stackTop()
{
    if (isEmpty())
        return -1;
    return S[top];
}

int Stack::isEmpty()
{
    return top == -1;
}

int Stack::isFull()
{
    return top == MAX - 1;
}

void Stack::Display()
{
    cout << "Stack values: ";
    for (int i = top; i >= 0; i--)
        cout << S[i] << " ";
    cout << endl;
}

bool isBalanced(string str)
{
    Stack stack;
    for(int i=0; i<str.length(); i++){
        if(str[i]=='('){
            stack.push(str[i]);
        }
        else if(str[i]==')'){
            if(stack.isEmpty())
                return false;
            stack.pop();
        }
    }
    if(stack.isEmpty())
        return true;
    else return false;
}

int main()
{
    string str= "((a+b)*(c-d))";
    //cin >> str;

    cout<<"res: "<<isBalanced(str);

    return 0;
}

/*      output
//----------------------------------------
    res: 1
*/