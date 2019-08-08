# -*- coding: utf-8 -*-
# Leave a comment wherever you see a hashtag in order to explain
# the programs behavior.  Comments for parsing the requested
# file are left in the program, as thats tertiary to the basic
# functionality of the program


# Importing socket library
from socket import * 
import sys # In order to terminate the program

#Create a server socket
# AF_INET is used for IPv4 protocol 
# SOCK_STREAM is used for TCP 
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign port number 6789 to the server
serverPort = 6789

# Bind the socket to server address and port number
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

while True:
	print('The server is ready to receive')

	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()

	# To handle any errors (exceptions) that may occur, the code is written in the try catch block, if an exception occurs, the code exits
	try:
		# Receive the request message from the client
		message = connectionSocket.recv(1024).decode()
		
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
		
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		
		# Store the contenet of requested file in a temporary buffer
		outputdata = f.read()
		
		# Send the HTTP response header line to the connection socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode()) 
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
			# Send HTTP response message for file not found
			connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
			connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

			# Close the client connection socket
			connectionSocket.close()

#Close the server socket
serverSocket.close()  

#Terminate the program
sys.exit()