import os

# set
os.environ['variable_data'] = 'my_password'

# Standard way is to set environment variable in Windows, Linux, Mac system

# get
env1 = os.getenv('variable_data')
print(env1, type(env1))

env2 = os.environ.get('variable_data')
print(env2, type(env2))



