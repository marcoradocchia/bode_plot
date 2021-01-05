import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
import math as m
from auto_transf_func_multiplot import importData, getCircuitName, getCutOff, splitAt, pickColor, formatTicks, getCutOffLabel, printLegend

#************************GLOBAL PARAMETERS************************
emptyLine = '\n'
alphaGridMajor = 0.8
alphaGridMinor = 0.4
alphaErrorRange = 0.5
ticksDivisions = 10
line = '-'
dashedLine = '--'
latexFigWidth = 11.6

#************************LINE COLORS************************
ubuntuWarmGrey = '#AEA79F'
vertLineColor = '#77AADD'
colorPalette = [
	'#EE8866',
	'#B34255',
	'#59B342',
	'#787878'
]

#************************SETUP PLOTS************************
def getTicks(valuesArray):
	multipleLocator = []
	for subArray in valuesArray:
		maxVal = max(subArray)
		minVal = min(subArray)
		deltaVal = abs(maxVal - minVal)
		if deltaVal == 0:
			print('Invalid range, please retry.')
			quit()
		multipleLocator.append(deltaVal / ticksDivisions)
	multipleLocator = max(multipleLocator)
	tickFormat = formatTicks(multipleLocator)
	return multipleLocator, tickFormat

def setUpAx(ax1, ax2, ax3, circuitName, gain, gaindB, phase):
	ax1MultipleLocator, ax1TickFormat = getTicks(gain)
	ax2MultipleLocator, ax2TickFormat = getTicks(gaindB)
	ax3MultipleLocator, ax3TickFormat = getTicks(phase)
	#ax1
	ax1.set_xscale('log')
	ax1.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(ax1MultipleLocator))
	ax1.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(ax1MultipleLocator * 2))
	ax1.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.{}f'.format(ax1TickFormat)))
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
	ax2.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.{}f'.format(ax2TickFormat)))
	ax2.grid(True, alpha=alphaGridMajor, linestyle=dashedLine, which='major')
	ax2.grid(True, alpha=alphaGridMinor, linestyle=dashedLine, which='minor')
	#ax3
	ax3.set_xscale('log')
	ax3.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(ax3MultipleLocator))
	ax3.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(ax3MultipleLocator * 2))
	ax3.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.{}f'.format(ax3TickFormat)))
	ax3.grid(True, alpha=alphaGridMajor, linestyle=dashedLine, which='major')
	ax3.grid(True, alpha=alphaGridMinor, linestyle=dashedLine, which='minor')

#************************PRINT PLOTS************************
def printTransfPlot(freqPlot, transfPlot, ax1, ax1Label, thisPlotColor): #plots out the transf function
	cutOffVals, deltaCutOffVals = getCutOff(freqPlot, transfPlot, case='abs')
	ax1LegendCheck = False
	if cutOffVals is not None:
		for index in range(len(cutOffVals)):
			if cutOffVals[index] is not None: #if a cutoff freq is found, plots a vertical line at specific frequency
				ax1LegendCheck = True
				ax1CutoffLabel = getCutOffLabel(latexUse, cutOffVals[index], deltaCutOffVals[index])
				ax1.axvline(cutOffVals[index], color=vertLineColor, label=ax1CutoffLabel)
				ax1.axvspan(cutOffVals[index] - deltaCutOffVals[index], cutOffVals[index] + deltaCutOffVals[index], alpha=alphaErrorRange, color=ubuntuWarmGrey)
	ax1yLabel = r'Gain'
	ax1.set_ylabel(ax1yLabel)
	if ax1Label is not None:
		ax1.plot(freqPlot, transfPlot, color=thisPlotColor, label=ax1Label)
	else:
		ax1.plot(freqPlot, transfPlot, color=thisPlotColor)
	return ax1LegendCheck


