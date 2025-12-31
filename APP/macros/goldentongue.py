import keyboard
import time

class GoldenTongueListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind, content):
        def on_key(event):
            if event.name in keybind:
                time.sleep(0.05)
                keyboard.press_and_release('/')
                time.sleep(0.05)
                keyboard.write(content)
                time.sleep(0.05)
                keyboard.press_and_release('enter')  
        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key, suppress=True)

    def run(self,keybind, content):
        print('checking')
        """Start the macro thread"""
        if not self.thread or not self.thread.is_alive():
            print('starting!!')
            self.running = True
            self.stack(keybind=keybind, content=content)  # Just call stack directly
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
