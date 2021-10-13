#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

class Stack
{
private:
    Node *top;
public:
    Stack(){
        top = NULL;
    }
    void push(int x);
    int pop();
    int stackTop();
    void Display();
};

void Stack::push(int x)
{
    Node *t = new Node;
    if(t == NULL)
        cout<<"Stack is full"<<endl;
    else{
        t->data = x;
        t->next = top;
        top = t;
    }
}

int Stack::pop()
{   
    int x = -1;
    if(top == NULL)
        cout<<"Stack is Empty"<<endl;
    
    else{
        x = top->data;
        Node *t = top;
        top = top->next;
        delete t;
    }
    return x;
}

int Stack::stackTop()
{
    if(top == NULL)
        cout<<"Stack is Empty"<<endl;
    return top->data;
}

void Stack::Display()
{
    Node *p = top;
    while (p != NULL)
    {
        cout<< p->data <<" ";
        p = p->next;
    }
    cout<<endl;
    
}

int main()
{
    Stack s;

    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    s.push(50);

    cout<<"Stack values: ";
    s.Display();

    cout<<"Top value: "<<s.stackTop()<<endl;

    cout<<"one pop: "<<s.pop()<<endl;

    cout<<"After pop stack values: ";
    s.Display();

    return 0;
}


/*
        output
-------------------------
    Stack values: 50 40 30 20 10 
    Top value: 50
    one pop: 50
    After pop stack values: 40 30 20 10

*/