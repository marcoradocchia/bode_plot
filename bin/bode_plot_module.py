from math import sqrt, log10
import random
import platform

#************************FUNCTIONS************************
def checkData(scopeData):
	for val in scopeData: #i need to check if the input data file presents some infinity values that break matplolib
		val = float(val)
		if val == float('inf') or val == float('-inf'):
			print('Input file contains some invalid values. Please check your input file!')
			quit()

def importData(inputFilePath):
	try:
		inputFile = open(inputFilePath, 'r')
	except:
		print('Couldn\'t open the given file, try again.')
		quit()
	freq = []
	inVolt = []
	outVolt = []
	gain = []
	gaindB = []
	phase = []
	for line in inputFile:
		if line == '\n':
			freq.append(line)
			inVolt.append(line)
			outVolt.append(line)
			gain.append(line)
			gaindB.append(line)
			phase.append(line)
			continue
		scopeData = line.split(',')
		checkData(scopeData)
		freq.append(float(scopeData[0]))
		inVolt.append(float(scopeData[1]))
		outVolt.append(float(scopeData[2]))
		gain.append(float(scopeData[3]))
		gaindB.append(float(scopeData[4]))
		phase.append(float(scopeData[5]))
	return freq, inVolt, outVolt, gain, gaindB, phase, getCircuitName(inputFilePath)

def splitAt(array, entry): #function that accepts an array and a variable and splits the array in several arrays using entry as splitpoint
	outArray = [[]]
	index = 0
	for element in array:
		if element == entry:
			index += 1
			outArray.append([])
			continue
		outArray[index].append(element)
	return outArray

def formatTicks(multipleLocator): 
	digit = round(log10(multipleLocator))
	if digit > 0:
		formatTicksVal = 0
	elif digit == 0:
		formatTicksVal = 1
	elif digit < 0:
		formatTicksVal = abs(digit - 1)
	return formatTicksVal

def getCircuitName(inputFilePath):
	systemType = platform.system()

	if systemType == 'Windows':
		inputFilePath = inputFilePath.split('\\')
	elif systemType == 'Linux':
		inputFilePath = inputFilePath.split('/')
	fileName = inputFilePath[len(inputFilePath) - 1]
	fileName = fileName.split('.csv')[0]
	fileName = fileName.split('_')
	name = ''
	if len(fileName) > 1:
		for element in fileName:
			name += element + ' '
		name = name.title()
	else:
		name = fileName[0].title()
	return name

def printCuoffResults(cutOffVals, deltaCutOffVals, case): #prints cutoff measure and bandwidth in terminal (where present)
	if case == 'abs':
		print('Cutoff Frequency(s):')
	elif case == 'db':
		print('Cutoff Frequency(s), dB measure:')
	if cutOffVals is not None:
		for index in range(len(cutOffVals)):
			if deltaCutOffVals[index] > 1: 
				cutOffVals[index] = int(round(cutOffVals[index], 0))
				deltaCutOffVals[index] = int(round(deltaCutOffVals[index], 0))
			else:
				cutOffVals[index] = round(cutOffVals[index], 1)
				deltaCutOffVals[index] = round(deltaCutOffVals[index], 1)
			print(str(cutOffVals[index]) + ' +/- ' + str(deltaCutOffVals[index]) + ' Hz')

def getCutOff(freqPlot, transfPlot, case): #returns the cutoff frequency(s) and delta(s)
	if case == 'abs': cutVal = 1 / sqrt(2)
	elif case == 'db': cutVal = -3.
	cutOffVals = []
	deltaCutOffVals = []
	for index in range(len(freqPlot) - 1):
		if transfPlot[index] >= cutVal and transfPlot[index + 1] <= cutVal:
			cutOffVal = (freqPlot[index + 1] + freqPlot[index]) / 2
			deltaCutOffVal = freqPlot[index + 1] - cutOffVal
			#appending to arrays
			cutOffVals.append(cutOffVal)
			deltaCutOffVals.append(deltaCutOffVal)
		if transfPlot[index] <= cutVal and transfPlot[index + 1] >= cutVal:
			cutOffVal = (freqPlot[index + 1] + freqPlot[index]) / 2
			deltaCutOffVal = freqPlot[index + 1] - cutOffVal
			#appending to arrays
			cutOffVals.append(cutOffVal)
			deltaCutOffVals.append(deltaCutOffVal)
	if len(cutOffVals) != 0 and len(deltaCutOffVals) != 0:
		printCuoffResults(cutOffVals, deltaCutOffVals, case)
		return cutOffVals, deltaCutOffVals
	else:
		return None, None

def getCutOffLabel(latexUse, cutOff, deltaCutOff):
	if latexUse == True: #determines the use of latex and latex packages
		return r'Cutoff: ${}\pm{}'.format(cutOff, deltaCutOff) + r'\si{\hertz}$'
	else:
		return r'Cutoff: {} ± {} Hz'.format(cutOff, deltaCutOff)

def printLegend(ax1LegendCheck, ax2LegendCheck, ax3LegendCheck, ax1, ax2, ax3):
	if ax1LegendCheck == True: ax1.legend(loc='best')
	if ax2LegendCheck == True: ax2.legend(loc='best')
	if ax3LegendCheck == True: ax3.legend(loc='best')

def pickColor(colorPalette):
	try:
		color = colorPalette[0]
		colorPalette.pop(0)
		return color, colorPalette
	except:
		print('Too many plots.')
		quit()