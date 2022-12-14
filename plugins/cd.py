# Plugin Docs: `cd`
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

# Loop through arguments and build cd string, expanding aliases
def cd(args):
    aliases = _read_data()
    cd_string = "cd " + BASE_PATH
    for arg in args: 
        if arg in aliases:
            cd_string += "/" + aliases[arg]
        else:
            cd_string += "/" + arg
    return cd_string

# Create new alias
def mk(args): 
    aliases = _read_data()
    alias, folder = args[0], args[1]
    aliases[alias] = folder
    with open(DATA_PATH, 'w') as f: 
        json.dump(aliases, f)

# List all aliases
def ls(args): 
    aliases = _read_data()
    print("\n---Current Aliases---\n")
    for alias, folder in aliases.items(): 
        print(alias + " ---> " + folder)
    print("\nAdd more with 'dev cd:mk <alias> <path>'\nRemove with 'dev cd:rm <alias>'\n")

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