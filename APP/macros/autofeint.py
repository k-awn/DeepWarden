import win32api, win32con, keyboard
import time
import threading

class autoFeintListener:  
    def __init__(self):
        self.running = False
        self.thread = None

    def stack(self):
        def is_mouse_swapped():
            return win32api.GetSystemMetrics(23) != 0
        def feintparry(*_): #ignores all arguments passed to it 
                if is_mouse_swapped():
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        time.sleep(0.05)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                else:
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                        time.sleep(0.05)
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        keyboard.on_press_key('f', feintparry)
        

    def run(self):
            """Start the macro thread"""
            if not self.thread or not self.thread.is_alive():
                print('starting!!')
                self.running = True
                self.thread = threading.Thread(target=self.stack)
                self.thread.daemon = True
                self.thread.start()
                

    def stop(self):
        """Stop the macro thread"""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)  # Wait up to 1 second for the thread to stop
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")

    def main(self):
        controller = autoFeintListener()
        controller.run()  # Changed from start() to run()
        
        try:
            # Keep the main thread alive
            while controller.running:  # Changed from self.running to controller.running
                keyboard.wait(1)
        except KeyboardInterrupt:
            controller.stop()

if __name__ == "__main__":
    auto_feint = autoFeintListener()
    auto_feint.main()