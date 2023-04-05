from pathlib import Path


app_root_dir = Path(__file__).absolute().parent.parent

save_file_path = f'{app_root_dir}/data/SAVE_FILE.pickle'

Path(save_file_path).touch()