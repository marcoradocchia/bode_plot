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
	#check if config file exists, if it does runs the script, otherwhise asks the use to setup first
	configPath = os.getcwd() + '\\config.json'
	try:
		open(configPath, 'r')
	except:
		print('Please run setup first!')
		quit()
	system = platform.system()
	if system == 'Windows':
		workSpacePath = os.getcwd() + '\\trasferimento_workspace_win.dwf3work'
		configPath = os.getcwd() + '\\config.json'
		with open(configPath, 'r') as configFile:
			readJson = json.load(configFile)[0]
		WFPath = readJson["installationPath"]
		windowsLaunch(WFPath, workSpacePath)
	elif system == 'Linux':
		workSpacePath = os.getcwd() + '/trasferimento_workspace_linux.dwf3work'
		linuxLaunch(workSpacePath)
	else:
		print('Script autorun not supported on this OS.')