# Cliqly Installation Setup

## Setting Up Python 3.12 and Required Packages on a MacBook Using the Command Line

This guide will walk you through the process of setting up Python 3.12 on your MacBook using the command line, installing PyCharm, managing your project dependencies, and cloning the Cliqly repository from GitHub.

## Table of Contents
1. [Installing Python 3.12 Using Command Line](#installing-python-312-using-command-line)
2. [Installing PyCharm](#installing-pycharm)
3. [Cloning the Git Repository](#cloning-the-git-repository)
4. [Setting Up Your Project](#setting-up-your-project)
5. [Installing Required Libraries](#installing-required-libraries)

## Installing Python 3.12 Using Command Line

1. **Install Homebrew:**
   - Open Terminal.
   - Install Homebrew by running the following command:
     ```sh
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Follow the on-screen instructions to complete the installation.

2. **Update Homebrew:**
   - After installing Homebrew, update it to make sure you have the latest version and package information:
     ```sh
     brew update
     ```

3. **Install Python 3.12:**
   - Use Homebrew to install Python 3.12:
     ```sh
     brew install python@3.12
     ```

4. **Verify the Installation:**
   - Check the installed version of Python:
     ```sh
     python3.12 --version
     ```
   - You should see something like `Python 3.12.x`.

5. **Set Up Python 3.12 as the Default Python Version (Optional):**
   - If you want to use Python 3.12 as your default Python version, you can update your shell profile:
     ```sh
     echo 'export PATH="/usr/local/opt/python@3.12/bin:$PATH"' >> ~/.zshrc
     source ~/.zshrc
     ```
   - Verify the update by running:
     ```sh
     python3 --version
     ```

## Installing PyCharm

1. **Download PyCharm:**
   - Open your web browser and go to the official JetBrains website: [PyCharm Downloads](https://www.jetbrains.com/pycharm/download/)
   - Select the Community Edition (free) or the Professional Edition (paid) and download the installer.

2. **Install PyCharm:**
   - Open the downloaded `.dmg` file.
   - Drag and drop the PyCharm icon into the Applications folder.
   - Open PyCharm from the Applications folder.

## Cloning the Git Repository

1. **Open Terminal:**
   - Navigate to the directory where you want to clone the repository:
     ```sh
     cd path/to/your/directory
     ```

2. **Clone the Repository:**
   - Run the following command to clone the Cliqly repository:
     ```sh
     git clone https://github.com/SanaAkram/Cliqly.git
     ```

3. **Navigate to the Project Directory:**
   - Change to the project directory:
     ```sh
     cd Cliqly
     ```


## Setting Up Your Project

1. **Create a Virtual Environment:**
   - Create a virtual environment in the project directory:
     ```sh
     python3.12 -m venv venv
     ```

2. **Activate the Virtual Environment:**
   - Activate the virtual environment:
     ```sh
     source venv/bin/activate
     ```

3. **Configure the Python Interpreter in PyCharm:**
   - Open PyCharm.
   - Click on "Open" and select the cloned repository.
   - Go to `PyCharm > Preferences` (or `File > Settings` on Windows/Linux).
   - Navigate to `Project: Cliqly > Python Interpreter`.
   - Ensure that the virtual environment you created is selected. If not, add it by clicking on the gear icon and selecting `Add...`.

## Installing Required Libraries

1. **Install Libraries Using Command Line:**
   - With the virtual environment activated, install the required libraries:
     ```sh
     pip install requests beautifulsoup4 lxml pandas
     ```

## Conclusion

