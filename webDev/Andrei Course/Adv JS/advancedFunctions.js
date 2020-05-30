const first = () => {
	const greet = "HI";
	const second = () => {
		alert(greet);
	}
	return second;
}

const newFunc = first();
newFunc();

// Closures

// Currying
const multiply = (a, b) => a + b;
const curriedMultiply = (a) => (b) => a + b;
const multiplyBy5 = curriedMultiply(5);

// basically it is a function inside a function
// up there it is like eachtime I run multiply5
// curried will be called and substitue the value
// of a by 5 which in this function is a constant
// multiplyBy5(x)
// is equal to
// curriedMultiply(5)(x)

// Compose
// the act of putting two functions together to form
// a third function where the output of one function
// is the input of the other

const compose = (f, g) => (a) => f(g(a));
const sum = (num) => num + 1;

compose(sum, sum)(5);