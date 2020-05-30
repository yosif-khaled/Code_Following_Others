// Exercise Build Facebook

 var database = [
	{
		userName: "Yosif",
		password: "secret"
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
	}
 ];
 
 var userNamePrompt = prompt("What is your user name?");
 
 var passwordPrompt = prompt("what is your password?");
 
 function signIn(user, password) {
	 if (user === database[0].userName && password === database[0].password){
		 console.log(newsFeed);
	 } else { console.error("wrong password or user name");
 };
 };
 
signIn(userNamePrompt, passwordPrompt);
