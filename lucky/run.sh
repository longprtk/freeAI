# run.sh
#!/bin/bash

# Cài đặt phụ thuộc Python (nếu chưa cài)
if [ ! -d "env" ]; then
  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
fi

# Chạy Lucky
python lucky/lucky.py
