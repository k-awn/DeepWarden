import keyboard
import time

class RitualCastListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybinds, notes):
        allKeys = str(keybinds).split(',')
        allKeysConnected = ''.join(allKeys)
        allNotes = str(notes).split('|')
        print(allKeys)
        print(allNotes)

        def on_key(event):
            if event.name in allKeysConnected:
                for i in range(len(allKeys)):
                    if event.name == allKeys[i]:
                        note = allNotes[i]
                        note = str(note).split(',')
                        time.sleep(0.25)
                        keyboard.press_and_release(note[0])
                        for k in range((len(note) - 1)):
                            time.sleep(0.15)
                            keyboard.press_and_release(note[k+1])
        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key)

    def run(self,keybinds, notes):
        print('checking')
        """Start the macro thread"""
        if not self.thread or not self.thread.is_alive():
            print('starting!!')
            self.running = True
            self.stack(keybinds=keybinds, notes=notes)  # Just call stack directly
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
