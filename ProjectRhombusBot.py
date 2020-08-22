import pyautogui
from pynput.keyboard import Key, Controller, Listener

def on_press(key):
    if key == Key.enter or key == Key.space:
        pyautogui.press('w')
        listener.stop()

def is_arrow(pixel_color):
    # If pixel_color is the color of:
    #             Expert's white arrow    or                blue arrow
    return (pixel_color == (253, 250, 241) or pixel_color == (143, 139, 252)
    #   or          Hard's white arrow    or                 blue arrow
        or pixel_color == (253, 253, 253) or pixel_color == (40, 152, 253)
    #   or        Normal's yellow arrow  or                 blue arrow
        or pixel_color == (253, 253, 19) or pixel_color == (0, 223, 253)
    #   or          Easy's yellow arrow  or                 blue arrow.
        or pixel_color == (248, 217, 73) or pixel_color == (81, 132, 253))

if __name__ == '__main__':
    pyautogui.FAILSAFE = False # Fixes an unwanted process termination when the
                               # user drags their mouse to the lower-right corner
                               # of the screen while the process is running.

    try: # Exits cleanly if the user ever enters Control-C.
        # Prints some instructions for the user.
        print('The bot is now running, switch to Project Rhombus and play in fullscreen mode on any difficulty')
        print('If Project Rhombus starts dropping frames (lagging), simply Alt-Tab out and back in to fix')
        print('When you close the game, please also terminate this process by entering Control-C in the console')

        listener = Listener(
            on_press=on_press)
        listener.start()

        prev_input = 'w' # prev_input keeps track of the previous keyboard input.
                         # See README for more info on why this is needed.

        while True:
            if prev_input != 'w': # If the previous keyboard input wasn't 'w'.
                pixel_color = pyautogui.pixel(960, 375) # Color of the pixel
                                                        # that is 165 pixels
                                                        # above center.
                # If the pixel color is that of an arrow:
                if is_arrow(pixel_color):
                    pyautogui.press('w') # Hits the 'w' key.
                    prev_input = 'w'
            
            if prev_input != 'a': # If the previous keyboard input wasn't 'a'.
                pixel_color = pyautogui.pixel(795, 540) # Color of the pixel
                                                        # that is 165 pixels
                                                        # to the left of center.
                # If the pixel color is that of an arrow:
                if is_arrow(pixel_color):
                    pyautogui.press('a') # Hits the 'a' key.
                    prev_input = 'a'
            
            if prev_input != 's': # If the previous keyboard input wasn't 's'.
                pixel_color = pyautogui.pixel(960, 705) # Color of the pixel
                                                        # that is 165 pixels
                                                        # below center.
                # If the pixel color is that of an arrow:
                if is_arrow(pixel_color):
                    pyautogui.press('s') # Hits the 's' key.
                    prev_input = 's'
            
            if prev_input != 'd': # If the previous keyboard input wasn't 'd'.
                pixel_color = pyautogui.pixel(1125, 540) # Color of the pixel
                                                         # that is 165 pixels
                                                         # to the right of center.
                # If the pixel color is that of an arrow:
                if is_arrow(pixel_color):
                    pyautogui.press('d') # Hits the 'd' key.
                    prev_input = 'd'

    except KeyboardInterrupt: # Exits cleanly if the user ever enters Control-C.
        listener.stop()
        print('The process has terminated due to Control-C input.')
