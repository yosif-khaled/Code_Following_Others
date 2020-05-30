// function sayHello() {
// 	console.log("Hello");
// }

// sayHello();

// var sayBye = function () {
// 	console.log("Bye");
// }

// sayBye();


// function sing (song) {
// 	console.log(song);
// }

// var song = "Hello Mate"

// sing(song);

// function multiply(a, b) {
// 	if (a > b)
// 		{return a * b;}
// 	else {return "a is less than b";}
// }

// console.log(multiply(50, 10));

var checkDriverAge2 = function (age) {

	if (Number(age) < 18) {
		console.log("Sorry, you are too yound to drive this car. Powering off");
	} else if (Number(age) > 18) {
		console.log("Powering On. Enjoy the ride!");
	} else if (Number(age) === 18) {
		console.log("Congratulations on your first year of driving. Enjoy the ride!");
	}
}


function checkDriverAge(age) {

	if (Number(age) < 18) {
		console.log("Sorry, you are too yound to drive this car. Powering off");
	} else if (Number(age) > 18) {
		console.log("Powering On. Enjoy the ride!");
	} else if (Number(age) === 18) {
		console.log("Congratulations on your first year of driving. Enjoy the ride!");
	}
}

var age = prompt("Enter You Age: ");

checkDriverAge(age);

checkDriverAge2(age);

