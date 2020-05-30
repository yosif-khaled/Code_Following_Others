// Exercise Build Facebook

 var database = [
	{
		userName: "Yosif",
		password: "secret"
	},
	{
		userName: "Ingrid",
		password: "secret01"
	},
	{
		userName: "Ingrid",
		password: "secret02"
	}
 ];
 
 var newsFeed = [
	{
		userName: "Bobby",
		timeline: "so tired of all that learning"
	},
	{
		userName: "Sally",
		timeline: "JavaScript is ugly but powerful"
	},
	{
		userName: "Mitch",
		timeline: "JS is not cool"
	}
 ];
 
 var userNamePrompt = prompt("What is your user name?");
 
 var passwordPrompt = prompt("what is your password?");
 
function isUsrNameValid(userName, password) {
    for(i = 0; i < database.length; i++) {
        if(database[i].userName === userName && database[i].password === password) {
        return true;
        }
    return false;
    }
}
 
function signIn(userName, password) {
    if(isUsrNameValid(userName, password)){
    console.log(newsFeed); //don't forget adding parameters of the function
    } else {
    alert("wrong username or password");
    }
}
 
 signIn(userNamePrompt, passwordPrompt);

