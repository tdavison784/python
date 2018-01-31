#!/usr/bin/python
import json
import paramiko
import os
from stat import S_ISDIR
import glob


def store_file_data():
    """Function to store file data
    that gets loaded from a JSON file
    """
    filename = "file.json"
    with open(filename, 'r') as f_obj:
        data =  json.load(f_obj)
    f_obj.close()
    return data

def load_file_data():
    """Function to imports file data from
    store_file_data function and stores the needed
    key information
    """
    conn_data = store_file_data()

    hostname = conn_data['router']['host']
    username = conn_data['router']['username']
    password = conn_data['router']['password']
    src = conn_data['router']['src']
    dest = conn_data['router']['dest']

    data = hostname, username, password, src, dest
    return data

def open_connection():
    """Function that loads all data from load_file_data module
    and opens a SFTP connection to destination server that is
    specified in the hostname variable.
    """
    sftp_conn_data = load_file_data()

    ## Port will always be 22
    port = 22

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())
    ssh.connect(sftp_conn_data[0], username=sftp_conn_data[1], password=sftp_conn_data[2])
    sftp = ssh.open_sftp()

    connection = sftp
    return connection

def transfer_files(remote_dir, local_dir):
    establish_conn = open_connection()
    sftp_conn_data = load_file_data()
    dir_items = establish_conn.listdir()

    for item in dir_items:
        remote_dir =  sftp_conn_data[4] + '/' + item.filename
        local_dir = os.path.join(sftp_conn_data[3], item.filename)
        if S_ISDIR(item.st_mode):
            transfer_files(remote_dir, local_dir)
        else:
            establish_conn.get(remote_dir, local_dir)
