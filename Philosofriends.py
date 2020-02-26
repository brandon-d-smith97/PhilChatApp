import socket
import threading
import sys
import re
import random

#TCP Server Code

serverPort = 9065 #arbitrary port number
host = socket.gethostname()

class Server:
	'''
	Attributes:
	connections - array where active connections are stored 
	connected_ids - list of unique id's
	Methods:
	bind() - binds to port to allows server to listen
	listen() - allows up to two connections 
	socket() - specifies connection to TCP and IPv4
	check_for_exit() - if the clients send 'exit', disconect them from the server
	assign_client_id() - assign random number and name to client
	handler()
	run()
	'''
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 and TCP
	
	global connected_ids
	connections = [] #what clients are connected with the server

	def __init__(self):  #Server constructor
		self.s.bind(('', serverPort)) #bind to port and listen to server
		self.s.listen(2) #allow up to two connections

		self.connected_ids = {}

	def handler(self, c,a):
		global connections
		while True:
			data = c.recv(1024) # server takes in bits
			#self.show_ids(data)
			self.check_for_exit(data, c) #did they type exit?
			for connection in self.connections: # for each connection
				connection.send(bytes(data)) #send the data recieved by the server
			if not data: #close when no more data
				print(str(self.connected_ids.get('str(c)')), "disconected")
				self.connections.remove(c)
				c.close()
				break

	def run(self):
		while True:
			c, a = self.s.accept() #c is connection, a is address
			self.assign_client_id(c)
			cThread  = threading.Thread(target=self.handler, args=(c,a))
			cThread.daemon = True #is a daeomon thread?
			cThread.start() #start thread
			self.connections.append(c) 
			print(str(self.connected_ids.get('str(c)')), "conected")

	
	def check_for_exit(self, data, c):
		data = data.decode('utf-8') #bytes to letters
		searchResult = re.search('.exit', data, re.M|re.I) #match exit alone 
		if searchResult: #if matched
			c.close() #close connection
			self.connections.remove(c)
			print(str(self.connected_ids.get('str(c)')) + ' Exited the Program')
			
		else:
			pass # or just move on

	def assign_client_id(self, c):
		id = random.randint(0,99)
		self.connected_ids['str(c)'] = id
	
	def show_ids(self,data):
		data = data.decode('utf-8') #bytes to letters
		searchResult = re.search('user', data, re.M|re.I) #match exit alone 
		if searchResult: #if matched
			for i in self.connections:
				print(self.connections)


class Client:
	"""
	Attributes:
	id
	username
	Methods: 
	socket() - specifies connection to TCP and IPv4
	set_name() - client sets username 
	send_message() - allows message sending

	""" 



	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket with ipv4 and TCp
	
	def __init__(self, address):
		self.s.connect((host, serverPort)) #Connect Client to server

		id = 0
		username = ''
		self.set_name()

		iThread = threading.Thread(target=self.send_message) 
		iThread.daemon = True
		iThread.start()

		while True:
			data=self.s.recv(1024)
			if not data:
				break
			print(str(data, 'utf-8'))

	def send_message(self): #method for clients
		while True:
			self.s.send(bytes(self.username + ' : ' + input(""), 'utf-8')) #Sends user input in byte format
		

	def set_name(self):
		print('Type \'exit\' at any time leave the server')
		self.username =  input("What would you like your username to be?")
		
#Testing
def main():
	
	if (len(sys.argv) > 1):
			client = Client(sys.argv[1])
			print(server.connected_ids)
	else:
		server = Server()
		server.run()

	


main()
'''
 Instructions: 
 Requirements: Python
 Download roject.py
 Go into file path of where the .py file is located using command line
 Type in the command line : python project.py
 -this makes a server on your computer. 
 if you add another arguement in the command line of the host name you wish to connect to, you create a client.
'''