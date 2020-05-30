// reference type
var object1 = { value: 10 };
var object2 = object1;
var object3 = { value: 10 };

// context vs scope
// basically scope is governed by curly brackets
// context is all about "this."

// instantiation
class Player {
	constructor(name, type) {
		this.name = name;
		this.type = type;
	}
	
	introduce() {
		console.log(`hi I am ${this.name}, I am ${this.type}`);
	}
}

//adding on top of whatever player has
class Wizard extends Player {
	constructor(name, type) {
		// basically to give you access to these attributes
		super(name, type); // always at the beginning
		console.log('Wizard', this);
	}
	play(){
		console.log(`I am a ${this.type}`);
	}
}

const wizard1 = new Wizard("shelly", "healer");
const wizard2 = new Wizard("shawn", "dark magic");