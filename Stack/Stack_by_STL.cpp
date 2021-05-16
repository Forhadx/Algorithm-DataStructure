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

void Display(stack<int> st)
{
    while (!st.empty())
    {
        cout << st.top() << " ";
        st.pop();
    }
}

int main()
{
    stack<int> stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(40);
    stack.push(50);

    cout<<"Stack values: ";
    Display(stack);

    cout << "\nAfter one pop: ";
    stack.pop();
    Display(stack);

    cout<<"\nStack size: "<<stack.size();
    return 0;
}


/*
        output
    --------------------
    Stack values: 50 40 30 20 10
    After one pop: 40 30 20 10 
    Stack size: 4
*/
