# Azure Functions Set Up

https://azure.microsoft.com/en-us/services/functions/

### Install Ubuntu on your local machine using Hyper-V
Important: The option "Require my password to login" must be selected.

### Install Chrome browser and Git

Open a terminal (press: cntrl + alt + t) and type:
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install chromium-browser git 
```

### Prepare Visual Studio Code (https://code.visualstudio.com)
Install Visual Studio Code by open a terminal and type:
```bash
cd Downloads
wget https://az764295.vo.msecnd.net/stable/ae08d5460b5a45169385ff3fd44208f431992451/code_1.42.0-1580986622_amd64.deb
sudo dpkg -i code_1.42.0-1580986622_amd64.deb
```

Install python and azure functions extensions by open VS Code Quick, press (Ctrl+P), paste the following command, and press enter:
```bash
ext install ms-azuretools.vscode-azurefunctions
ext install ms-python.python
```

### Install Azure Function Core Tools:
Open a terminal and type:
```bash
wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb && sudo dpkg -i packages-microsoft-prod.deb && sudo apt-get update && sudo apt-get install azure-functions-core-tools
```



### Install required python version:
Step 1 - Get numbers of cpu cores for the -j parameter by open a terminal and type:
```bash
nproc 
```
Step 2 - Build python 3.7.5 from source code by open a terminal and type:
```bash
sudo apt update && sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget && cd Downloads && wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz && tar -xf Python-3.7.5.tgz && cd Python-3.7.5 && ./configure --enable-optimizations && make -j 4 && sudo make altinstall
```


### Check if all requirements are available:
Open a terminal and type:
```bash
func
git
python3.7 --version
Open a terminal and type:
```

### Documentation
https://docs.microsoft.com/en-us/azure/python/tutorial-vs-code-serverless-python-01
https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/
https://docs.microsoft.com/en-us/azure/azure-functions/functions-openapi-definition


### Optional
Disable Gnome animations:
```bash
gsettings set org.gnome.desktop.interface enable-animations false
```

## Azure APIM test:
{
"subject": "6",
"to":"12",
"body":"9"
}

{
"subject": "123456789012345",
"to":"-1",
"body":"-1"
}
