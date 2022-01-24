
import subprocess

def get_output(cmd):

	sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	return (sp.stdout.read()).decode("utf-8")