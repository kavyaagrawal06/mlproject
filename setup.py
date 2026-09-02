#setup.py helps turn your ML project's code into an installable Python package, so its modules/functions can be imported cleanly wherever that package is installed.

from setuptools import find_packages,setup  #setuptools is a Python library used to create and install Python packages.
                                              # find_packages It automatically finds the packages inside your project.

from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]: 
    
    #file_path: str means:
         #file_path should be a string.
         
     #List[str]: means    
    #A list containing strings.
    '''
    this function will return the list of requirements
    '''
    requirements=[] #It's an empty list.
    with open(file_path) as file_obj: #This opens the file whose path was provided.
        requirements=file_obj.readlines() #readlines() reads every line and creates a list
        requirements=[req.replace("\n","") for req in requirements] #removes the newline character from every requirement.

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(             #This is the main function that gives information about your project.  
                     #It tells Python:
                     #"Here is my project's name, version, packages, dependencies, etc."
name='mlproject',
version='0.0.1',
author='kavya',
author_email='kavyaagrawal1410@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)