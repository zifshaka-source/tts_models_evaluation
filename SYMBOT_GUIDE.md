
# 🤖 Symbot: The Non-Traditional AI Companion Guide

## Overview
Symbot is not a chatbot; it is a **symbiotic agent**. It operates via a continuous "Inner Monologue" that allows it to be proactive, multimodal, and context-aware.

## 🏗️ Architecture
1. **Perception Layer:** Monitors active windows and clipboard in real-time.
2. **Audition Layer:** VAD-triggered listening with emotional sentiment analysis.
3. **Cognitive Layer:** Uses a persistent knowledge graph for long-term memory.
4. **Presence Layer:** A transparent "Ghost UI" that overlays the OS.
5. **Voice Layer:** Emotion-aware TTS (ElevenLabs/Orpheus) that adjusts tone.

## 🚀 Deployment Instructions
1. **Install Dependencies:**
   ```bash
   pip install -r symbot_requirements.txt
   ```
2. **Setup API Keys:** Add your ElevenLabs/OpenAI keys in `symbot_core/voice/voice_output.py`.
3. **Launch:**
   ```bash
   python symbot_core/main.py
   ```

## 🌟 Unique Symbot Behaviors
- **Proactive Intervention:** The bot will interrupt you if it detects a crash in your IDE or a meeting starting on your calendar.
- **Emotional Mirroring:** The bot changes its voice stability and pitch based on your detected stress levels.
- **Digital Twin Memory:** It remembers your coding style, your preferences, and your relational network.
