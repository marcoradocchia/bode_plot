# Scripted Transfert Function acquisition and plotting
Scripts for automatic transfer function acquisition on _Digikent Studio_

## Requirements:
* __Digilent WaveForms__
* __Digilent Adept for Linux Runtime__ (Linux only)
* __Python 3__: in case you're using these scripts on Windows you need to add it to Path in Environment Variables section; should be already installed on Linux
* __TEX distribution__ (tested using TeX Live)
* __GhostScript__: required by 'matplotlib' in order to work with LaTeX (should be already installed on Linux)


## Important:
* In order to make the scripts work you need to donwload the files as _.zip_ and extract the zip in the _Documents_ folder of your system (please do not rename the folder, extract the files maintaining the default name)
* These scripts support Windows and Debian based Linux distributions
* Careful! The scripts are not working on _Python 2_
* Please don't apply any changes to the _*.dwf3work_ files! They contain a script that runs the data acquisition


## Download Links:
* [Digilent WaveForms](https://mautic.digilentinc.com/waveforms-download)
* [Digilent Adept for Linux Runtime](https://mautic.digilentinc.com/adept-runtime-download)
* [TeX Live (Windows)](https://tug.org/texlive/acquire-netinstall.html)
* [GhostScript (Windows)](https://ghostscript.com/download/gsdnld.html)