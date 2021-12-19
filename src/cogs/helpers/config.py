import yaml

from typing import Union

CONFIG_PATH = 'src/config.yml'

def load():
    """Parses the config.

    Returns:
        dict: The parsed YAML Data from src/config.yml
    """
    parsed_config_data = yaml.load(open(CONFIG_PATH), Loader=yaml.SafeLoader)
    return parsed_config_data

def nested_set(dic: dict, keys: list, value) -> None:
    """Helps with editing a nested dictionary, see https://stackoverflow.com/a/13688108/14345173

    Args:
        dic (dict): Input dictionary
        keys (list): List of keys for the path
        value (any): Value to set
    """
    
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value

def edit(path: Union[str, list], to: str) -> None:
    """Edits the config

    Args:
        path (str/list): path for the keys to access/edit
        to (str): Value to edit it to
    """

    if isinstance(path, str):
        path = [path]

    source = load()
    nested_set(source, path, to)

    yaml.dump(data=source, stream=open(CONFIG_PATH, 'w'), indent=2)
    
if __name__ == '__main__':
    edit()