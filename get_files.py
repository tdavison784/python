#!/usr/bin/python
import paramiko
import json
import glob

class FileMover():
    """Class to move files from server to server
    This module can move files from windows to linux,
    Windows to Windows,
    And Linux to Windows."""

    def __init__(self, filename):
        """Init all arguments"""
        self.filename = filename
        self.sftp = None
        self.sftp_open = False


    def store_file_data(self):
        """Stores all file data into a variable
        Data is loaded in JSON"""

        with open(self.filename, 'r') as f_obj:
            self.data = json.load(f_obj)
        f_obj.close()


    def load_file_data(self):
        """Loads data """
        self.hostname = self.data['router']['host']
        self.user = self.data['router']['username']
        self.passwd = self.data['router']['password']
        self.src = self.data['router']['src']
        self.dest = self.data['router']['dest']
        self.filename = self.data['router']['filename']

        self.conn_details = self.hostname, self.user, self.passwd, self.src, self.dest


    def establish_connection(self):
        """Establish paramiko connection"""
        self.port = 22

        self.transport = paramiko.Transport(self.hostname, self.port)
        self.transport.connect(username=self.user, password=self.passwd)

        if not self.sftp_open:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.sftp_open = True

    def get_files(self):
        """Get files from remote server"""
        self.establish_connection()
        self.sftp.get(self.src+self.filename, self.dest+self.filename)
