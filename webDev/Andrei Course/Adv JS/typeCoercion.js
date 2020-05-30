// Type Coercion //
// the language converting a certain data type to another type
// all languages have type coercion but there are different levels
// JS is dynamically typed so it has a high level of type coercion
// type coercion usually happens when we use double == sign

// JS coerces 1 to true and 0 to false
// so we almost always want to use triple ===
// not really important when it comes to practical use

// object.is( , ); //

if(+0 === -0){console.log("hello world")}
if(Object.is(+0,-0)){console.log("wrong answer motherfucker")};

