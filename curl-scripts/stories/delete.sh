#!/bin/bash

curl "http://localhost:8000/stories/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
