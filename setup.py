from setuptools import find_packages,setup
from typing import List

from pathlib import Path
HYPHEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will returnt he list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements



setup(
name = "mlproject",
version='0.001',
author ='LV',
author_email = 'mygalaxy02082020@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)