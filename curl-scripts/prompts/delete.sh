#!/bin/bash

curl "http://localhost:8000/prompts/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
