import os
import json
import platform
import subprocess

#LINUX INSTALL REQUIREMENTS COMMANDS
pipInstall = ['sudo', 'apt', 'install', 'python3-pip']
tkInstall = ['sudo', 'apt', 'install', 'python3-tk']
installMatplotlibWin = ['pip', 'install', 'matplotlib==3.3.3']
installMatplotlibLinux = ['pip3', 'install', 'matplotlib==3.3.3']

#RASPBERRY INSTALL PYTHON3-GI-CAIRO
giCairoInstall = ['sudo', 'apt', 'install', 'python3-gi-cairo']

#UBUNTU x86_64 canberra-gtk-module
canberraInstall = ['sudo', 'apt', 'install', 'libcanberra-gtk-module', 'libcanberra-gtk3-module']

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
		#installes dependencies
		subprocess.check_call(installMatplotlibWin)
		Tk().withdraw()
		print('Please select WaveForms.exe installation file from your file system.')
		while True:
			WFexe = askopenfilename(title='Select WaveForms EXE file', filetypes=[('EXE', '.exe')])
			if WFexe == '': quit()
			elif WFexe.endswith('WaveForms.exe'):
				dumpJsonWin(WFexe) #returns only if the file is the correct one
				break
			else:
				print('Please select the correct file.')
		os.remove(os.path.join(os.getcwd(), 'plot_linux.sh'))
		os.remove(os.path.join(os.getcwd(), 'setup_linux.sh'))
		os.remove(os.path.join(os.getcwd(), 'start_measure_linux.sh'))
	elif systemType == 'Linux':
		#asks if waveforms is installed and in case installs dependencies
		WFinstalled = str(input('Is Diligent WaveForms currently installed in this pc? [Y/n]: ')).lower()
		if WFinstalled == 'y':
			print('OK')
			if platform.machine() == 'armv7l': #raspberry requirements
				subprocess.check_call(giCairoInstall)
			if platform.machine() == 'x86_64': #ubuntu x86_64 requirements
				subprocess.check_call(canberraInstall)
			subprocess.check_call(pipInstall)
			subprocess.check_call(tkInstall)
			subprocess.check_call(installMatplotlibLinux)
			dumpJsonLinux()
		else:
			input('Please install Diligent Adept Runtime and Diligent WaveForms first!\nPress Enter key to continue.\n')
		os.remove(os.path.join(os.getcwd(), 'plot_win.bat'))
		os.remove(os.path.join(os.getcwd(), 'setup_win.bat'))
		os.remove(os.path.join(os.getcwd(), 'start_measure_win.bat'))

if __name__ == "__main__":
	systemType = platform.system()
	print('In order to make these scripts work you need a working Python, LaTeX and GhostScript installation.\nBefore you continue, please make sure you match these requirements.')
	if str(input('Do you want to continue with the setup? [Y/n]: ')).lower() != 'y': quit()
	setup()

#CAREFUL! SETUP AUTOREMOVES SYSTEM UNCOMPATIBLE FILES (using linux removes .bat, using windows removes .sh)