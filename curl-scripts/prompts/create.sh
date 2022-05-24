#!/bin/bash
NAME="Test Prompt 3"
PROMPT="Test prompt for a user to use 3"
TOKEN="32a21f2bf4888211a0abd1864c127563c4a815cd"

curl "http://localhost:8000/prompts/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "prompt": {
      "name": "'"${NAME}"'",
      "prompt": "'"${PROMPT}"'"
    }
  }'

echo
