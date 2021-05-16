#include <iostream>
using namespace std;

#define MAX 1000

class Stack
{
private:
    int top;

public:
    int S[MAX];
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

int main()
{
    class Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    s.push(50);
    s.push(60);
    s.push(70);

    s.Display();

    cout << "Top value: "<<s.stackTop()<<endl;

    cout << "Value of position 3: " << s.peek(3) << endl;

    cout << "pop: " << s.pop() << endl;

    return 0;
}


/*      output
//----------------------------------------
    Stack values: 70 60 50 40 30 20 10 
    Top value: 70
    Value of position 3: 50
    pop: 70
*/