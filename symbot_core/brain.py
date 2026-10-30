
import time
import threading
from symbot_core.memory.long_term import SymbioticMemory # Assume split into file
from symbot_core.perception.os_perception import OSPerception

class SymbotBrain:
    def __init__(self):
        self.memory = SymbioticMemory()
        self.perception = OSPerception()
        self.is_running = True
        self.state = "IDLE"
        
        # Start Perception
        self.perception.start()

    def think(self, context):
        window = context.get("active_window", "")
        clipboard = context.get("clipboard", "")
        
        print(f"[Inner Monologue]: Observing {window} | Clipboard: {clipboard[:30]}...")
        
        # PROACTIVE LOGIC 1: Coding Assistance
        if "Visual Studio Code" in window or "PyCharm" in window:
            if "Error" in clipboard or "Exception" in clipboard:
                return "I see a stack trace in your clipboard. Should I analyze this error for you?"
        
        # PROACTIVE LOGIC 2: Research Support
        if "Chrome" in window or "Firefox" in window:
            if "TTS" in window or "Speech Synthesis" in window:
                return "You're researching TTS again. Want me to pull up the DAPA benchmark results?"
        
        # PROACTIVE LOGIC 3: Memory-Based Intervention
        user_name = self.memory.data["user_profile"].get("name", "User")
        if "Calendar" in window:
            return f"Hey {user_name}, I noticed your next meeting is in 10 minutes. Should I prepare the notes?"

        return None

    def act(self, decision):
        if decision:
            print(f"\n🤖 SYMBOT INTERVENTION: {decision}\n")

    def run_loop(self):
        while self.is_running:
            context = self.perception.get_current_context()
            decision = self.think(context)
            if decision:
                self.act(decision)
            time.sleep(5)

if __name__ == "__main__":
    bot = SymbotBrain()
    bot.run_loop()
