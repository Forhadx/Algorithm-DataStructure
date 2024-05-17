let num = [1, 40, 23, 9, 2, 5, 12, 22];

// linear search
const linearSearch = (arr, val) => {
    for (let i = 0; i < arr.length; i++) {
        if (val === arr[i]) return i;
    }
    return -1;
};

let index = linearSearch(num, 9);

index === -1 ? console.log("value not found!") : console.log(index);

console.log("--------------------------");

//binary search
const binarySearch = (arr, val) => {
    let l = 0;
    let h = arr.length - 1;

    while (l <= h) {
        let m = l + Math.floor((h - 1) / 2);
        if (arr[m] === val) return m;

        if (arr[m] < val) l = m + 1;
        else h = m - 1;
    }
    return -1;
};

num.sort((a, b) => a - b);
console.log(num);
index = binarySearch(num, 23);

index === -1 ? console.log("value not found!") : console.log(index);
