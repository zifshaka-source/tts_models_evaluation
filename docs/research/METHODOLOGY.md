
# 🔬 The DAPA Approach: Diacritic-Aware Phoneme Alignment

## The Problem with Standard Benchmarks
Most TTS benchmarks rely on **WER (Word Error Rate)** or **MOS (Mean Opinion Score)**. For Urdu and Arabic, this is insufficient because:
1. **Tashkeel Invisibility:** A model can get the word right but the *vowels* wrong, completely changing the meaning of a Hadith.
2. **Nastaliq Ligature Collapse:** Standard models often skip complex ligatures in Urdu, which doesn't show up in simple text-to-text WER.

## Our Unique Solution: The LFS (Linguistic Fidelity Score)
We introduce the **Linguistic Fidelity Score (LFS)**, a weighted composite metric:

$$	ext{LFS} = w_1(	ext{TPI}) + w_2(	ext{CS}_{	ext{acc}}) - w_3(	ext{MCD})$$

Where:
- **TPI (Tashkeel Preservation Index):** A window-based check that compares the predicted phoneme sequence against the diacritic markers.
- $	ext{CS}_{	ext{acc}}$ **(Code-Switching Accuracy):** Measures the spectral continuity during the transition between Urdu and Arabic.
- **MCD:** Mel-Cepstral Distortion.

## Why This is the New Standard
By isolating the **Tashkeel Dropout Rate**, we provide empirical proof of a model's ability to handle sacred and formal texts, moving beyond 'naturalness' into 'linguistic correctness'.
