#!/bin/bash

curl "http://localhost:8000/prompts/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
