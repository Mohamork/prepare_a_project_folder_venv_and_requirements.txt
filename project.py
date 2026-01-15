'''
This script creates a project folder, install a venv, then install packages from a requirements.txt file.
At the end it creates a requirements.txt inside the project for future collaborators to use.
'''
import os
import sys
import venv
import subprocess

# Create a name for the project and the venv
project_name = input('Please give a name for this project > ').lower()
venv_name = 'venv'
# Exit and do not create the folder if it exists
if not os.path.exists(project_name) :
    os.makedirs(project_name)
    print(f'A new folder name: {project_name} is created')
else: 
    print(project_name,'already exists.','\nExiting.')
    sys.exit()    
# Get the absolute path for the project and combine with the venv name
project_path = os.path.abspath(project_name)
venv_path = os.path.join(project_name,venv_name)
# Create the virtual environment
print('Please wait while installing the virtual environment...')
venv.EnvBuilder(with_pip=True).create(venv_path)
# Use the venv's Python interpreter
if os.name =='nt' :
    python = os.path.join(venv_path,'Scripts','python')   # if on a windows computer
else :
    python = os.path.join(venv_path,'bin','python') # if on a Linux or Mac
# Upgrade pip
result = subprocess.check_call([
    python,'-m','pip','install','--upgrade', 'pip'])
print(result)
# Install packages from requirements.txt
result = subprocess.check_call([
    python, '-m','pip','install','-r', 'requirements.txt'])
# Create a new requirements.txt inside the projectfolder
with open(f'{project_path}/requirements.txt','w')  as f:
    result = subprocess.check_call([
        python, '-m','pip','freeze'],stdout=f,)
    print('* '*15)
    print(f'requirements.txt is created inside {project_path} for reference for collaborators.')
# Display the installed packages
with open(f'{project_path}/requirements.txt', 'r') as f:
    pkg = (sum(1 for _ in f)) 
subprocess.check_call([python,'-m','pip','list'])
print(f'Installed {pkg} packages from requirements.txt')

'''

with open(f'{project_path}/requirements.txt', 'r') as f:
    print(sum(1 for pkg in f)) 

'''





