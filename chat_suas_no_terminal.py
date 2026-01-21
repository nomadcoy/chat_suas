import subprocess

MODEL = "phi3:mini"

print("🤖 ChatSUAS (modo terminal)")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        break

    prompt = f"""
SUAS NÃO É SUS.
SUAS = Sistema Único de Assistência Social.
Base: LOAS.

Responda curto e correto:
{pergunta}
"""

    result = subprocess.run(
        ["ollama", "run", MODEL, prompt],
        capture_output=True,
        text=True
    )

    resposta = result.stdout.strip()
    print("\nChatSUAS:", resposta, "\n")
