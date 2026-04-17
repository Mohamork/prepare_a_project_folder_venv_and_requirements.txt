# Project Description
This is a script that reduces project creation time by automating :
  - Create a project folder
  - Create a virtual environment
  - Install modules
  - Works on Windows, Linux and macOs

## How to use
- Run the script from the same directory you usually create your projects
- From here a new subfolder is created including your virtual environment and optional modules.

### How to automate module installation
- Prepare the modules inside a requirements.txt file
- Store the requirements.txt file inside the same directory where you usually create your projects.
   
##### I have a requirements.txt with content
The script will create a project folder, venv and install packages from the requirements.txt file.

##### I have a requirements.txt but it's empty
The script will create a project folder and venv. No packages get installed.

##### I have no requirements.txt
No problem. The script will create the project folder and the virtual environment. No packages get installed.




