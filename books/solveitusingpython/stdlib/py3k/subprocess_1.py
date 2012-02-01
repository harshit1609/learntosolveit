# using os.system() you could call the external operating system calls
# That is equivalent to call() method from subprocess.
# Optional shell argument provides the facility to pass the shell variables.

# Doing it os.system way
import os
os.system('date')

# Doing it subprocess way
from subprocess import call
call('date')

# Accessing shell variables
# Since we set shell=True, the shell variables are expanded in the command line
call('echo $PATH',shell=True)
