import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
import math as m
from auto_transf_func_multiplot import importData, getCircuitName, getCutOff, splitAt, randomColor

#************************GLOBAL PARAMETERS************************
emptyLine = '\n'
alphaGridMajor = 0.8
alphaGridMinor = 0.4
alphaErrorRange = 0.5
ticksDivisions = 10
line = '-'
dashedLine = '--'

#************************LINE COLORS************************
ubuntuPurple = '#77216F'
ubuntuOrange = '#E95420'
ubuntuWarmGrey = '#AEA79F'
colorPalette = [
	'#E64B35B2',
	'#00A087B2',
	'#00A087B2',
	'#8491B4B2',
	'#3C5488B2',
	ubuntuOrange,
	ubuntuPurple,
	ubuntuWarmGrey
]

#************************SETUP PLOTS************************
def getMultipleLocator(valuesArray):
	multipleLocator = []
	for subArray in valuesArray:
		maxVal = max(subArray)
		minVal = min(subArray)
		multipleLocator.append((maxVal - minVal) / ticksDivisions)
	multipleLocator = max(multipleLocator)
	return multipleLocator


def setUpAx(ax1, ax2, ax3, circuitName, gain, gaindB, phase):
	ax1MultipleLocator = getMultipleLocator(gain)
	ax2MultipleLocator = getMultipleLocator(gaindB)
	ax3MultipleLocator = getMultipleLocator(phase)
	#ax1
	ax1.set_xscale('log')
	ax1.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(ax1MultipleLocator))
	ax1.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(ax1MultipleLocator * 2))
	ax1.grid(True, alpha=alphaGridMajor, linestyle=dashedLine, which='major')
	ax1.grid(True, alpha=alphaGridMinor, linestyle=dashedLine, which='minor')
	if latexUse == True:
		ax1.set_title(r'\textbf{' + '{}'.format(circuitName) + '}')
	else:
		ax1.set_title(r'{}'.format(circuitName))
	#ax2
	ax2.set_xscale('log')
	ax2.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(ax2MultipleLocator))
	ax2.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(ax2MultipleLocator * 2))
	ax2.grid(True, alpha=alphaGridMajor, linestyle=dashedLine, which='major')
	ax2.grid(True, alpha=alphaGridMinor, linestyle=dashedLine, which='minor')
	#ax3
	ax3.set_xscale('log')
	ax3.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(ax3MultipleLocator))
	ax3.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(ax3MultipleLocator * 2))
	ax3.grid(True, alpha=alphaGridMajor, linestyle=dashedLine, which='major')
	ax3.grid(True, alpha=alphaGridMinor, linestyle=dashedLine, which='minor')

#************************PRINT PLOTS************************
def printTransfPlot(freqPlot, transfPlot, ax1, thisPlotColor): #plots out the transf function
	cutOffVals, deltaCutOffVals = getCutOff(freqPlot, transfPlot, case='abs')
	if cutOffVals is not None:
		for index in range(len(cutOffVals)):
			if cutOffVals[index] is not None: #if a cutoff freq is found, plots a vertical line at specific frequency
				ax1.axvline(cutOffVals[index], color=ubuntuOrange, label=r'Cutoff Frequency')
				ax1.axvspan(cutOffVals[index] - deltaCutOffVals[index], cutOffVals[index] + deltaCutOffVals[index], alpha=alphaErrorRange, color=ubuntuWarmGrey)
				ax1.text(cutOffVals[index] + deltaCutOffVals[index], 0.3, str(round(cutOffVals[index])), verticalalignment='center', rotation=-90, color=ubuntuOrange)
	if latexUse == True: #determines the use of latex and latex packages
		ax1Label = r'Trasfer Function'
		ax1yLabel = r'Gain'
	else:
		ax1Label = r'Trasfer Function'
		ax1yLabel = r'Gain'
	ax1.plot(freqPlot, transfPlot, label=ax1Label, color=thisPlotColor)
	ax1.set_ylabel(ax1yLabel)

