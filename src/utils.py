import subprocess

def query_model(prompt):
    result = subprocess.run(
        ["ollama", "run", "qwen:2.5b"],
        input=prompt.encode('utf-8'),
        capture_output=True
    )
    return result.stdout.decode('utf-8').strip()
