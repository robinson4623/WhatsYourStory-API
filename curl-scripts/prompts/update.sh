#!/bin/bash
PROMPT="Updated prompt from original but left Name of propmpt the same"

ID=3

TOKEN="30e05f82b8ea135d3a124e36f10115bff5c3fb21"

curl "http://localhost:8000/prompts/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "prompt": {
      
      "prompt": "'"${PROMPT}"'"

    }
  }'

echo
