import sys, os
from inspect import signature
import plugins

def import_plugin(name): 
    __import__(f"plugins.{name}")
    return getattr(plugins, name)

def get_all_commands(plugin): 
    return [func for func in dir(plugin) if callable(getattr(plugin, func)) and not func.startswith('__')]

# Load plugins from local plugins folder
dir_path = os.path.dirname(os.path.realpath(__file__))
available_plugins = [m[:-3] for m in os.listdir(path=f"{dir_path}/plugins") if m.endswith('.py') and not m.startswith('__')]

# No arguments, default action is to cd to dev folder
if len(sys.argv) <= 1: 
    print("cd $DEV_ROOT_FOLDER")
    quit()
        

# Setup mode, call 'setup' command on all plugins if available
if sys.argv[1] == "--setup": 
    setup_cmd = ""
    for plugin_name in available_plugins: 
        plugin = import_plugin(plugin_name)
        try: 
            result = plugin.setup()
            if result: 
                setup_cmd += result + ";"
        except: 
            pass
    print(setup_cmd[:-1])
    quit()


# Check to see if user specified plugin, format is: "plugin:app"
# Defaults to `cd:cd` command
if ":" in sys.argv[1]: 
    plugin_name, plugin_cmd = tuple(sys.argv[1].split(':'))
    args = sys.argv[2:]
else: 
    plugin_name, plugin_cmd = 'cd', 'cd'
    args = sys.argv[1:]

# If debug flag exists, remove it. Not currently passing it on 
try: 
    args.remove('-d')
except: 
    pass

# Run plugin with arguments. Print return value as last line of script, to be run by original shell
if plugin_name in available_plugins: 
    plugin = import_plugin(plugin_name)
    available_commands = get_all_commands(plugin)

    if plugin_cmd in available_commands: 
        cmd_func = getattr(plugin, plugin_cmd)
        if len(signature(cmd_func).parameters) == 0: 
            result = cmd_func()
        else: 
            result = cmd_func(args)

        if result is None: 
            print(':')
        else: 
            print(result) if result is not None else print(':')
    else: 
        print(f'ERROR: Could not find `{plugin_cmd}` in plugin `{plugin_name}`')
        print(f"Available commands: {available_commands}")
        print(':') 
else: 
    print(f'ERROR: Could not find plugin `{plugin_name}`')
    print(f"Available plugins: {available_plugins}")
    print(':') 


