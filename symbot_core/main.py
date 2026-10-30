
import threading
import time
from symbot_core.memory.long_term import SymbioticMemory
from symbot_core.perception.os_perception import OSPerception
from symbot_core.audition.voice_engine import VoiceEngine
from symbot_core.voice.voice_output import VoiceOutput
from symbot_core.presence.ghost_ui import GhostUI
from PyQt5.QtWidgets import QApplication

class Symbot:
    def __init__(self):
        # Initialize Core Components
        self.memory = SymbioticMemory()
        self.perception = OSPerception()
        self.audition = VoiceEngine()
        self.voice = VoiceOutput()
        
        # Start Perception Thread
        self.perception.start()
        
        # UI Setup (Must be in main thread)
        self.app = QApplication([])
        self.ui = GhostUI()

    def handle_voice_input(self, text, emotion):
        print(f"User said: {text} ({emotion})")
        self.memory.save_fact(f"User said {text}", category="speech")
        
        # Reason based on input + context
        context = self.perception.get_current_context()
        response = self.think(text, emotion, context)
        
        self.ui.update_status("Speaking...")
        self.voice.speak(response, emotion)
        time.sleep(2)
        self.ui.hide_status()

    def think(self, text, emotion, context):
        # Integration of Memory + Perception + Audition
        if "help" in text.lower():
            return "I'm here. I see you are in " + context["active_window"] + ". How can I assist?"
        if emotion == "Negative/Stressed":
            return "You sound a bit stressed. Let's tackle this one step at a time."
        return "I've noted that. Your memory is updated."

    def proactive_loop(self):
        while True:
            context = self.perception.get_current_context()
            # Proactive reasoning
            if "Error" in context["clipboard"]:
                self.ui.update_status("Error Detected!")
                self.voice.speak("I noticed an error in your clipboard. Want me to fix it?", "Neutral")
            time.sleep(10)

    def run(self):
        # Start Proactive Thread
        threading.Thread(target=self.proactive_loop, daemon=True).start()
        # Start Audition Thread
        threading.Thread(target=self.audition.start_listening_loop, args=(self.handle_voice_input,), daemon=True).start()
        
        print("🚀 SYMBOT fully operational. Standing by...")
        self.app.exec_()

if __name__ == "__main__":
    bot = Symbot()
    bot.run()
