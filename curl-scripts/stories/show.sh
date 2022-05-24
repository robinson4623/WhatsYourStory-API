#!/bin/bash

curl "http://localhost:8000/stories/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
