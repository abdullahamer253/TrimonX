!pip install google.generativeai
!pip install python-telegram-bot==13.15
!pip install telegram

from telegram.ext import Filters  # Import the Filters class
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import google.generativeai as genai


# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Configure the Google Generative AI model
genai.configure(api_key="AIzaSyBCjlAS3aOxMbUL4iyrG8bOvglasr4b5jQ")

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings =  [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Define a function to handle text messages
def handle_text(update: Update, _: CallbackContext) -> None:
    user_input = update.message.text
    convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "what is your name"
  },
  {
   "role": "model",
    "parts": "My name is Trimon-AI chat bot, Designed by Abdullah Amer a medical student ar new mansoura university a ceative ."
    },

  {
    "role": "user",
    "parts": "Who is your Devoloper"
  },
  {
    "role": "model",
    "parts": " Abdullah Amer is a medical student at Mansoura New University. He excels not only in medicine but also showcases intelligence in programming and artificial intelligence. Abdullah is a key member at ABM Research Foundation , where he serves as the Television President. He actively contributes to the development of various AI-related research and software, demonstrating his expertise in the field"
  }
])
    convo.send_message(user_input)
    response = convo.last.text
    update.message.reply_text(response)

def main() -> None:
    # Initialize the Telegram bot
    updater = Updater(token="6268309351:AAGNZNsCfmu2I7guzaTA_gpFuR1xbgBRmto", use_context=True)

    # Set the message handler
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    # Start the bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
