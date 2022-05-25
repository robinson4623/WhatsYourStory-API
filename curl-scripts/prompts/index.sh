#!/bin/bash
TOKEN="816d53801f2399034556a88791f3bc79be568950"

curl "http://localhost:8000/prompts/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
