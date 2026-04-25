# Project Description
Automate the initial steps of your new project. A dedicated script to:
  - Create a project folder inside the parent folder for all of your projects
  - Upgrade to the latest version of pip
  - Create a virtual environment
  - Install modules
  - Save installed modules in a new requirements.txt file
  

## Before using the script
  - Save the script in whichever folder you like. For example my_scripts
  - On line 14 replace parent_folder = 'INSERT THE PARENT FOLDER FOR ALL YOUR PROJECTS HERE to a folder which you will like to create new projects
  - Create an empty requirements.txt file in the same folder as the script. From here the script will know which modules to install. This can be updated for future projects

## How to use
- Open a commandline shell and run the script i.e 'python my_scripts\stage_new_project.py'
- Type in the name of the new project

## Results
- You will have a dedicated folder for your new project
- Installed all the specified modules
- A dedicated virtual environment for your project
- A new requirements.txt file which you can commit along with the rest of your project
   
**Works on Windows, Linux and macOs**


