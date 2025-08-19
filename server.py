import os, subprocess, shlex
from flask import Flask, request, jsonify, abort
from waitress import serve

API_KEY = os.environ.get("COPILOT_AGENT_API_KEY")

app = Flask(__name__)

def run(cmd, cwd=None):
    p = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()

@app.before_request
def auth():
    token = request.headers.get("Authorization", "")
    if not API_KEY or token != f"Bearer {API_KEY}":
        abort(401)

@app.post("/copilot")
def copilot():
    data = request.get_json(force=True, silent=True) or {}
    prompt = data.get("prompt", "").strip()
    repo_path = data.get("repo_path", "").strip() or os.getcwd()

    # mode = (data.get("mode") or "chat").lower()  # chat | suggest | explain
    mode = (data.get("mode") or "explain").lower()  # suggest | explain

    if not prompt:
        return jsonify(error="prompt is required"), 400
    if not os.path.isdir(repo_path):
        return jsonify(error=f"repo_path not found: {repo_path}"), 400

    if mode == "suggest":
        cmd = f'gh copilot suggest {shlex.quote(prompt)}'
    elif mode == "explain":
        cmd = f'gh copilot explain {shlex.quote(prompt)}'
    else:
        # fallback if chat is unsupported
        cmd = f'gh copilot suggest {shlex.quote(prompt)}'

    code, out, err = run(cmd, cwd=repo_path)
    return jsonify(ok=(code==0), code=code, output=out, error=err), (200 if code==0 else 500)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8787"))
    serve(app, host="0.0.0.0", port=port)
