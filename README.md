# Scripted Transfert Function acquisition and plotting
Scripts for automatic Transfer Function acquisition on __Digilent Studio__ and automatic plotting

## Requirements:
* __Digilent WaveForms__
* __Digilent Adept for Linux Runtime__ (Linux only)
* __Python 3__: in case you're using these scripts on Windows you need to install and add Python3 to Path in Environment Variables; already installed on Linux
* __TEX distribution__ (tested using TeX Live)
* __GhostScript__: required by 'matplotlib' in order to work with LaTeX (already installed on Linux)


## Important:
* In order to make the scripts work you need to clone this repository into the _Documents_ directory of your file system (please __DO NOT__ rename the cloned directory, keep the default name '_transf\_function_')
* These scripts support Windows and Debian based Linux distributions (tested on Windows, Ubuntu 20.10, RaspberryOS)
* Careful! The scripts are __NOT__ working on Python2
* Please don't apply any changes to the ```*.dwf3work``` files!
* On _Linux_ run scripts using: ```bash ./*.sh```


## Download Links:
* [Digilent WaveForms](https://mautic.digilentinc.com/waveforms-download)
* [Digilent Adept for Linux Runtime](https://mautic.digilentinc.com/adept-runtime-download)
* [TeX Live (Windows)](https://tug.org/texlive/acquire-netinstall.html)
* [GhostScript (Windows)](https://ghostscript.com/download/gsdnld.html)


## Scripts Description:
To use these scripts clone this repository into your file system as ```~/Documents/transfer_function/```.
Using Git: ```git clone https://gihub.com/marcoradocchia/transfer_function```

Use _win_ or _linux_ version of the scripts, wheter you are on a Windows or Linux system:
* ```setup_win.bat```, ```setup_linux.sh```: creates a configuration file and donwloads/installs further required packages
* ```start_measure_win.bat```, ```start_measure_linux.sh```: starts a transfer function measurement in _WaveForms_, saves a _*.csv_ file containing the data and asks you if you want to immediately plot it
* ```plot_win.bat```, ```plot_linux.sh```: plots data in a given _*.csv_ file(s) (columns in the input file need to be [frequency, input voltage, output voltage, gain, gain (dB), phase]); if more than a file is given, merges all the plots into a single one, labelling each curve with the _*.csv_ file name