from pathlib import Path

import torch
from faster_whisper import WhisperModel
from transformers import AutoTokenizer, AutoModelForCausalLM


def carregarModelos():
    torch.set_num_threads(8)
    caminhoQwen = Path(__file__).parent / "modelos" / "qwen35"
    tokenizador = AutoTokenizer.from_pretrained(caminhoQwen)
    qwen = AutoModelForCausalLM.from_pretrained(caminhoQwen, dtype=torch.float32)
    whisper = WhisperModel("base", device="cpu", compute_type="int8", cpu_threads=4)
    return tokenizador, qwen, whisper


carregarModelos()
print("Modelos carregados.")






