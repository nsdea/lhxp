echo 'Fixing Slash Commands...'

curl --location --request PUT 'https://discord.com/api/v9/applications/BOT_ID_HERE/commands' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bot BOT_TOKEN_HERE' \
--data-raw '[]'

echo '\n'
echo 'Done.'
echo 'WAIT before running this script again! You might get ratelimited.'