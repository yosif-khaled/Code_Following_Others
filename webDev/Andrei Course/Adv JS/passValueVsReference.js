// passed by reference vs passed by value
// easy but wierd

// passing by value
var a = 5;
var b = 10;


// passing by reference
var object1 = {
};

var object2 = object1;

object2.value = "change";

var c = [1,2,3,4,5];
var d = c;
d.push(123456789);

// shallow cloning //

let obj = {a:"a", b:"b", c:{deep: 'try and copy me'}};
let obj2 = obj
// the first curly brackets are simply the object to cop to
// then the source object
let clone = Object.assign({}, obj);
let clone2 = {...obj};
obj.c = 5;
console.log(obj);
console.log(obj2);
console.log(clone);
console.log(clone2);

// deep cloning //
let superClone = JSON.parse(JSON.stringify(obj))
console.log(superClone);