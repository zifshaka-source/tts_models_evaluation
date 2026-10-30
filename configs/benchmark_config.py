# TTS Benchmark Configuration
MODELS = {
    "ElevenLabs": {"api": "commercial", "tier": "Paid", "arch": "Proprietary-LLM"},
    "Orpheus": {"api": "local", "tier": "Open-Source", "arch": "Llama-3-Speech"},
    "Habibi-TTS": {"api": "local", "tier": "Open-Source", "arch": "F5-Flow-Matching"},
    "Azure-TTS": {"api": "commercial", "tier": "Paid", "arch": "Neural-Concatenative"},
    "MMS-TTS": {"api": "local", "tier": "Open-Source", "arch": "VITS-Scaled"}
}

METRICS = {
    "LFS": "Linguistic Fidelity Score",
    "TPI": "Tashkeel Preservation Index",
    "MOS": "Mean Opinion Score",
    "WER": "Word Error Rate"
}

FILTERS = {
    "min_mos": 3.5,
    "max_dropout": 0.12,
    "min_cs_accuracy": 85.0
}