#!/usr/bin/python
import json
import paramiko

def store_file_details():
	filename = "file.json"
	with open(filename, 'r') as f_obj:
		data = json.load(f_obj)
	f_obj.close()
	return data
	
	
def load_file_details():
	file_data = store_file_details()
	
	host = file_data['router']['host']
	username = file_data['router']['user']
	password = file_data['router']['password']
	dest = file_data['router']['dest']
	data = host, username, password, dest
	
	return data

def open_connection():
	"""Invokes paramiko to open an ssh connection
	to the info that was provided in the JSON file
	"""
	data = load_file_details()
	
	port = 22
    
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(
		paramiko.AutoAddPolicy())
	ssh.connect(data[0], username=data[1], password=data[2])
	sftp = ssh.open_sftp()

open_connection()
