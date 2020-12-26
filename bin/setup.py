import os
import json
import platform
import subprocess

#LINUX INSTALL REQUIREMENTS COMMANDS
pipInstall = ['sudo', 'apt', 'install', 'python3-pip']
tkInstall = ['sudo', 'apt', 'install', 'python3-tk']
installMatplotlibWin = ['pip', 'install', 'matplotlib==3.3.3']
installMatplotlibLinux = ['pip3', 'install', 'matplotlib==3.3.3']

#dump json
def dumpJsonWin(WFexe):
	configPath = os.getcwd() + '\\bin\\config.json'
	jsonScheme = [{"installationPath": WFexe}]
	with open(configPath, 'w') as configFile:
		json.dump(jsonScheme, configFile)

def dumpJsonLinux():
	configPath = os.getcwd() + '/bin/config.json'
	jsonScheme = [{"setupComplete": "ok"}]
	with open(configPath, 'w') as configFile:
		json.dump(jsonScheme, configFile)

#detect WF istallation path
def setup():
	if systemType == 'Windows':
		#import tkinter only
		from tkinter import Tk
		from tkinter.filedialog import askopenfilename

		#writes in a config.json the path of the waveforms.exe installation
		if str(input('Make sure your Python and GhostScript installations are added to PATH. Confirm? [Y/n]: ')).lower() != 'y': quit()
		print('Please select WaveForms.exe installation file from your file system.')
		Tk().withdraw()
		#installes dependencies
		subprocess.check_call(installMatplotlibWin)
		while True:
			WFexe = askopenfilename()
			if WFexe == '': quit()
			elif WFexe.endswith('WaveForms.exe'):
				dumpJsonWin(WFexe) #returns only if the file is the correct one
				break
	elif systemType == 'Linux':
		#asks if waveforms is installed and in case installs dependencies
		WFinstalled = str(input('Is Diligent WaveForms currently installed in this pc? [Y/n]: ')).lower()
		if WFinstalled == 'y':
			print('OK')
			subprocess.check_call(pipInstall)
			subprocess.check_call(tkInstall)
			subprocess.check_call(installMatplotlibLinux)
			dumpJsonLinux()
		else:
			input('Please install Diligent Adept Runtime and Diligent WaveForms first!\nPress Enter key to continue.\n')

if __name__ == "__main__":
	systemType = platform.system()
	print('In order to make these scripts work you need a working Python, LaTeX and GhostScript installation.\nBefore you continue, please make sure you match these requirements.')
	if str(input('Do you want to continue with the setup? [Y/n]: ')).lower() != 'y': quit()
	setup()