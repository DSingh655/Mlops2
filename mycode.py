# import panda as pd
import os

import os 

# os.mkdir("data")

import shutil

shutil.copy("sample_top/1.png", "data")

# dvc init
# dvc remote add -d myremote s3       # store data versioning here
# dvc add data                    # you are reposible for versioning insid data folder