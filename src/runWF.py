import subprocess
import sys
import os
import platform
import json

#check if config file exists, if it does runs the script, otherwhise asks the use to setup first
def checkJsonFile(configPath):
	try:
		with open(configPath, 'r') as configFile:
			readJson = json.load(configFile)[0]
	except:
		print('Please run setup first!')
		quit()
	return readJson

def windowsLaunch(WFPath, workSpacePath):
	openWF = [WFPath, workSpacePath, '-runscript']
	subprocess.Popen(openWF)

def linuxLaunch(workSpacePath):
	openWF = ['waveforms', workSpacePath, '-runscript']
	subprocess.Popen(openWF)

if __name__ == "__main__":
	system = platform.system()	
	if system == 'Windows':
		readJson = checkJsonFile(configPath=os.getcwd() + '\\bin\\config.json')
		WFPath = readJson["installationPath"]
		workSpacePath = os.getcwd() + '\\bin\\trasferimento_workspace_win.dwf3work'
		windowsLaunch(WFPath, workSpacePath)
	elif system == 'Linux':
		checkJsonFile(configPath=os.getcwd() + '/bin/config.json')
		workSpacePath = os.getcwd() + '/bin/trasferimento_workspace_linux.dwf3work'
		linuxLaunch(workSpacePath)
	else:
		print('Script autorun not supported on this OS.')