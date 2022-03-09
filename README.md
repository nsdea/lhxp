*`nsde/lhxp`*
# LHXP・Official "LH - Cyber Security" Discord Leveling-Bot
## Overview
**Contribuors:**
- [ONLIX aka. NSDE](https://github.com/nsde)
    - Lead/main developer, implementing all features as of right now and building the core with his old projects

- [LH - Cyber Security aka. Boss of Technic](https://github.com/luishuber3)
    - Planning & feedback

- [Raptor](https://github.com/raptor-007)
    - Planning & concept


### **Developement** (~2 months)
- **Alpha** (~1.5 months)
    - 28.11.2021-10.01.2022
    - Developement of the core features.

- **Beta** (~20 days)
    - 10.01.2022-31.01.2022 or sooner
    - Bot is (almost) ready to go live, a few bugs and improvements have to be made though.

- **Release**
    - 31.01.2022 or sooner
    - Bot is fully live and stable, ready to be used.

- **Future**
    - I won't be able to mainain the project forever, so one of the developers will have to work on it, which shouldn't be that much of a probem because everything is customizable and documented. 
    - As explained below, the *onlix.me*-API is going to be moved soon to another subdomain (*api.onlix.me*).
    - The project will probably be move to my archive [nsde-archive/LHXP](https://github.com/nsde-archive/lhxp) or moved to an organization.
    - Please keep the project and future open source and give credit to everyone who worked on it - not just me. Also, give the community the oppurtunity to contribute. 

### **Based on**
- [nsde/NOVΛLIX](https://github.com/nsde/novalix)[*](https://github.com/nsde-archive/novalix)
- [nsde/LHbot](https://github.com/nsde/lhbot)[*](https://github.com/nsde-archive/lhbot)

Repo not found? Click on the asterisk (`*`)!

### **Built with**
- [*`pycord`*](https://github.com/Pycord-Development/pycord)
- [*`onlix.me`* (selfmade) API ¹](https://onlix.me)

*¹) As eventually, the website and/or server will go offline or change its domain name, it has to be updated and changed to another domain and/or server.* 


![Cover](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FO_L9rqoMPUY%2Fmaxresdefault.jpg&f=1&nofb=1)

## Features
> **Warning:** This is not fully up to date!
### Code style/general
- Highly **configurable**!
    - Almost every single language string, XP reward value, channel/role and more can be edited.

- Using **slash commands** & **modern GUI** (buttons, menus, ...) API!

- Easily extendible!
    - **Helpers** allow a simple integration and implementation of new features.

- **Cog-Style**!
    - The bot's features are seperated in specific cogs/**extensions**, which can be reloaded one by one.

- Auto-**Backups**!
    - When the bot is started, every single config will get backed up in the `/backups`-directory. 

- **Real-time config**!
    - When the configuration is **edited**, changes will be applied in **realtime** to the bot.

- **Shell-tools**!
    - There are a lot of `.sh` files avaiable to be run in case of problems with the **installation**.

- **Colored logging**!
    - Problems and info will get printend coloured to the terminal for you to easily get the **overview** of how well the bot functions.

### Slash commands
The arrow (→) shows which cog the command is connected to.


- `/clearxp <@user>`
    - Requires admin permissions!
    - Purges all XP from a user.
    - → *admintools*

- `/setxp <@user> <level> <in-levels?>`
    - Requires admin permissions!
    - Sets the experience points or level of an user
    - → *admintools*

- `/changexp <@user> <level> <in-levels?>`
    - Requires admin permissions!
    - Changes the experience points or level of an user.
    - → *admintools*

- `/leaderboard`
    - Displays the users with the most levels in the server.
    - → *tools*

- `/info`
    - Displays an explanation of the leveling system.
    - → *info*

- `/xp <@user>`
    - Displays the XP and level of an user.
    - → *tools*

- `/thank <@user>`
    - Thanks some other user for helping with an issue, giving them quite some XP.
    - → *tools*

### Automatic events
- `Bump Detection`
    - Users who successfully `!d bump` get rewarded

- `Error Info`
    - The bot goes as far as **creating** and sending a **temporary website** for the traceback to be read. 

- `Anti Spam`
    - To see how it works, click here: [[src/cogs/helpers/spam.py](src/cogs/helpers/spam.py)

- `XP Gaining`
    - Allows users to level up in realtime

- `Rank Check`
    - Allows users to obtain new ranks by achieving a higher level. Too see, which levels you need, click here: [[src/ranks.yml](src/ranks.yml)

## Installation

### Setup
> Make sure to run the code from THIS directory `/` NOT `/src`.

Rename `dotenv_template.txt` to `.env` and replace the values. Keep them secret! You may want to contact the team if you're unsure what to put in there.

### Install
```bash
./dependencies.sh
./packages.sh

# or

sh dependencies.sh
sh packages.sh
```

### Run

Normal

```bash
py src/bot.py # Windows
python src/bot.py # or (don't run this on Linux as it could start Python 2!)
python3 src/bot.py # Linux (recommended)
```

Screen

```bash
screen -S LHXP python3/bot.py # open a screen named "LHXP" with the command "python3 src/bot.py"
```

Issues?

```bash
/usr/bin/python3 src/bot.py # or
/usr/bin/python3.9 src/bot.py # replace 3.9 with your Python version
```

### Fix package warnings

> **Warning:** Experimental!

```bash
./experimental.sh
```

### Developement mode
The bot is automatically entering the development mode when the computer name matches on of the names listed in `config.yml` in `dev-names`. Feel free to enter *your* machine/PC name in there!

### Invite the bot
Is is really important that you check/enable the `bot` AND `application.commands` scope!

### Slash commands not working?
Kick the bot and re-invite it. Another experimental way is to do the following:

1. Re-name `src/fix.sh` to `src/.fix.sh` and replace `BOT_TOKEN` and `BOT_ID` with your values.
> **Warning:** The renaming is important for the `.gitignor`-config to notice that this file should not be uploaded to the public!
2. Run `sh src/.fix.sh` 

## Settings
### Configuration
Don't configure the files stored in `/backups`! The code just looks for the *actual* (config) files, not the backed up ones.

> **Warning:** This - as well - isn't fully updated.

- **`colors.yml`** [src/colors.yml](src/colors.yml)
    - Color codes in the format `0xFFFFFF`

        ```yml
        color-primary: 0x7289DA # blurple
        color-error: 0xFF0000 # red
        color-warn: 0xFFFF00 # yellow
        color-ok: 0x00FF00 # green
        ...
        ```
    
    - Use in Python code

        ```py
        # don't forget to import the helpers you need!
        from .helpers import management
        
        # primary color
        management.color() # returns a <discord.Color> Object

        # all other colors can be read directly from the file
        management.color('error') # returns a <discord.Color> Object

        # implementation in embeds
        embed = discord.Embed(..., color=management.color('warn'))

        ```


- **`config.yml`** [src/config.yml](src/config.yml)
    - General bot configuration, such as *playing ...*-Status

        ```yml
        # some boring examples to learn how YAML/yml works
        text: Lorem # or
        text2: "Ipsum"
         
        hungry: true
        hungary: false
        
        food: [apple, banana]
        food-count: 123
        ```

    - Implementation in the Python code
        ```py
        # don't forget to import the helpers you need!
        from .helpers import config

        # use config.yml
        config.load()['food']

        # use other .yml-configs
        config.load('ranks')[0]

        ```

- **`lang.yml`** [[src/lang.yml](src/lang.yml)
        ```yml
        # basic strings
        key: value # or
        key2: "value2" # doesn't matter

        # use lists for new lines
        long-key:
            - "Lorem ipsum"
            - ""
            - "Discord formatting **works**"
            - "💬 Emojis work, too"
            - "" are not needed, but recommended
            ...

        # use variables (works with lists, too)
        xp: {user} has {xp} XP. # see below
        ```

    - Use language strings in the Python code:
        ```py
        # don't forget to import the helpers you need!
        from .helpers import config

        # basic strings
        config.lang('key')

        # lists with newlines
        config.lang('long-key') # works the same, newlines are automatically put together with \n, returns a string

        # variables
        config.lang('xp', {'user': user.name, 'xp': xp.of(user)}) # pretty easy, huh?

        ```

- **`ranks.yml`** [[src/ranks.yml](src/ranks.yml)
    - Implementation in the Python code is shown above, see `config.yml`.

### Auto-Generated
> **Critical WARNING:** **Do not change files these if you are unsure what you're doing!**

**The code blocks just show examples, not the actual content!**

The following files are being managed automatically by the code.

- **`dailystep.yml`** [src/dailies.yml](src/dailies.yml)
    - On how many days a user has written at least one message in the month. 

        ```yml
        
        # user (id/int): step (int)
        338711554683830292: 2
        657900196189044736: 4
        ...
        ```

- **`helperreward.yml`** [src/helperreward.yml](src/helperreward.yml)
    - Last date (unix timestamp) of when someone thanked (`/thank` [in German]) some other person for helping them.

        ```yml
        
        # user (id/int): timestamp (unix/int)
        338711554683830292: 1641244836.794864
        657900196189044736: 1641476016.8825243
        ...
        ```

- **`invitedby.yml`** [src/invitedby.yml](src/invitedby.yml)
    - Who invited someone?
    
        ```yml
        # user who invited (id/int): user who got invited (id/int)
        338711554683830292: 1641244836.794864
        ...
        ``` 

- **`inviteowners.yml`** [src/inviteowners.yml](src/inviteowners.yml)
    - Who created this invite?
    
        ```yml
        # invite (id/str): user (id/str)
        qu74zH4Wv3: 657900196189044736
        XyHhzz33Na: 657900196189044736
        ...
        ```

- **`invites.yml`** [src/invites.yml](src/invites.yml)
    - How many invite-uses has this user?
    
        ```yml
        # user (id/str): count (int)
        657900196189044736: 11
        ...
        ```

- **`lastmessage.yml`** [src/lastmessage.yml](src/lastmessage.yml)
    - When wrote this user the last message?
    
        ```yml
        # user (id/str): count (unix/int)
        657900196189044736: 1641244836.794864
        ...

- **`times.yml`** [src/times.yml](src/times.yml)
    - When happened XY?

        ```yml
        # key: timestamp (unix/int)
        xp-reset: 1641244836.794864
        ...
        ```

- **`xp.yml`** [src/xp.yml](src/xp.yml)
    - XP points of all users

        ```yml
        # user (id/str): xp count (int)
        657900196189044736: 11 # not in levels!
        ```

    - Use in Python code

        ```py
        # don't forget to import the helpers you need!
        from .helpers import xp

        xp.of(657900196189044736) # 11

        xp.level_of(657900196189044736) # 3

        xp.add(657900196189044736, 999)
        
        # instead of the user ID,
        # you can also use a <discord.Member> or <discord.User>
        xp.of(ctx.author)

        ```
