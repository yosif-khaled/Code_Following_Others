// //Examine the document object //
// //console.dir(document);

// console.log(document.domain);
// console.log(document.url);
// console.log(document.title);
// //document.title = 123;
// console.log(document.doctype);
// console.log(document.head);
// console.log(document.body);
// console.log(document.all);
// console.log(document.all[10]);
// //document.all[10].textContent = "Hello";
// console.log(document.forms[0]);
// console.log(document.links);
// console.log(document.images);

// Selectors to query the dom
// GETELEMENTBYID

// var headerTitle = document.getElementById("header-title");
// var header = document.getElementById("main-header");
//console.log(headerTitle);

// one of them pays attention to styling
// headerTitle.textContent = "Hello";
// headerTitle.innerText = "GoodBye"; //pays attention to style

//headerTitle.innerHTML = "<h3>Hello</h3>"; //adds html element inside another element

// header.style.borderBottom = "solid 3px #000";



// GETELEMENTSBYCLASSNAME //
// var items = document.getElementsByClassName("list-group-item");
// console.log(items);
// console.log(items[1]);
// items[1].textContent = "Hello 2";
// items[1].style.fontWeight = "bold";
// items[1].style.backgroundColor = "yellow";

// // items.style.backgroundColor = "#f4f4f4";
// //well you can't use the previous commend unles you loop through the whole items because because basically it is an array of items

// for (var i = 0; i < items.length; i++) {
// 	items[i].style.backgroundColor = "#f4f4f4";
// }

// GETELEMENTSBYTAGNAME //

// var li = document.getElementsByTagName("li");
// console.log(li);
// console.log(li[1]);
// li[1].textContent = "Hello 2";
// li[1].style.fontWeight = "bold";
// li[1].style.backgroundColor = "yellow";

// // items.style.backgroundColor = "#f4f4f4";
// //well you can't use the previous commend unles you loop through the whole items because because basically it is an array of items

// for (var i = 0; i < li.length; i++) {
//  	li[i].style.backgroundColor = "#f4f4f4";
// }

// QUERYSELECTOR // only grabs the first one

// var header = document.querySelector("#main-header");
// header.style.borderBottom = "solid 4px #ccc";

// var input = document.querySelector("input");
// input.value = "Hello World"

// var submit = document.querySelector("input[type='submit']");
// submit.value = "Send";

// var item = document.querySelector(".list-group-item");
// item.style.color = "red";

// var lastItem = document.querySelector(".list-group-item:last-child");
// lastItem.style.color = "blue"

// var secondItem = document.querySelector(".list-group-item:nth-child(2)");
// secondItem.style.color = "orange";

// QUERYSELECTORALL //

// var titles = document.querySelectorAll(".title");
// console.log(titles);

// var odd = document.querySelectorAll("li:nth-child(odd)");

// var even = document.querySelectorAll("li:nth-child(even)");

// for (var i = 0; i < odd.length; i++){
// 	odd[i].style.backgroundColor = "#f4f4f4";
// 	even[i].style.backgroundColor = "#ccc";
// }

// TRAVERSING THE DOM //

// var itemList = document.querySelector("#items");
// parentNode
// console.log(itemList.parentNode);
// itemList.parentNode.style.backgroundColor = "#f4f4f4";
// console.log(itemList.parentNode.parentNode);

// parentElement
// console.log(itemList.parentElement);
// itemList.parentElement.style.backgroundColor = "#f4f4f4";
// console.log(itemList.parentElement.parentElement);

// // childNodes
// console.log(itemList.childNodes);

// // children
// console.log(itemList.children);
// itemList.children[1].style.backgroundColor = "yellow";

// // firstChild
// console.log(itemList.firstChild);

// // firstElementChild
// console.log(itemList.firstElementChild);
// itemList.firstElementChild.textContent = "Hello 1";

// // lastChild
// // lastElementChild

// // SIBLINGS //

// // nextSibling
// console.log(itemList.nextSibling);

