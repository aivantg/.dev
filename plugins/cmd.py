# Plugin Docs: `cmd`
# setup func runs when terminal opens
# other functions take in arguments as an array
# functions return command for bash to run
import json
import os

DATA_PATH = os.getenv('DEV_INSTALL_FOLDER') + '/data/cd.json'
BASE_PATH = os.getenv('DEV_ROOT_FOLDER')

def _read_data():
    try: 
        with open(DATA_PATH, 'r') as f: 
            return json.load(f)
    except: 
        return {}

# Set up aliases on startup
def setup(): 
    aliases = _read_data()
    alias_string = ""
    for alias, cmd in aliases.items(): 
        alias_string += 'alias ' + alias + '="eval ' + cmd + '";'
    return alias_string[:-1] # remove final semicolon
    

# Create new alias
def mk(args): 
    aliases = _read_data()
    alias, cmd = args[0], " ".join(args[1:])
    aliases[alias] = cmd
    with open(DATA_PATH, 'w') as f: 
        json.dump(aliases, f)
    return 'alias ' + alias + '="eval ' + cmd + '"'

# List all aliases
def ls(args): 
    aliases = _read_data()
    print("\n---Current Command Aliases---\n")
    for alias, cmd in aliases.items(): 
        print(alias + " ---> " + cmd)
    print("\nAdd more with 'dev cmd:mk <alias> <cmd>'\nRemove with 'dev cmd:rm <alias>'\n")

# Remove an alias
def rm(args):
    aliases = _read_data()
    alias = args[0]
    if alias in aliases: 
        aliases.pop(alias)
        with open(DATA_PATH, 'w+') as f: 
            json.dump(aliases, f)
    else: 
        print("No aliases found matching pattern: '" + alias + "'")