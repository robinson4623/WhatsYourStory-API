#!/bin/bash
TITLE="My First Story"
STORY="this is my first story about a time that I took camp to learn how to become a programmer."
TOKEN="32a21f2bf4888211a0abd1864c127563c4a815cd"

curl "http://localhost:8000/stories/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "story": {
      "title": "'"${TITLE}"'",
      "story": "'"${STORY}"'"
    }
  }'

echo
