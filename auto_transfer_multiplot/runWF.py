import subprocess
import sys
import os
import platform
import json

def windowsLaunch(WFPath, workSpacePath):
	openWF = [WFPath, workSpacePath, '-runscript']
	subprocess.Popen(openWF)

def linuxLaunch(workSpacePath):
	openWF = ['waveforms', workSpacePath, '-runscript']
	subprocess.Popen(openWF)

if __name__ == "__main__":
	system = platform.system()
	workSpacePath = os.getcwd() + '\\trasferimento_workspace.dwf3work'
	if system == 'Windows':
		configPath = os.getcwd() + '\\config.json'
		with open(configPath, 'r') as configFile:
			readJson = json.load(configFile)[0]
		WFPath = readJson["installationPath"]
		windowsLaunch(WFPath, workSpacePath)
	elif system == 'Linux':
		linuxLaunch(workSpacePath)
	else:
		print('Script autorun not supported on this OS.')