def printTransfPlotdB(freqPlot, transfPlotdB, ax2, ax3, ax2Label, thisPlotColor): #plots out the transf function
	cutOffVals, deltaCutOffVals = getCutOff(freqPlot, transfPlotdB, case='db')
	ax2LegendCheck = False
	if cutOffVals is not None:
		for index in range(len(cutOffVals)):
			if cutOffVals[index] is not None: #if a cutoff freq is found, plots a vertical line at specific frequency
				ax2LegendCheck = True
				ax2CutoffLabel = getCutOffLabel(latexUse, cutOffVals[index], deltaCutOffVals[index])
				ax2.axvline(cutOffVals[index], color=vertLineColor, label=ax2CutoffLabel)
				ax2.axvspan(cutOffVals[index] - deltaCutOffVals[index], cutOffVals[index] + deltaCutOffVals[index], alpha=alphaErrorRange, color=ubuntuWarmGrey)
				ax3.axvline(cutOffVals[index], color=vertLineColor, label=ax2CutoffLabel)
				ax3.axvspan(cutOffVals[index] - deltaCutOffVals[index], cutOffVals[index] + deltaCutOffVals[index], alpha=alphaErrorRange, color=ubuntuWarmGrey)
	if latexUse == True:
		ax2yLabel = r'Gain $(\si{\decibel})$'
	else:
		ax2yLabel = r'Gain (dB)'
	ax2.set_ylabel(ax2yLabel)
	if ax2Label is not None:
		ax2.plot(freqPlot, transfPlotdB, color=thisPlotColor, label=ax2Label)
	else:
		ax2.plot(freqPlot, transfPlotdB, color=thisPlotColor)
	return ax2LegendCheck

def printPhasePlot(freqPlot, phasePlot, ax3, ax3Label, thisPlotColor): #plots phase vs frequency
	if latexUse == True:
		ax3xLabel = r'$\nu \, (\si{\hertz})$'
		ax3yLabel = r'$\lvert\Delta \phi \, (\si{\degree})\rvert$'
	else:
		ax3xLabel = r'Frequency (Hz)'
		ax3yLabel = r'|Phase Shift|'
	ax3.set_xlabel(ax3xLabel)
	ax3.set_ylabel(ax3yLabel)
	if ax3Label is not None:
		ax3.plot(freqPlot, phasePlot, color=thisPlotColor, label=ax3Label)
		return True
	else:
		ax3.plot(freqPlot, phasePlot, color=thisPlotColor)
		return False

#************************MAIN************************
if __name__ == "__main__":
	#PROCESSING INLINE ARGUMENTS
	args = sys.argv
	args.pop(0)
	try:
		latexArg = args[0]
		inputFilePath = args[1]
		plotNames = []
		if len(args) > 2:
			mergePlotNames = args[2:]
			for name in mergePlotNames:
				plotNames.append(getCircuitName(name))
			ax1LegendCheck = True
			ax2LegendCheck = True
		lenPlotNames = len(plotNames)
	except:
		print('Please give valid arguments.')
		quit()

	#DECIDES THE USE OF TEX TO RENDER THE PLOT
	if latexArg == 'y':
		latexUse = True
		rc('font',**{'family':'serif'})
		preamble = r'\usepackage{siunitx} \usepackage{amsmath}'
		params = {
			'text.usetex': True,
			'figure.figsize': (latexFigWidth, latexFigWidth/(4/3)),
			'font.size' : 11,
			'axes.labelsize': 11,
			'legend.fontsize': 11,
			'text.latex.preamble': preamble
		}
		plt.rcParams.update(params)
		print('Using LaTeX labels!')
	else:
		latexUse = False
		print('Not using LaTeX labels!')

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
		if lenPlotNames != 0:
			plotLabels = plotNames[index]
		else:
			plotLabels = None
		thisPlotColor, colorPalette = pickColor(colorPalette) #picks this plot color
		ax1LegendCheck = printTransfPlot(freq[index], gain[index], ax1, plotLabels, thisPlotColor)
		ax2LegendCheck = printTransfPlotdB(freq[index], gaindB[index], ax2, ax3, plotLabels, thisPlotColor)
		ax3LegendCheck = printPhasePlot(freq[index], phase[index], ax3, plotLabels, thisPlotColor)
	if lenPlotNames != 0:
		ax1LegendCheck = True
		ax2LegendCheck = True
	printLegend(ax1LegendCheck, ax2LegendCheck, ax3LegendCheck, ax1, ax2, ax3)
	plt.tight_layout() #adjust padding
	plt.show() #makes window with plots