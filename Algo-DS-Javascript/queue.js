let Q = [];
const MAX = 5;
let front = 0;
let back = -1;

const isEmpty = () => {
    if (back === -1) {
        console.log("Queue is empty!");
        return true;
    } else false;
};

const isFull = () => {
    if (Q.length >= MAX) {
        console.log("Queue is full!");
        return true;
    } else false;
};

const enqueue = (x) => {
    if (!isFull()) {
        Q[++back] = x;
    }
};

const dequeue = () => {
    if (!isEmpty()) {
        for (let i = 0; i < Q.length - 1; i++) {
            Q[i] = Q[i + 1];
        }
        Q.splice(-1);
        --back;
    }
};

const frontQ = () => {
    //if()
};

enqueue(3);
enqueue(4);
enqueue(5);
enqueue(6);
enqueue(7);

console.log(Q); // [ 3, 4, 5, 6, 7 ]
console.log("front: ", Q[front]); // 7
console.log("back: ", Q[back]); // 3

dequeue();

console.log("after dequeue: ", Q); // [ 4, 5, 6, 7 ]
console.log("front: ", Q[front]);
console.log("back: ", Q[back]);

console.log("------------------------------------------");

// build in Array fn

let stackArr = [];

stackArr.unshift(5);
stackArr.unshift(8);
stackArr.unshift(9);
stackArr.unshift(7);

console.log(stackArr); // [7, 9, 8, 5 ]

console.log("front: ", stackArr[0]); // 7
console.log("back: ", stackArr[stackArr.length - 1]); // 5

stackArr.shift();
console.log(stackArr); //[ 9, 8, 5 ]
