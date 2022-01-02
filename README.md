# LHXP・Official "LH - Cyber Security" Discord Leveling-Bot
Based on [nsde/NOVΛLIX](https://github.com/nsde/novalix)

![Cover](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FO_L9rqoMPUY%2Fmaxresdefault.jpg&f=1&nofb=1)

## Feature Overview
- `/clear <@user>`
    - Requires admin permission
    - Purges all XP from a user

- `/setxp <@user> <level> <in-levels?>`
    - Requires admin permission
    - Sets the experience points or level of an user

- `/change <@user> <level> <in-levels?>`
    - Requires admin permission
    - Changes the experience points or level of an user

- `/leaderboard`
    - Displays the users with the most levels in the server

- `/info`
    - Displays an explanation of the leveling system

- `/user <@user>`
    - Displays the XP and level of an user

## Installation

### Setup
> Make sure to run the code from THIS directory `/` NOT `/src`.

### Install
```bash
./dependencies.sh
./packages.sh
```

### Run

```bash
sh src/.fix.sh
python3 src/bot.py
```

### Fix package warnings

> **Warning:** Experimental!

```bash
./experimental.sh
```

## Settings
### Configuration
- **`colors.yml`** » Color codes for the bot in the format `0xFFFFFF`
- **`config.yml`** » General bot configuration, such as *playing ...*-Status
- **`language.yml`** » Translations for the bot (all texts)
- **`roles.yml`** » Role configuration for rewards etc.

### Auto-Generated
**Do not change these if you are unsure what you're doing!**

The following files are being managed automatically and should be backuped (manually).

- **`helperreward.yml`** » Last date (unix timestamp) of when someone thanked (`/helfer` [in German]) some other person for helping them.
- **`xp.yml`** » XP points of all users