def printTransfPlotdB(freqPlot, transfPlotdB, ax2, thisPlotColor): #plots out the transf function
	cutOffVals, deltaCutOffVals = getCutOff(freqPlot, transfPlotdB, case='db')
	if cutOffVals is not None:
		for index in range(len(cutOffVals)):
			if cutOffVals[index] is not None: #if a cutoff freq is found, plots a vertical line at specific frequency
				ax2.axvline(cutOffVals[index], color=ubuntuOrange, label=r'Cutoff Frequency')
				ax2.axvspan(cutOffVals[index] - deltaCutOffVals[index], cutOffVals[index] + deltaCutOffVals[index], alpha=alphaErrorRange, color=ubuntuWarmGrey)
				ax2.text(cutOffVals[index] + deltaCutOffVals[index], -25, str(round(cutOffVals[index])), verticalalignment='center', rotation=-90, color=ubuntuOrange)
	if latexUse == True:
		ax2Label = r'Trasfer Function $(\si{\decibel})$'
		ax2yLabel = r'Gain $(\si{\decibel})$'
	else:
		ax2Label = r'Transfer Function (dB)'
		ax2yLabel = r'Gain (dB)'
	ax2.plot(freqPlot, transfPlotdB, label=ax2Label, color=thisPlotColor)
	ax2.set_ylabel(ax2yLabel)

def printPhasePlot(freqPlot, phasePlot, ax3, thisPlotColor): #plots phase vs frequency
	if latexUse == True:
		ax3Label = r'Phase $\phi$'
		ax3xLabel = r'$\nu \, (\si{\hertz})$'
		ax3yLabel = r'$\phi \, (\si{\degree})$'
	else:
		ax3Label = r'Phase'
		ax3xLabel = r'Frequency (Hz)'
		ax3yLabel = r'Phase'
	ax3.plot(freqPlot, phasePlot, label=ax3Label, color=thisPlotColor)
	ax3.set_xlabel(ax3xLabel)
	ax3.set_ylabel(ax3yLabel)

#************************MAIN************************
if __name__ == "__main__":
	#PROCESSING INLINE ARGUMENTS
	args = sys.argv
	args.pop(0)
	try:
		latexArg = args[0]
		inputFilePath = args[1]
	except:
		print('Please give valid arguments.')
		quit()

	#DECIDES THE USE OF TEX TO RENDER THE PLOT
	if latexArg == 'y':
		latexUse = True
		rc('font',**{'family':'serif','serif':['Roman']})
		plt.rcParams.update({
			"text.usetex": True
		})
		preamble = r'\usepackage{siunitx} \usepackage{amsmath}'
		params = {
			'text.latex.preamble': preamble
		}
		plt.rcParams.update(params)
		print('Using LateX labels!')
	else:
		latexUse = False
		print('Not using LateX labels!')

	#GETTING THE PLOT DATA INTO ARRAYS
	freq, inVolt, outVolt, gain, gaindB, phase, circuitName = importData(inputFilePath)
	freq = splitAt(array=freq, entry=emptyLine)
	inVolt = splitAt(array=inVolt, entry=emptyLine)
	outVolt = splitAt(array=outVolt, entry=emptyLine)
	gain = splitAt(array=gain, entry=emptyLine)
	gaindB = splitAt(array=gaindB, entry=emptyLine)
	phase = splitAt(array=phase, entry=emptyLine)

	#DEFINING SUBPLOTS
	fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
	setUpAx(ax1, ax2, ax3, circuitName, gain, gaindB, phase) #set up axes parameters
	fig.canvas.set_window_title(circuitName) #changes window title to circuitName
	for index in range(len(freq)): #print every curve
		thisPlotColor, colorPalette = randomColor(colorPalette) #picks this plot color
		printTransfPlot(freq[index], gain[index], ax1, thisPlotColor)
		printTransfPlotdB(freq[index], gaindB[index], ax2, thisPlotColor)
		printPhasePlot(freq[index], phase[index], ax3, thisPlotColor)
	plt.tight_layout() #adjust padding
	plt.show() #makes window with plots