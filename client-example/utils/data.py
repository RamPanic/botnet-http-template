
import json
import uuid
import socket
import getpass
import platform
import requests

def get_uuid():

    return str(uuid.getnode())

def get_hostname():

    return socket.gethostname()

def get_username():

    return getpass.getuser()

def get_platform():

    return platform.system()

def get_local_ip():

    return socket.gethostbyname(get_hostname())

def get_remote_ip():

    return (json.loads(requests.get("https://api.ipify.org/?format=json").text))["ip"]