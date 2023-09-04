
'''
Constructs nessecery path & files for the server to run 
'''

import os , yaml

if not os.path.exists(os.path.join(os.getcwd(),'folder')):
    os.mkdir(os.path.join(os.getcwd(),'folder'))

if not os.path.exists(os.path.join(os.getcwd(),'.gitignore')):
    with open('.gitignore', 'x') as git_file:
        git_file.write('')
        git_file.close()

if not os.path.exists(os.path.join(os.getcwd(),'config.yaml')): 
    with open('config.yaml', 'x') as config: 
        # file = yaml.safe_load(config)
        data = {
            'clients' : {}
        }
        yaml.safe_dump(data, config)
        config.close()   