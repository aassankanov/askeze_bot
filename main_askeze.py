# Importing necessary modules
import logging  # Helps us keep track of what’s happening in the bot (useful for debugging)
import requests  # Allows us to make HTTP requests to external APIs
from telegram import Update  # Represents an incoming update/message from a user
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes  # Tools to build the bot

# Your Telegram Bot Token 
BOT_Token = 'Put your telegram token that you can create using botfather'

#enable logging to see errors and info in the consolegit --version

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # Log format
    level = logging.INFO  # Show info-level messages and above
    )

# A simple function to get a random motivational quote from the quotable.io API
def get_quote():
    try:
        response = requests.get('https://api.quotable.io/random')   # Get random quote
        response.raise_for_status()                                 # Raise an error if the request fails
        data = response.json()                                      # Convert the response to a Python dictionary
        return f'"{data["content"]}"\n— {data["author"]}'           # Format the quote nicely
    except Exception as e:
        logging.error(f"Error fetching quote: {e}")                 # Print error in the console
        return "Sorry, I couldn't fetch a quote right now. Please try again later."

#commands functions
#/start button

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(             # Reply to the user with a welcome message
        "Hi! I'm your Motivator Bot. Type /quote to get inspired!"
    )

#/quote button

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote_text=get_quote()                       # Get a motivational quote
    await update.message.reply_text(quote_text)  # Send it back to the user


# This is the main part that runs the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token("put your telegram token that you created").build()   # Create an application (the main bot engine) using your bot token
      # Add command handlers: what to do when someone types /start or /quote
    app.add_handler(CommandHandler("start", start))     # When user types /start, run start()
    app.add_handler(CommandHandler("quote", quote))     # When user types /quote, run quote()

                         # Start the bot and keep it running, checking for new messages
    app.run_polling()    # Starts the bot so it can listen for user messages

