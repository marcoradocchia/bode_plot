import os
import json
import platform
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#LINUX INSTALL REQUIREMENTS COMMANDS
pipInstall = ['sudo', 'apt', 'install', 'python-pip']
tkInstall = ['sudo', 'apt', 'install', 'python3-tk']
installMatplotlib = ['pip', 'install', 'matplotlib']

#detect WF istallation path
def setup():
	if systemType == 'Windows':
		#writes in a config.json the path of the waveforms.exe installation
		if str(input('Make sure your Python installation is added to PATH. Confirm? [Y/n]: ')).lower() != 'y': quit()
		print('Please select WaveForms.exe installation file from your file system.')
		Tk().withdraw()
		while True:
			WFexe = askopenfilename()
			if WFexe == '': quit()
			elif WFexe.endswith('WaveForms.exe'):
				dumpJson(WFexe) #returns only if the file is the correct one
				break
		#installes dependencies
		subprocess.check_call(installMatplotlib)
	elif systemType == 'Linux':
		#asks if waveforms is installed and in case installs dependencies
		WFinstalled = str(input('Is Diligent WaveForms currently installed in this pc? [Y/n]')).lower()
		if WFinstalled == 'y':
			print('OK')
			subprocess.check_call(pipInstall)
			subprocess.check_call(tkInstall)
			subprocess.check_call(installMatplotlib)
		else:
			input('Please install Diligent Adept Runtime and Diligent WaveForms first!\nPress Enter key to continue.\n')

#dump json
def dumpJson(WFexe):
	configPath = os.getcwd() + '\\config.json'
	jsonScheme = [{"installationPath": WFexe}]
	with open(configPath, 'w') as configFile:
		json.dump(jsonScheme, configFile)

if __name__ == "__main__":
	systemType = platform.system()
	print('In order to make these scripts work you need a working Python, LaTEX and GhostScript installation. Please make sure you match these requirements.')
	if str(input('Do you want to continue with the setup? [Y/n]: ')).lower() != 'y': quit()
	setup()