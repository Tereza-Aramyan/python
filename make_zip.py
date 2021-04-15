'''
 File-operations. For one folder (homework) gets hierarchy of python files, then crates  zip for that structure using temporary file/dir
'''


import tempfile
import shutil
import os


homework_dir = (os.sep).join((os.getcwd().split(os.sep))[0:-1])
tempdr = tempfile.TemporaryDirectory(prefix='homework', suffix='_1', dir=os.getcwd())


for el in os.listdir(homework_dir):
    if(el.endswith("-Tereza-Aramyan") & ("zip" not in el)):
        os.mkdir(f'{tempdr.name}{os.sep}{el}')
        for root, dirs, files in os.walk(f'{homework_dir}{os.sep}{el}'):
            for file in files:
                if(file.endswith(".py") ):
                    rec =''
                    if ((root.split(os.sep))[-1] != el):
                        rec = (root.split(el))[-1]
                        os.makedirs(f'{tempdr.name}{os.sep}{el}{rec}')

                    shutil.copy(os.path.join(root, file), f'{tempdr.name}{os.sep}{el}{rec}')


shutil.make_archive('homework', 'zip', tempdr.name)
tempdr.cleanup()





