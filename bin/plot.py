from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import subprocess
import platform
import os

emptyLine = '\n'

def fixFile(csvFile):
	with open(csvFile, 'r') as inFile:
		lines = list(line + '\n' for line in (l.strip() for l in inFile) if line)
	with open(csvFile, 'w+') as outFile:
		outFile.writelines(lines)

def mergeFiles(csvFiles, plotName):
	dirPath = os.path.dirname(os.path.realpath(csvFiles[0]))
	plotName = plotName + '.csv'
	tmpFile = os.path.join(dirPath, plotName)
	allFilesLines = []
	with open(tmpFile, 'w+') as outFile:
		for csvFile in csvFiles:
			with open(csvFile, 'r') as inFile:
				lines = list(line + '\n' for line in (l.strip() for l in inFile) if line)
			lines.append('\n')
			allFilesLines.append(lines)
		allFilesLinesLen = len(allFilesLines) - 1
		allFilesLines[allFilesLinesLen] = allFilesLines[allFilesLinesLen][:-1]
		for line in allFilesLines:
			outFile.writelines(line)
	return tmpFile

def fixWindowsPath(csvFile):
	csvFile = csvFile.split('/')
	csvFile = '\\'.join(csvFile)
	return csvFile

if __name__ == "__main__":
	systemType = platform.system()
	Tk().withdraw()
	csvFiles = askopenfilenames(title='Open data file', filetypes=([('CSV', '.csv')]))
	if csvFiles == '': quit()
	csvFiles = list(csvFiles)
	if len(csvFiles) == 1:
		csvFile = csvFiles[0]
		fixFile(csvFile)
	elif len(csvFiles) > 1:
		print('You selected the following file(s):')
		for csvFile in csvFiles:
			print(csvFile)
		plotName = input('Insert your plot\'s name: ')
		csvFile = mergeFiles(csvFiles, plotName)
		print('New file has been creted: ' + csvFile)
	latexArg = str(input('Print a plot using LaTeX labels? [Y/n]: ')).lower()
	script = os.path.join(os.getcwd(), 'bin', 'auto_transf_multiplot.py')
	if systemType == 'Windows':
		runPython = 'python'
		csvFile = fixWindowsPath(csvFile)
	elif systemType == 'Linux':
		runPython = 'python3'
	plotCommand = [runPython, script, latexArg, csvFile]
	subprocess.Popen(plotCommand)

#TODO: check working on linux
#TODO: in workspace script, force the user to make at least 2 measures