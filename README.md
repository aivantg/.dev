# .dev

A lightweight terminal app that helps you move around your terminal faster!

The app is based around plugins, and has three built-in.

## Setup

1. Clone the repo, and choose a folder to install the applet in.
2. Update `dev.sh` with the absolute path to the install folder.
3. Update `dev.sh` with the path to your desired development folder
4. Add `source path/to/dev.sh` to your `.bash_profile` or `.zshrc`

## Adding plugins

1. Create a new file called <plugin_name>.py to the plugins folder.
2. Write your plugin. All functions in the plugin file will be available through `dev <plugin_name>:<function_name>`. Each function takes in an `args` param that is an array of all args passed into the command separated by spaces. The function can return a string, if it does, the original terminal window that called the dev command will evaluate that string _in_ that terminal. This allows you, for example, to change the working directory of the original terminal, by returning the string "cd ~/.ssh" for example. Multiple commands can be run by chaining them together on one line. Look at bash syntax for more info.
3. The `setup()` function is a special function that runs when the dev script first loads (when the terminal opens). It can also return a string to be evaluated on setup. This is useful for setting something up for every new terminal session.
4. For good practice, I recommend you name any helper functions with an underscore at the start. It's also recommended to use the `/data` folder for any information you need to store, naming files as the same name as your plugin.
5. Feel free to submit a pull request with your plugin if you feel like it could be useful to more people!

## Plugin Docs

The dev script comes built-in with three plugins. They're explained below.

### `cd`

### `env`

### `cmd`

## Dev Notes

- passing the `-d` flag to the script will have the script print out the bash command being run by the terminal
