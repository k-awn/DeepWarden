import os
import time
import cv2
import numpy as np
import mss
import keyboard

# --- CONSTANTS ---
DETECTION_THRESHOLD = 0.85
MAX_SCAN_ATTEMPTS = 3
SCAN_TIMEOUT = 1
DEFAULTPING = 100

# Region Definitions
LETTER_REGIONS = [
    {"left": 835, "top": 250, "width": 50, "height": 50}, 
    {"left": 835, "top": 300, "width": 50, "height": 50}, 
    {"left": 935, "top": 250, "width": 50, "height": 50},
    {"left": 935, "top": 300, "width": 50, "height": 50},
    {"left": 1035, "top": 250, "width": 50, "height": 50},
    {"left": 1035, "top": 300, "width": 50, "height": 50},
    {"left": 1135, "top": 250, "width": 50, "height": 50},
    {"left": 1135, "top": 300, "width": 50, "height": 50},
]

class RitualCastListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.templates = {}
        self.images = [None] * len(LETTER_REGIONS)

    def load_templates(self, filepath):
        """Loads images from the template folder."""
        if not os.path.isdir(filepath):
            print(f"ERROR: Template folder not found at: {filepath}")
            return False

        count = 0
        for f in os.listdir(filepath):
            if not f.endswith('.png') or f == 'background.png':
                continue
            
            # Extract letter from filename
            name = os.path.splitext(f)[0]
            char = None
            for c in reversed(name):
                if c.isalpha():
                    char = c.upper()
                    break
            
            if char:
                path = os.path.join(filepath, f)
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    self.templates[char] = img
                    count += 1
        
        if count == 0:
            print("ERROR: No .png templates found!")
            return False
        
        print(f"Loaded {count} templates.")
        return True

    def grab_regions(self, sct):
        """Takes screenshots of each region in letter_region, returns list"""
        for i, roi in enumerate(LETTER_REGIONS):
            img = np.array(sct.grab(roi))
            
            # Drop alpha channel if present
            if img.ndim == 3 and img.shape[2] == 4:
                img = img[:, :, :3]
                
            self.images[i] = img

    def detect_letter(self, region_img, template_list):
        """Finds the best matching letter in a single region."""
        best_letter = None
        best_score = 0.0
        
        region_gray = cv2.cvtColor(region_img, cv2.COLOR_BGR2GRAY)

        if np.mean(region_gray) < 10: 
            return None, 0.0

        for letter, template in template_list:
            if template.shape[0] > region_gray.shape[0] or template.shape[1] > region_gray.shape[1]:
                continue

            res = cv2.matchTemplate(region_gray, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(res)

            if max_val > 0.98:
                return letter, max_val
            
            if max_val > best_score and max_val >= DETECTION_THRESHOLD:
                best_score = max_val
                best_letter = letter

        return best_letter, best_score

    def scan_until_found(self, sct, template_list):
        """Scans all regions until valid letters are found for all columns."""
        detected = [None] * len(LETTER_REGIONS)
        start_time = time.time()
        attempts = 0

        while attempts < MAX_SCAN_ATTEMPTS and (time.time() - start_time) < SCAN_TIMEOUT:
            if not self.running: 
                break
            
            self.grab_regions(sct)
            for i, img in enumerate(self.images):
                if detected[i] is None:
                    letter, score = self.detect_letter(img, template_list)
                    if letter:
                        detected[i] = letter

            columns_satisfied = True
            for col in range(4):
                topRow, bottomRow = col * 2, col * 2 + 1
                if detected[bottomRow] is None and detected[topRow] is None:
                    columns_satisfied = False
                    break
            
            if columns_satisfied:
                break
                
            attempts += 1
            time.sleep(0.005)
            
        return detected

    def perform_macro_cycle(self, sct, template_list, ping_ms):
        """Runs one cycle of detection and typing."""
        detected = self.scan_until_found(sct, template_list)
        sequence = [d for d in detected if d is not None]

        if sequence:
            print(f"Detected: {''.join(sequence)}")
            
            final_seq = []
            for char in sequence:
                c = char.upper()
                final_seq.append(c)

            key_delay = 0.01 + (int(ping_ms) * 0.001)
            for k in final_seq:
                time.sleep(key_delay)
                keyboard.press_and_release(k.lower())
            time.sleep(0.1)
        
        time.sleep(0.001)

    def stack(self, ping_ms, filepath):
        """Main execution logic"""
        print(f"Ping: {ping_ms}ms")
        
        if not self.load_templates(filepath):
            self.running = False
            return

        # Initialize Screen Capture
        with mss.mss() as sct:
            template_list = list(self.templates.items())

            # Main Loop
            while self.running:
                try:
                    self.perform_macro_cycle(sct, template_list, ping_ms)
                except Exception as e:
                    print(f"Unhandled runtime error: {e}")
                    time.sleep(0.1)

    def run(self, filepath, ping_ms):
        if ping_ms is None or not str(ping_ms).isdigit():
            ping_ms = DEFAULTPING # if field is empty it inputs '' so ping_ms = 100 doesnt work
        print('checking')
        """Start the macro thread"""
        if not self.thread or not self.thread.is_alive():
            print('starting!!')
            self.running = True
            self.stack(ping_ms, filepath)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        """Stop the macro thread"""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")