# coding=utf-8


import os

# Possible ENV values:
# - PROD
# - LOCAL
current_env = os.environ.get('ENV', 'LOCAL')

if current_env == 'PROD':
    # Using production settings
    from newsfeels.settings.prod import *
else:
    # Using local settings
    try:
        from newsfeels.settings.local import *
    except ImportError:
        raise ImportError(
            'You need to define a `local.py` file inside the `newsfeels.settings` package.\n'
            'Please double-check the instructions in `local-template.py` and try again.')
