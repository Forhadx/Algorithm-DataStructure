class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    eat() {
        console.log(this.name, "is Eating!!");
    }
}

class Cricketer extends Person {
    constructor(name, age, type, country) {
        super(name, age); // send the name , age data to Person
        this.name = name;
        this.age = age;
        this.type = type;
        this.country = country;
    }

    play() {
        console.log(this.name, "is playing");
    }
}

const sakib = new Cricketer("sakib", 23, "bowler", "bd");

sakib.eat();
sakib.play();
