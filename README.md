# copilot-agent

Small Flask service that proxies GitHub Copilot CLI commands over HTTP.

## Prerequisites
- Python 3.9+
- [GitHub CLI](https://cli.github.com/) with Copilot access
- `flask` and `waitress` Python packages

## Installation
1. Clone the repository and enter the directory:
   ```bash
   git clone <repo-url>
   cd copilot-agent
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install flask waitress
   ```

## Configuration
Set a token used to authenticate requests:
```bash
export COPILOT_AGENT_API_KEY="mysecret"
```

## Running
Start the server (defaults to port `8787`):
```bash
python server.py
```
Use `PORT` to override the port if needed.

## Usage
Send an authorized request to the `/copilot` endpoint:
```bash
curl -X POST http://localhost:8787/copilot \
  -H "Authorization: Bearer $COPILOT_AGENT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "explain hello world", "repo_path": "/path/to/repo", "mode": "explain"}'
```

The server executes the corresponding `gh copilot` command in the given repository and returns the result as JSON.
