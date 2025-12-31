import keyboard
import time

class autoTacetListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, uncrouch, keybind):
        
        def on_key(event):
            if event.name in keybind:
                print('running')
                time.sleep(0.05)
                keyboard.press_and_release('ctrl')
                time.sleep(0.05)
                keyboard.press_and_release('t')
                if uncrouch:
                    time.sleep(0.25)
                    keyboard.press_and_release('ctrl')
        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key)

    def run(self,keybind, uncrouch):
        print('checking')
        """Start the macro thread"""
        if not self.thread or not self.thread.is_alive():
            print('starting!!')
            self.running = True
            self.stack(keybind=keybind, uncrouch=uncrouch)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        """Stop the macro thread"""
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
