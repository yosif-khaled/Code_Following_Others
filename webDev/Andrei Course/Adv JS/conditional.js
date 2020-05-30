// function isUserValid(bool) {
// 	return bool;
// }

// var answer = isUserValid(true) ? "you may enter" : "access denied";

// var automatedAnswer = "your account # is " + (isUserValid(false) ? "1234" : "available");

// //var automatedAnswer = `your account # is ${(isUserValid(false) ? "1234" : "available")}`;

// function condition(){

// 	if(isUserValid){
// 		return "you may enter";
// 	} else {return "access denied";
// 	}

// }

// var answer3 = condition();

function moveCommand(direction){
	var whatHappens;
	switch(direction) {
		case "forward":
			whatHappens = "you encounter a monster";
			break;
		case "back":
			whatHappens = "you arrived home";
			break;
		case "right":
			whatHappens = "you found a river";
			break;
		case "left":
			whatHappens = "you run into a troll";
			break;
		default:
			whatHappens = "please bitch enter a vlid direction"
			break;
	}

	return whatHappens;
}