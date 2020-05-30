var button = document.getElementById("enter");
var input = document.getElementById("userinput");
var ul = document.querySelector("ul");
var li = document.getElementsByTagName("li");
var btn = document.createElement("BUTTON");
var delbtn = document.querySelectorAll(".delete");



function inputLength() {
	return input.value.length;
}

function createListElement() {
	var li = document.createElement("li");

	li.appendChild(document.createTextNode(input.value));
	li.appendChild(btn);
	btn.innerHTML = "Delete";
	btn.classList.add("delete");
	ul.appendChild(li);
	input.value = "";
	delbtn.onClick = removeParent;

}

function addListAfterClick() {
	if (inputLength() > 0) {
		createListElement();
	}
}

function addListAfterKeypress(event) {
	if (inputLength() > 0 && event.keyCode === 13) {
		createListElement();
	}
}

function toggleDone(event) {
	if(event.target.tagName === "LI"){
		event.target.classList.toggle("done");
	}
}

function removeParent(event){
	if(event.parentNode.tagName === "LI"){
		event.removeParentNode();	}
}

for(var i = 0; i < delbtn.length; i++){
 	console.log("what the semen");
 }



ul.addEventListener("click", toggleDone);

button.addEventListener("click", addListAfterClick);

input.addEventListener("keypress", addListAfterKeypress);

