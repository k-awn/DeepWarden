import keyboard
import time
import pyautogui

class PerfectCastListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hook = None  # Added hook storage

    def code(self, keybinds):

        
        # Function to handle the actual mouse click
        def perform_click():
            time.sleep(0.1)
            pyautogui.click()
            print('h')
        
        # Function to handle key press events
        def on_key(event):
            allKeys = str(keybinds).split(',')
            allKeys = ''.join(allKeys)
            if event.name in allKeys:
                perform_click()
        
        # Register the key press handler and store the hook
        self.hook = keyboard.on_press(on_key)

    def run(self, keybinds):
        print('checking')
        """Start the macro thread"""
        if not self.thread or not self.thread.is_alive():
            print('starting!!')
            self.running = True
            self.code(keybinds=keybinds)  
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        """Stop the macro thread"""
        self.running = False
        if self.hook:  # Remove only this class's hook
            keyboard.unhook(self.hook)
            self.hook = None
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
