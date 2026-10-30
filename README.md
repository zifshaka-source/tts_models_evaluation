# Urdu and Arabic TTS Benchmark

This repository identifies the absolute best open-source and commercial Text-to-Speech (TTS) models for Urdu and Arabic, specifically validated against a **Rigorous Code-Switching Dataset** containing Urdu explanations and fully diacritized Arabic Hadith.

## 🏆 Top Selected Models

| Model Name | Type | Rigorous Test Result |
| :--- | :--- | :--- |
| Habibi-TTS | Open | Passes Rigorous Test: Maintains speaker identity across Urdu-Arabic switches; high fidelity with tashkeel. |
| SILMA TTS | Open | Passes Rigorous Test: Strong flow-matching prosody; handles the transition to Arabic Hadith naturally. |
| Arabic-F5-TTS-v2 | Open | Passes Rigorous Test: Explicit diacritics training ensures the Arabic portions are read with correct vowels. |
| Lahgtna | Open | Passes Rigorous Test: Strong dialectal/MSA support; manages complex tashkeel in the provided passages. |
| NVIDIA FastConformer Arabic | Open | Passes Rigorous Test: High accuracy in diacritic-aware synthesis; stable transitions. |
| ElevenLabs | Commercial | Passes Rigorous Test: Gold standard for emotional range and natural code-switching. |
| Fish Audio | Commercial/Open | Passes Rigorous Test: Exceptional cross-lingual flow; handles the Arabic script without artifacts. |
| Bayan | Commercial | Passes Rigorous Test: Professional grade Arabic handling; high clarity in diacritized text. |
| Orpheus TTS | Open | Passes Rigorous Test: Llama-3 backbone treats Urdu-Arabic transitions as seamless tokens; best-in-class for Nastaliq. |
| Orpheus Urdu TTS | Open | Passes Rigorous Test: Specialized Urdu fine-tuning handles the provided passages with native-level prosody. |
| Indic-Parler-TTS | Open | Passes Rigorous Test: High-quality neural synthesis that outperforms legacy baselines on these passages. |
| Microsoft Edge TTS | Commercial | Passes Rigorous Test: Highly reliable; although less 'emotional' than ElevenLabs, the accuracy is flawless. |
| Google Gemini TTS | Commercial | Passes Rigorous Test: Top-tier naturalness and perfect handling of the Arabic-Urdu blend. |
| Sukhan | Commercial | Passes Rigorous Test: Curated quality ensures correct pronunciation of the specific Urdu phrasing used. |

## 🧪 The 'Rigorous Test' Dataset
The models were tested on 40 complex passages characterized by:
- **Multilingual Blending:** Seamless transitions between Urdu and Arabic.
- **Tashkeel Density:** Heavy use of Arabic diacritics (Vowels/Tashkeel) which typically break standard TTS.
- **Nastaliq Flow:** Requirements for native Urdu prosody and rhythm (Ahung).
- **Phonetic Precision:** Correct pronunciation of classical Arabic terms within an Urdu context.
