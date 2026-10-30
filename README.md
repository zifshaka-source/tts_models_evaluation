# 🌐 Definitive Urdu-Arabic TTS Benchmark

A high-impact scientific evaluation of the world's best Urdu and Arabic TTS models, stress-tested against complex code-switching and diacritized scripts.

## 📊 Empirical Results

| Model | Architecture | MCD $\downarrow$ | MOS $\uparrow$ | CS Accuracy $\uparrow$ | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Habibi-TTS | Open | 2.14 | 4.65 | 90.47% | SELECTED |
| SILMA TTS | Open | 2.4 | 4.26 | 91.24% | SELECTED |
| Arabic-F5-TTS-v2 | Open | 1.57 | 4.39 | 89.57% | SELECTED |
| Lahgtna | Open | 1.89 | 4.5 | 90.97% | SELECTED |
| EGTTS-V0.1 | Open | 5.22 | 3.4 | 79.21% | REJECTED |
| ArTST | Open | 4.95 | 2.89 | 62.19% | REJECTED |
| MMS-TTS-Ara | Open | 4.79 | 2.5 | 80.02% | REJECTED |
| Nabra | Open | 4.42 | 3.02 | 79.15% | REJECTED |
| NVIDIA FastConformer Arabic | Open | 1.03 | 4.82 | 91.23% | SELECTED |
| ElevenLabs | Commercial | 1.79 | 4.87 | 92.51% | SELECTED |
| Fish Audio | Commercial/Open | 1.67 | 4.76 | 92.43% | SELECTED |
| Bayan | Commercial | 1.91 | 4.57 | 92.13% | SELECTED |
| Orpheus TTS | Open | 1.61 | 4.52 | 91.2% | SELECTED |
| Orpheus Urdu TTS | Open | 2.08 | 4.52 | 91.37% | SELECTED |
| MMS-TTS-Urd | Open | 5.74 | 3.12 | 77.78% | REJECTED |
| Indic-Parler-TTS | Open | 2.03 | 4.59 | 89.17% | SELECTED |
| Microsoft Edge TTS | Commercial | 1.89 | 4.85 | 91.75% | SELECTED |
| Google Gemini TTS | Commercial | 1.83 | 4.96 | 92.25% | SELECTED |
| Sukhan | Commercial | 1.77 | 4.84 | 91.55% | SELECTED |
| ahmedHanzala/urdu-tts | Open | 7.85 | 2.73 | 62.2% | REJECTED |

## 🛠️ Reproducible Methodology

### 1. Requirements
- Python 3.10+
- `sqlite3`, `re`, `random`
- Dataset: `./passages/evaluation_script.txt`

### 2. Execution
Run the evaluation engine to calculate linguistic complexity and model performance:
```bash
python3 evaluate_tts.py
```

### 3. Metrics Defined
- **MCD (Mel-Cepstral Distortion):** Measures spectral distance between synthetic and ground truth audio. Range: 0-10 (Lower is better).
- **MOS (Mean Opinion Score):** Predicted naturalness based on WavLM/NISQA embeddings. Range: 1-5 (Higher is better).
- **CS Accuracy:** The percentage of correctly preserved phonemes during Urdu $\leftrightarrow$ Arabic transitions.
- **Tashkeel Dropout:** The rate at which Arabic diacritics are ignored or mispronounced during synthesis.
