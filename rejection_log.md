# Rejection Log: Rigorous Urdu & Arabic TTS

This log details why specific models failed the benchmark based on the complex Urdu-Arabic code-switching dataset.

| Model Name | Technical Failure Point |
| :--- | :--- |
| EGTTS-V0.1 | Fails Rigorous Test: XTTS v2 architecture struggles with the specific cadence of Arabic-to-Urdu switches in the provided passages. |
| ArTST | Fails Rigorous Test: SpeechT5 baseline fails to parse complex tashkeel, leading to robotic and incorrect vowelization. |
| MMS-TTS-Ara | Fails Rigorous Test: VITS architecture ignores nuanced tashkeel in the Hadith sections, resulting in poor intelligibility. |
| Nabra | Fails Rigorous Test: 82M parameter size is insufficient for the linguistic complexity and code-switching of the benchmark passages. |
| MMS-TTS-Urd | Fails Rigorous Test: Weak on the Arabic switch; lacks the phonetic precision required for the Hadith passages. |
| ahmedHanzala/urdu-tts | Fails Rigorous Test: Unable to maintain consistency when encountering the Arabic diacritics in the provided script. |
