// Loops

var todos  = [
	"clean room",
	"brush teeth",
	"exercise",
	"study JS",
	"eat healthy"
];

var done = [];
var todosLength = todos.length
for(var i = 0; i < todosLength; i++) {
	console.log(todos[i], i);
};

todos.forEach(function(todos, i) {console.log(todos, i);});


var counterOne = 10;

while (counterOne > 10){
	console.log(counterOne);
	counterOne--;
};

var counterTwo = 10

do {
	console.log(counterTwo);
	counterTwo--;
} while (counterTwo > 10);
