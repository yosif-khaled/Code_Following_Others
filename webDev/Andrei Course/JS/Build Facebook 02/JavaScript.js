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
 
 function signIn(user, password) {
	 
	 for (var i = 0; i < database.length; i++){
		if (database[i].userName === user && database[i].password === password){
		console.log(newsFeed);
		} else { console.error("wrong password or user name");};
	 };
	 

 };
 
 signIn(userNamePrompt, passwordPrompt);

