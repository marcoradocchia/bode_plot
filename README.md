# Scripted Transfert Function acquisition and plotting
Scripts for automatic transfer function acquisition on _Digilent Studio_

## Requirements:
* __Digilent WaveForms__
* __Digilent Adept for Linux Runtime__ (Linux only)
* __Python 3__: in case you're using these scripts on Windows you need to add it to Path in Environment Variables section; should be already installed on Linux
* __TEX distribution__ (tested using TeX Live)
* __GhostScript__: required by 'matplotlib' in order to work with LaTeX (should be already installed on Linux)


## Important:
* In order to make the scripts work you need to clone this repository into the _Documents_ directory of your file system (please __DO NOT__ rename the cloned directory, keep the default name '_transf\_function_')
* These scripts support Windows and Debian based Linux distributions
* Careful! The scripts are not working on _Python 2_
* Please don't apply any changes to the _*.dwf3work_ files!


## Download Links:
* [Digilent WaveForms](https://mautic.digilentinc.com/waveforms-download)
* [Digilent Adept for Linux Runtime](https://mautic.digilentinc.com/adept-runtime-download)
* [TeX Live (Windows)](https://tug.org/texlive/acquire-netinstall.html)
* [GhostScript (Windows)](https://ghostscript.com/download/gsdnld.html)


## Scripts Description:
To use these scripts clone this repository into your file system as _'~/Documents/transfer\_function'_
Use _win_ or _linux_ version of the scripts, wheter you are on a Windows or Linux system:
* __setup_win__, __setup_linux__: creates a configuration file and donwloads/installs further required packages
* __start_measure_win__, __start_measure_linux__: starts a transfer function in _WaveForms_, lets you save a _.csv_ file of the measure and asks you if you want to immediately plot it
* __plot_win__, __plot_linux__: plots data in a given _.csv_ file(s) (columns in the input file need to be [frequency, input voltage, output voltage, gain, gain (dB), phase]); if more than a file is given, merges all the plots into a single one, labelling each curve with the _.csv_ file name