#!/bin/bash

curl "http://localhost:8000/prompts/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
