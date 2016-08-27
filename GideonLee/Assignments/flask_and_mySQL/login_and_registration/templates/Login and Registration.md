Login and Registration

1. Server.py
	+ Routes
		+ /account (GET) =>  Displays failures to meet login requirements, if 
		  registered, automatically log in. 
		  	+ first_name
		  	+ last_name
		  	+ email
		  	+ password
		  	+ password confirmation
		+ /account/login (POST) => displays on fail, a flash message
			+ email + passsword
		+ /account/newUser (POST) => 
		+ /account/summary (GET) => use sessions to say "Hello ___"
		(How do I create a log out button?)
2. Connections.py 
3. Templates
	+ 'login.html' - Registration/Login Page 
	+ 'summary.html' - Success Page
