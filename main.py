import time

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Replace these with your own api_id and api_hash
api_id = 123456
api_hash = '0123456789abcdef0123456789abcdef'

# Set up the client
client = TelegramClient('session_name', api_id, api_hash)

async def send_message(account, group, message):
    """Sends a message to the specified group using the given account."""
    try:
        # Sign in to the account
        await client.login(username=account['username'], password=account['password'])
        print(f"Signed in to {account['username']}")

        # Find the group to send messages to
        group = await client.get_entity(group)

        # Send the message
        await client.send_message(group, message)
        print(f"Sent message from {account['username']}")
    except SessionPasswordNeededError:
        print("Two-factor authentication required for account")

async def schedule_messages(accounts, group, message, interval):
    """Schedules the given message to be sent to the specified group using the given accounts at the specified interval."""
    while True:
        for account in accounts:
            await send_message(account, group, message)
        time.sleep(interval)

async def main():
    # Connect to the server
    await client.start()
    print("Connected to Telegram")

    # Load the list of accounts from a file or database
    accounts = [{'username': 'account1', 'password': 'password1'},
                {'username': 'account2', 'password': 'password2'},
                {'username': 'account3', 'password': 'password3'}]

    # Set the message and interval
    message = "This is an automated message"
    interval = 3600  # Send message every hour

    # Schedule the messages
    await schedule_messages(accounts, 'my_group', message, interval)

# Run the main function
with client:
    client.loop.run_until_complete(main())
