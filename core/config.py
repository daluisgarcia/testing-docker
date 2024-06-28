import os

from dotenv import dotenv_values

config = dotenv_values('.env')
# config = dict(os.environ) 