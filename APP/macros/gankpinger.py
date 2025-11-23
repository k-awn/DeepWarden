import keyboard
import time
import requests
import mss
import json
import os

class GankPingListener:  
    def __init__(self):
        self.running = False
        self.thread = None

    def stack(self, webhook_url, message, takeimage, username, avatar_url, hotkey):
        def send_discord_message(webhook_url, message, takeimage=False, username=None, avatar_url=None):
            """
            Send a Discord webhook message with optional image, username, and avatar_url
            
            Parameters:
                webhook_url (str): Discord webhook URL
                message (str): Message content
                takeimage (bool): Whether to take and attach a screenshot
                username (str, optional): Custom username for the webhook
                avatar_url (str, optional): HTTPS URL for the webhook avatar
            """
            # Prepare the payload
            payload = {
                "content": message,
                "username": username if username else None,
                "avatar_url": avatar_url if avatar_url else None
            }
            
            # Remove None values from payload
            payload = {k: v for k, v in payload.items() if v is not None}

            try:
                files = {}
                
                # Handle screenshot
                if takeimage:
                    abspath = os.path.dirname(os.path.abspath(__file__))
                    sspath = os.path.join(abspath, 'screenshot.png')
                    
                    try:
                        mss.mss().shot(output=sspath)
                        if os.path.exists(sspath):
                            with open(sspath, 'rb') as screenshot:
                                files['file'] = ('screenshot.png', screenshot.read(), 'image/png')
                    except Exception as e:
                        print(f"Error taking screenshot: {str(e)}")
                        return

                # Send request
                if files:
                    response = requests.post(
                        webhook_url,
                        data={'payload_json': json.dumps(payload)},
                        files=files
                    )
                else:
                    response = requests.post(
                        webhook_url,
                        json=payload
                    )
                
                if response.status_code in [200, 204]:
                    print("Message sent successfully!")
                else:
                    print(f"Failed to send message. Status code: {response.status_code}")
                    print(f"Response content: {response.text}")

            except Exception as e:
                print(f"Error sending message: {str(e)}")
            finally:
                # Clean up screenqshot if it exists
                if takeimage and os.path.exists(sspath):
                    try:
                        os.remove(sspath)
                    except Exception:
                        pass
        keyboard.add_hotkey(hotkey, lambda:send_discord_message(webhook_url=webhook_url, message=message, username=username if username else None, avatar_url=avatar_url if avatar_url else None, takeimage=takeimage), suppress=True)

    def run(self, webhook_url, message, username, avatar_url, takeimage, hotkey):
        print('checking')
        """Start the macro thread"""
        if not self.thread or not self.thread.is_alive():
            print('starting!!')
            self.running = True
            self.stack(webhook_url=webhook_url, hotkey=hotkey, message=message, username=username, avatar_url=avatar_url, takeimage=takeimage)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        """Stop the macro thread"""
        self.running = False
        keyboard.unhook_all()  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
