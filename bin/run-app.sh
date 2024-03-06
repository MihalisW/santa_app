set -a # automatically export all variables
source .app.local.env
set +a

python3 -m venv flask
source $(pwd)/flask/bin/activate
pip install -r $(pwd)/requirements.txt
python3 main.py