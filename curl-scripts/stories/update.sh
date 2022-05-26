#!/bin/bash
ID="14"

TOKEN="cf4c624cd1ef1444c95e390881212d5bc5a29fa1"

TITLE="Updated Title"

STORY="Updated story that is a little longer in length just to test it out and see how things will look."



curl "http://localhost:8000/stories/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "story": {
      "title": "'"${TITLE}"'",
      "story": "'"${STORY}"'"
    }
  }'

echo
