from tkinter import Tk
from tkinter.filedialog import askopenfilename
import subprocess
import platform
import os

def fixWindowsPath(csvFile):
	csvFile = csvFile.split('/')
	csvFile = '\\'.join(csvFile)
	return csvFile

if __name__ == "__main__":
	systemType = platform.system()
	Tk().withdraw()
	while True:
		csvFile = askopenfilename()
		if csvFile == '': quit()
		elif csvFile.endswith('.csv'):
			break
		print('Please select a .csv file!')
	latexArg = str(input('Print a plot using LaTeX labels? [Y/n]: ')).lower()
	if systemType == 'Windows':
		runPython = 'python'
		script = os.getcwd() + '\\bin\\auto_transf_multiplot.py'
		csvFile = fixWindowsPath(csvFile)
	elif systemType == 'Linux':
		runPython = 'python3'
		script = os.getcwd() + '/bin/auto_transf_multiplot.py'
	plotCommand = [runPython, script, latexArg, csvFile]
	subprocess.Popen(plotCommand)

#TODO: check working on linux
#TODO: ask for multiple plotting and let user open more than one single file if he wants. if so make one file containing all the data and separate the different files data with a blank line
#TODO: in workspace script, force the user to make at least 2 measures