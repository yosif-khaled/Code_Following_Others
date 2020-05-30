//advanced arrays

const array = [1, 2, 10, 10];

const double = []
const newArray = array.forEach((num) => {
	double.push(num * 2);
});

console.log(newArray);

// map filter reduce

// Map //
const mapArray = array.map((num) => {
	return num = 2;
});

//cleaner way
// const mapArray = array.map(num => num + 2);

console.log(mapArray);

// Filter //
const filterArray = array.filter(num => {
	return num > 5;
}); // will return an array

console.log(filterArray);

// Reduce //
const reduceArray = array.reduce((accumelator, num) => {
	return accumelator + num;
}, 0);

console.log(reduceArray);