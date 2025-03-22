# EchoBot

Bot Framework v4 echo bot sample.

This bot has been created using [Bot Framework](https://dev.botframework.com), it shows how to create a simple bot that accepts input from the user and echoes it back.

## To try this sample

- Clone the repository
```bash
git clone https://github.com/ap9155-hue/02.echo-bot.git
```
- In a terminal, navigate to `02.echo-bot` folder
- Activate your desired virtual environment
- In the terminal, type `pip install -r requirements.txt`
- Run your bot with `python app.py`

## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the latest Bot Framework Emulator from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- File -> Open Bot
- Enter a Bot URL of `http://localhost:3978/api/messages`

## Interacting with the bot and its capabilities

Welcome to the Chatbot! This bot is here to engage with you, provide useful responses, and even entertain you with some fun features. Below is a list of the capabilities that this chatbot currently supports.

Start a conversation: Simply type something to initiate the interaction.
Ask questions or request a specific command: Use the predefined phrases (like "tell me something cool", "what can you do?", etc.) or any other input.
Math calculations: You can also enter mathematical expressions like "5 + 3" or "10 / 2".
Enjoy the jokes and fun facts: Whenever you're in the mood for something light-hearted, just ask the bot for a joke or fun fact!

Capabilities
1. Text Reversal
The chatbot can reverse any text you send. Just type something, and the bot will send it back in reverse order.

2. List of Abilities
Get a list of commands you can use with the bot, including all the fun things it can do.
Example:

You: What can you do?
Bot:
I can do a few cool things:
- Reverse your text
- Tell fun facts
- Chat about the weather
- Introduce myself
- Handle basic errors
- Tell jokes
- Perform math calculations
- Greet you

## Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Channels and Bot Connector Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)
