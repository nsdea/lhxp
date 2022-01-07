try:
    from . import config
except ImportError:
    import config
    
import socket
import discord
import datetime

def testing_mode() -> bool:
    """Returns whether the test mode is enabled based on the host system name.

    Returns:
        bool: Test mode enabled?
    """
    return socket.gethostname() in config.load()['dev-names']

def color(style: str='primary') -> discord.Color:
    """Returns a color from the config.^

    Args:
        style (str, optional): style name from the config. Defaults to 'primary'.

    Returns:
        discord.Color: the requested color
    """
    return discord.Color(config.load('colors')[f'color-{style}'])

start_timestamp = None

def set_start_time() -> None:
    """Sets the bot start timestamp to the current time (as a datetime.datetime object).
    """
    global start_timestamp
    start_timestamp = datetime.datetime.now()

def get_start_time() -> datetime.datetime:
    """Returns the time the bot started at.

    Returns:
        datetime.datetime: Start Timestamp
    """
    global start_timestamp
    return start_timestamp