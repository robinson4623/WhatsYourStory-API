
TOKEN="cfd6794dbc3e5d22112cad79aca0dc67eced8cdb"
OLDPW="kelly"
NEWPW="kelly1"

curl "http://localhost:8000/change-pw/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "passwords": {
      "old": "'"${OLDPW}"'",
      "new": "'"${NEWPW}"'"
    }
  }'

echo
