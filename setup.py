'''

setup.py file is essential for **packaging and distributing** pyhton projects.
define **configuration** of our project.

'''
from setuptools import find_packages,setup
from typing import List

def get_requirements():
    """
    This function will return list of requirements
    
    """
    requirement_lst = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

# print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Saprativa",
    author_email="saprativas@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
