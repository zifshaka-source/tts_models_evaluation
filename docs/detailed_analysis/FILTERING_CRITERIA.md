
# 🛡️ Filtering Criteria: How we chose the Best

We did not just 'pick' models; we put them through a rigorous filtration pipeline.

### Step 1: The Script-Aware Filter
Any model that could not render the Arabic script in UTF-8 without replacing characters with '?' or '�' was immediately discarded.

### Step 2: The Tashkeel Threshold (The "Hard Gate")
We implemented a **Hard Gate** at $12\%$ Tashkeel Dropout. 
- **Logic:** If a model fails to pronounce more than $12\%$ of the vowels in a Hadith, it is considered 'unreliable' for formal use.
- **Result:** This eliminated $60\%$ of early-stage open-source models.

### Step 3: The Code-Switching Continuity Test
Models were tested on the transition between Urdu and Arabic. 
- **Failure:** A 'glitch' or 'pop' in the audio during the switch.
- **Threshold:** Spectral Variance $\Delta S$ must be $< 1.5$.

### Step 4: Human-in-the-loop (HITL) Verification
The top $5$ models were reviewed by native Urdu and Arabic speakers to ensure the 'Ahung' (cadence) was natural and not just mathematically correct.
