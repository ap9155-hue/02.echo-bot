# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys
import traceback
from datetime import datetime
from http import HTTPStatus

from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    TurnContext,
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.integration.aiohttp import CloudAdapter, ConfigurationBotFrameworkAuthentication
from botbuilder.schema import Activity, ActivityTypes

from bots import EchoBot
from config import DefaultConfig

CONFIG = DefaultConfig()

# Create adapter.
# See https://aka.ms/about-bot-adapter to learn more about how bots work.
ADAPTER = CloudAdapter(ConfigurationBotFrameworkAuthentication(CONFIG))


# Catch-all for errors.
async def on_error(context: TurnContext, error: Exception):
    # This check writes out errors to console log .vs. app insights.
    # NOTE: In production environment, you should consider logging this to Azure
    #       application insights.
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity(
        "To continue to run this bot, please fix the bot source code."
    )
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":
        # Create a trace activity that contains the error object
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        # Send a trace activity, which will be displayed in Bot Framework Emulator
        await context.send_activity(trace_activity)


ADAPTER.on_turn_error = on_error

# Create the Bot
BOT = EchoBot()


# Listen for incoming requests on /api/messages
async def messages(req: Request) -> Response:
    # Main bot message handler
    if "application/json" not in req.headers.get("Content-Type", ""):
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    body = await req.json()
    print("User Input:", body)

    user_text = body.get("text", "").lower().strip()

    # Predefined responses for specific keywords
    if "weather" in user_text:
        bot_reply = "I can't check live weather yet, but it looks like a great day to code! ☀️"
    elif "who are you" in user_text or "introduce yourself" in user_text:
        bot_reply = "I'm a friendly bot here to chat! I can reverse your text, tell fun facts, and more!"
    elif "tell me something cool" in user_text or "fun fact" in user_text:
        bot_reply = "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good."
    elif "list abilities" in user_text or "what can you do" in user_text:
        bot_reply = (
            "I can do a few cool things: \n"
            "- Reverse your text \n"
            "- Tell fun facts \n"
            "- Chat about the weather \n"
            "- Introduce myself \n"
            "- Handle basic errors \n"
            "- Tell jokes \n"
            "- Perform math calculations \n"
            "- Greet you \n"
        )
    elif "hi" in user_text or "hello" in user_text or "hey" in user_text:
        bot_reply = "Hello there! How can I assist you today?"
    elif "joke" in user_text:
        bot_reply = "Why don't skeletons fight each other? They don't have the guts! 😄"
    elif "help" in user_text:
        bot_reply = "I can help with these commands: \n- Reverse text \n- Tell jokes \n- Share fun facts \n- Chat about the weather \n- Perform math calculations \n- Greet you \nJust ask!"
    elif any(op in user_text for op in ["+", "-", "*", "/"]):
        try:
            result = eval(user_text)  # Basic math evaluation (be cautious with this in production)
            bot_reply = f"The result is: {result}"
        except Exception:
            bot_reply = "Oops, I couldn't understand that math. Try again!"
    elif "goodbye" in user_text or "bye" in user_text:
        bot_reply = "Goodbye! Have a good one!"
    elif not user_text or user_text.isspace():
        bot_reply = "Oops! It looks like you didn't say anything. Try asking me something fun!"
    else:
        # Default: Reverse the text as before
        bot_reply = body["text"][::-1]

    body["text"] = bot_reply
    print("Bot Response:", body)

    activity = Activity().deserialize(body)
    auth_header = req.headers.get("Authorization", "")

    response = await ADAPTER.process_activity(auth_header, activity, BOT.on_turn)
    if response:
        return json_response(data=response.body, status=response.status)

    return Response(status=HTTPStatus.OK)


APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    try:
        web.run_app(APP, host="localhost", port=CONFIG.PORT)
    except Exception as error:
        raise error
