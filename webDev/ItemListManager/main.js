var form = document.getElementById('addForm');
var itemList = document.getElementById('items');
var filter = document.getElementById('filter');

// form submit event
form.addEventListener('submit', addItem);
// delete event
itemList.addEventListener('click', removeItem);
// filter event
filter.addEventListener('keyup', filterItems);

// add item
function addItem(event){
	event.preventDefault();

	// Get input value
	var newItem = document.getElementById('item').value;

	// create new li element
	var li = document.createElement('li');
	
	// add class
	li.className = 'list-group-item';

	// add text node with input value
	li.appendChild(document.createTextNode(newItem));

	// create delete buttoon element
	var deleteBtn = document.createElement('button');

	// adding classes to the button
	deleteBtn.className = 'btn btn-danger btn-sm float-right delete';

	// append text node
	deleteBtn.appendChild(document.createTextNode('X'));

	// append button to li
	li.appendChild(deleteBtn);

	// append li to list
	itemList.appendChild(li);
}

// remove item
function removeItem(event){
	if(event.target.classList.contains('delete')){
		// confirm is like alert but returns a boolean
		if (confirm('Are you sure?')){
			var li = event.target.parentElement;
			itemList.removeChild(li);
		}
	}
}

function filterItems(event){
	// convert text to lowercase
	var text = event.target.value.toLowerCase();
	// Get lis
	var items = itemList.getElementsByTagName('li');
	// convert to array
	console.log(items);
	Array.from(items).forEach(function(item){
		var itemName = item.firstChild.textContent;
		if(itemName.toLowerCase().indexOf(text) != -1){
			item.style.display = 'block';
		} else {
			item.style.display = 'none';
		}
	})
}