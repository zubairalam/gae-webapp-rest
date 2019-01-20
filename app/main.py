import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# how flask or requests library module import works?
sys.path.insert(0, PROJECT_ROOT)


import ipdb; ipdb.set_trace()

from gae_rest import ValidationError