// // nextElementSibling
// console.log(itemList.nextElementSibling); // doesn't actually have a next sibling

// // previousSibling
// console.log(itemList.previousSibling);
// // previousElementSibling
// console.log(itemList.previousElementSibling);
// itemList.previousElementSibling.style.color = "green";

// createElement

// create a div
// var newDiv = document.createElement("div");

// // adding a class
// newDiv.className = "Hello"

// // adding a new id
// newDiv.id = "hello1"

// // adding another attr
// newDiv.setAttribute('title', 'hello div');

// // creating a new text node
// var newDivText = document.createTextNode("Hello World");

// // add text to div
// newDiv.appendChild(newDivText);

// var container = document.querySelector('header .container');
// var h1 = document.querySelector('header h1');

// console.log(newDiv);

// newDiv.style.fontSize = '30px';

// container.insertBefore(newDiv, h1);

// EVENTS //

// you can create them in the html document ...
// onclick = "function in js file"
// but 
// this is not advised

// ADDEVENTLISTENER ... whch is the advised way

// var button = document.getElementById("button").addEventListener('click', buttonClick);

// function buttonClick(event){
	//console.log('button clicked');
	// document.getElementById("header-title").textContent = "changed";
	// document.querySelector("#main").style.backgroundColor = "#f4f4";
	//console.log(event); // prints the actions that you can get
	// console.log(event.target);
	// console.log(event.target.id);
	// console.log(event.target.className);
	// console.log(event.target.classList); //gives an array of the classes

	// var output = document.getElementById("output");
	// output.innerHTML = `<h3>${event.target.id}</h3>`;

	// console.log(event.type); // whatever type of event that it is
	// console.log(event.clientX); //gives the position of thte action on the x axis
	// console.log(event.clientY); // guess what
	// console.log(event.offsetX); // gives the actual position from the actual element that we are inside of and we can do y too
	//we can check if we are holding another key
	// you can use the following event.*key (basically alt, ctrl & shift) to check whether it is true or false and add different functionality based on that by using if statement of course
// 	console.log(event.altKey);
// 	console.log(event.ctrlKey);
// 	console.log(event.shiftKey);
// }

// var button = document.getElementById("button");
// var box = document.getElementById("box");

// button.addEventListener("click", runEvent);
// button.addEventListener("dblclick", runEvent);
// button.addEventListener("mousedown", runEvent);
// button.addEventListener("mouseup", runEvent);

// box.addEventListener("mouseenter", runEvent); // for parent elements
// box.addEventListener("mouseleave", runEvent); 

// box.addEventListener("mouseover", runEvent); // for inner elements
// box.addEventListener("mouseout", runEvent);

// box.addEventListener('mousemove', runEvent);

// var itemInput = document.querySelector(`input[type="text"]`);
// var form = document.querySelector(`form`);
// var select = document.querySelector(`select`);



// itemInput.addEventListener(`keydown`, runEvent);
// itemInput.addEventListener(`keyup`, runEvent);
// itemInput.addEventListener(`keypress`, runEvent);

// itemInput.addEventListener(`focus`, runEvent);
// itemInput.addEventListener(`blur`, runEvent);

// itemInput.addEventListener(`cut`, runEvent);
// itemInput.addEventListener(`paste`, runEvent);

// itemInput.addEventListener(`input`, runEvent);
// select.addEventListener("change", runEvent);
// select.addEventListener("input", runEvent);
// form.addEventListener('submit', runEvent);

// function runEvent(event){
// 	event.preventDefault();
// 	console.log(`EVENT TYPE: ${event.type}`);
	// console.log(event.target.value);
	// document.getElementById(`output`).innerHTML = `<h3>${event.target.value}</h3>`;

	// output.innerHTML = `<h3>MouseX: ${event.offsetX}</h3> <h3>MouseY: ${event.offsetY}</h3>`;

	// document.body.style.backgroundColor = `rgb(${event.offsetX},${event.offsetY},${event.offsetX-event.offsetY})`
// }

