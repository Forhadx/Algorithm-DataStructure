// factorial

const factorial = (n) => {
    if (n === 0) {
        return 1;
    }
    return n * factorial(n - 1);
};

let fact = factorial(4); // 24

console.log(fact);
console.log("-----------------------------------------");

//fibonacci
const fibonacci = (n) => {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
};

let fib = fibonacci(4); // 3

console.log(fib);
console.log("-----------------------------------------");

const showFibSeris = (n) => {
    let prev = 0;
    let curnt = 1;
    let t = 0;
    while (n--) {
        console.log(curnt);
        t = curnt;
        curnt += prev;
        prev = t;
    }
};

showFibSeris(6); // 1 1 2 3 5 8
console.log("-----------------------------------------");

// prime number
const isPrime = (n) => {
    if (n <= 1) return false;

    for (let i = 2; i < n; i++) {
        if (n % i === 0) return false;
        else return true;
    }
};

console.log(isPrime(11));
