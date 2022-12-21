# Plugin Docs: `env`
# setup func runs when terminal opens
# other functions take in arguments as an array
# functions return command for bash to run
import json
import os

DATA_PATH = os.getenv('DEV_INSTALL_FOLDER') + '/data/cd.json'

def _read_data():
    try: 
        with open(DATA_PATH, 'r') as f: 
            return json.load(f)
    except: 
        return {}

# Set up environment variables on startup
def setup(): 
    vars = _read_data()
    vars_string = ""
    for var, val in vars.items(): 
        vars_string += 'export "' + var + '=' + val + '";'
    return vars_string[:-1] # remove final semicolon
    

# Create new env var
def mk(args): 
    vars = _read_data()
    var, val = args[0], " ".join(args[1:])
    vars[var] = val
    with open(DATA_PATH, 'w') as f: 
        json.dump(vars, f)
    return 'export "' + var + '=' + val + '"'

# List all aliases
def ls(args): 
    vars = _read_data()
    print("\n---Current Dev Environment Variables---\n")
    for var, val in vars.items(): 
        print(var + " ---> " + val)
    print("\nAdd more with 'dev env:mk <var> <val>'\nRemove with 'dev env:rm <var>'\n")

# Remove an alias
def rm(args):
    vars = _read_data()
    var = args[0]
    if var in vars: 
        vars.pop(var)
        with open(DATA_PATH, 'w+') as f: 
            json.dump(vars, f)
        return 'export "' + var + '="'
    else: 
        print("No dev environment variables found matching pattern: '" + var + "'")