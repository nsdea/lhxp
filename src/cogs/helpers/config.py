import yaml

from typing import Union

def get_path(name: str='config') -> str:
    return f'src/{name}.yml'

def load(name: str='config') -> dict:
    """Parses the config.

    Args:
        name (str): Optional - the file name (without extension), defaults to "config" (for "config.yml")

    Returns:
        dict: The parsed YAML Data from src/config.yml
    """
    parsed_dict = yaml.load(open(get_path(name)), Loader=yaml.SafeLoader)
    return parsed_dict or {}

def nested_set(d: dict, keys: list, value) -> None:
    """Helps with editing a nested dictionary, see https://stackoverflow.com/a/13688108/14345173

    Args:
        d (dict): Input dictionary
        keys (list): List of keys for the path
        value (any): Value to set
    """
    
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value

def edit(name: str='config', path: Union[str, list]=None, to: str=None) -> None:
    """Edits the config

    Args:
        path (str/list): path for the keys to access/edit
        to (str): Value to edit it to
    """

    if isinstance(path, str):
        path = [path]

    source = load()
    nested_set(source, path, to)

    yaml.dump(data=source, stream=open(get_path(name), 'w'), indent=2)

def save(filename: str, source: dict):
    yaml.dump(data=source, stream=open(get_path(filename), 'w'), indent=2)

def set(filename: str, key, value=None):
    d = load(filename)
    d[key] = value
    save(filename, d)

def change(filename: str, key, value: int=0):
    d = load(filename)
    value = round(value, 1)

    if not load(filename).get(key): # key not found
        d[key] = value
    else:
        d[key] += value
        
    save(filename, d)

def var(string: str, dic: dict={}):
    """Replaces a string using a dict."""
    for key in dic.keys():
        string = string.replace('{' + str(key) + '}', str(dic[key]))
    return string

def lang(key: str, dic: dict={}):
    """Loads a language string, optionally with a replacer-dict used to insert variables."""
    text = load('lang').get(key)

    if isinstance(text, list):
        text = '\n'.join(text)

    return var(text, dic)

if __name__ == '__main__':
    print(load('ranks'))