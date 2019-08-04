# -*- coding: utf-8 -*-
# Leave a comment wherever you see a hashtag in order to explain
# the program’s behavior.  Comments for parsing the requested
# file are left in the program, as that’s tertiary to the basic
# functionality of the program


# 
from socket import * 
import sys # In order to terminate the program

# 
serverSocket = socket(AF_INET, SOCK_STREAM)

# 
serverPort = 6787

# 
serverSocket.bind(("", serverPort))

# 
serverSocket.listen(1)

while True:
	print('The server is ready to receive')

	# 
	connectionSocket, addr = serverSocket.accept()

	# 
	try:
		# 
		message = connectionSocket.recv(1024).decode()
		
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
		
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		
		#
		outputdata = f.read()
		
		# 
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 
 
		# 
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode()) 
		
		# 
		connectionSocket.close()

	except IOError:
			# 
			connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
			connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

			# 
			connectionSocket.close()

#
serverSocket.close()  

#
sys.exit()
