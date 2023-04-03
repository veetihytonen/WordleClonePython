import os
from pathlib import Path

# Magic number 19 is number of characters that need to be removed so that 
# '/src/save_config' is erased from path and we get path to project root dir.
# This is fucking cursed but I don't care to look for a better way.
app_root_dir = os.path.abspath(__file__)[:-19]

save_file_path = f'{app_root_dir}/data/SAVE_FILE.pickle'

Path(save_file_path).touch()