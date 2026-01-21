import subprocess

prompt = """
SUAS NÃO É SUS.
Explique de forma curta e correta o que é o SUAS no Brasil.
Base: LOAS.
"""

result = subprocess.run(
    ["ollama", "run", "phi3:mini", prompt],
    capture_output=True,
    text=True
)

print(result.stdout)
