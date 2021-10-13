class box {
    constructor(l, w) {
        this.l = l;
        this.w = w;
    }

    sum() {
        return this.l + this.w;
    }
}

let obj2 = new box(12, 10);
console.log(obj2.sum()); //22
