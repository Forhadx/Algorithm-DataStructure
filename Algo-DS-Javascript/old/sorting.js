// swap

let a = 4,
    b = 7;
[a, b] = [b, a];
console.log(a);
console.log(b);

//sorting fn
let num = [1, 4, 2, 6, 4];
num.sort((a, b) => a - b);
console.log(num);

let arr = [4, 2, 5, 3];
console.log(arr);
[arr[0], arr[1]] = [arr[1], arr[0]];
console.log(arr);
