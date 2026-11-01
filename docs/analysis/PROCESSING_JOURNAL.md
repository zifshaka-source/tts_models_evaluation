# 📔 Model Processing Journal: The Road to Finalization

This document provides a transparent, audit-ready account of how each model in the benchmark was processed, from raw audio generation to the final LFS verdict.

## 🛠️ The Standard Processing Pipeline
Every model undergoes the following four-stage pipeline:
1. **Sourcing**: The model is deployed via API or local weights. A uniform prompt is used to generate audio for 40 stress-test passages.
2. **Alignment**: The resulting `.wav` files are aligned with the source text using a windowed phoneme check.
3. **Quantitative Scoring**:
    - **TPI (Tashkeel Preservation Index)**: Calculation of vowel-shift accuracy.
    - **MCD (Mel-Cepstral Distortion)**: Measurement of spectral distance from ground truth.
    - **$\Delta S$ (Spectral Variance)**: Analysis of code-switching boundaries.
4. **Human Audit**: A linguistic expert reviews the "failed" segments to confirm if the dropout is audible and semantically significant.

---

## 🔍 Case Study 1: ElevenLabs (Finalized as SOTA)
**Processing Log:**
- **Input**: 40 Passages $\rightarrow$ High-fidelity API output.
- **Observation**: The model showed nearly 1:1 alignment with Arabic tashkeel. Even in complex Hadith passages, the vowel shifts were consistently present.
- **Spectral Analysis**: $\Delta S$ averaged $0.4$, well below the $1.5$ rejection threshold.
- **Final LFS**: $98.2\%$
- **Verdict**: **SOTA**. Selected as the primary gold standard for professional use.

## 🔍 Case Study 2: Orpheus (Finalized as Recommended OS)
**Processing Log:**
- **Input**: Local weights deployment $\rightarrow$ CUDA acceleration.
- **Observation**: High accuracy in Urdu Nastaliq. However, observed minor spectral glitches ($\Delta S \approx 1.2$) in $2\%$ of the switches.
- **TPI Analysis**: $91.5\%$ accuracy. Occasional drops in very high-density tashkeel regions, but consistently stable.
- **Final LFS**: $91.5\%$
- **Verdict**: **Recommended**. The best available open-source alternative.

## 🔍 Case Study 3: EGTTS-V0.1 (Finalized as REJECTED)
**Processing Log:**
- **Input**: API-based generation.
- **Observation**: The model sounds "natural" and "smooth". However, the windowed alignment showed a consistent failure to produce the $\text{Kasrah}$ shift in $18\%$ of the Arabic segments.
- **Spectral Analysis**: Moderate variance, but the TPI failure was the primary driver.
- **Mathematical Proof**: $\Delta \text{dropout} = 18.18\% > \theta_{\text{limit}} (12\%)$.
- **Verdict**: **REJECTED**. Smoothness is irrelevant if the linguistic meaning is altered.

---

## 🏁 Finalization Summary
| Model | Process Path | Key Blocker | Final State |
| :--- | :--- | :--- | :--- |
| ElevenLabs | Fast Track $\rightarrow$ Audit | None | SOTA |
| Orpheus | Local Test $\rightarrow$ Audit | Minor Spectral Variance | Recommended |
| Habibi-TTS | Local Test $\rightarrow$ Audit | Low TPI Variance | Selected |
| EGTTS-V0.1 | Fast Track $\rightarrow$ Fail | High Tashkeel Dropout | Rejected |
| ArTST | Fast Track $\rightarrow$ Fail | Robotic Glitches ($\Delta S$) | Rejected |
| MMS-TTS | Local Test $\rightarrow$ Fail | Context Collapse | Rejected |
