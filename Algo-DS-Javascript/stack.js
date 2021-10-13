let S = [];
const MAX = 5;
let top = -1;

const isFull = () => {
    if (S.length >= MAX) {
        console.log("Stack is full!");
        return true;
    } else return false;
};

const isEmpty = () => {
    if (top === -1) {
        console.log("Stack is empty!");
        return true;
    } else false;
};

const push = (x) => {
    if (!isFull()) {
        S[++top] = x;
        console.log("push: ", x);
    }
};

const pop = () => {
    if (!isEmpty()) {
        console.log("pop: ", S[top]);
        S.splice(-1);
        --top;
    }
};

const Top = () => {
    if (!isEmpty()) return S[top];
};

push(2);
push(5);
push(3);
push(5);
push(2);
push(3); // Stack is full!

console.log(S); // [ 2, 5, 3, 5, 2 ]

console.log(Top()); // 2

pop();
pop();
pop();
pop();
pop();
pop(); // Stack is empty!
pop(); // Stack is empty!

console.log(S); // []

console.log("------------------------------------------");

// build in Array fn

let stackArr = [];

stackArr.push(5);
stackArr.push(3);
stackArr.push(9);

console.log(stackArr); // [ 5, 3, 9 ]

stackArr.pop();

console.log(stackArr); // [ 5, 3 ]

let x = stackArr[stackArr.length - 1];
console.log("top: ", x); // 3
