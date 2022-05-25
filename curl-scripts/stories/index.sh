#!/bin/bash
TOKEN="2a5093f2afb46e8f6f7aab806a71be7b41b44a25"

curl "http://localhost:8000/stories/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
