# To install, add following lines two lines to ~/.bash_profile
# export DEV_INSTALL_FOLDER="/path/to/dev/folder" # must be absolute path!
# source "$DEV_INSTALL_FOLDER/dev.sh"

export DEV_INSTALL_FOLDER="/Users/aivant/Development/.dev/v2"
export DEV_ROOT_FOLDER="/Users/aivant/Development"

dev-setup() {
    # Call setup on dev.py
    output="$(python3 $DEV_INSTALL_FOLDER/dev.py --setup)"

    # Separate out last line of output. Log other lines
    logs=$(echo "$output" | sed '$d')
    cmd=$(echo "$output" | sed '$!d')

    if [[ ! -z "$logs" ]]; then
        echo "$logs"
    fi

    # Evaluate last line of python program
    eval "$cmd"
}

dev-setup

dev() {
    # Pass arguments to dev.py
    output="$(python3 $DEV_INSTALL_FOLDER/dev.py $@)"

    # Separate out last line of output. Log other lines
    logs=$(echo "$output" | sed '$d')
    cmd=$(echo "$output" | sed '$!d')

    if [[ ! -z "$logs" ]]; then
        echo "$logs"
    fi

    # Check for debug flag. Debug flag must always be first argument 
    if [[ $1 = "-d" ]]; then
        echo "[DEBUG] Executing command: '$cmd'"
    fi

    # Evaluate last line of python program
    eval "$cmd"
}