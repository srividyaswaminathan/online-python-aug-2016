1. Create server.py 
	+ Routes
		+ '/' (GET) => Registration Page
		+ '/wall' (GET) => Displays  the messages
		+ '/login' (POST) => Validate email/password, log them in 
		+ '/register' (POST) => Validate user, store their info, and log them in  
		+ '/message' (POST) => Push a message into the db, display it on wall
		+ '/comment' (POST) => Push a comment into the db, display it on the wall
2. Create a database and db connection.py
3. Templates
	+ Login 
	+ Registration 
