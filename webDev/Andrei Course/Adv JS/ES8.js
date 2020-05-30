// ECMA SCRIPT version 8

// String Padding //
// .padStart()
// .padEnd()

const fun = (a,b,c,d,) => {
	console.log(a);
}

fun(1,2,3,4,);


// Object.values
// Object.entries
// Object.keys

let obj = {
	username0: 'santa',
	username1: 'rudolf',
	username2: 'mr. grinch'
}

Object.keys(obj).forEach((key, index) => {
	console.lg(key, obj[key]);
})

Object.values(obj).forEach(value => {
	console.log(value);
})

Object.entries(obj).forEach(value => {
	console.log(value);
})

Object.entries(obj).map(value => {
	return value[1] + value[0].replace('username', '');
})

// Async Await