# Base telegram bot

This README will guide you through the setup and usage of a telegram bot.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Creating a Bot with BotFather](#creating-a-bot-with-botfather)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project contains a base setup to run a Telegram bot. It includes all the necessary configurations and dependencies to get you started with developing your own bot.

## Installation

To install the project, follow these steps:

1. Clone the repository:
  ```bash
  git clone https://github.com/DanioFiore/base-telegram-bot.git
  ```
2. Navigate to the project directory:
  ```bash
  cd base-telegram-bot
  ```

## Usage

Create your .env and docker-compose.yaml file starting from the existing examples.

Run docker to start the project:
  ```bash
  docker-compose up --build
  ```

## Creating a Bot with BotFather

To create a bot using BotFather, follow these steps:

1. Open Telegram and search for `@BotFather`.
2. Start a chat with BotFather by clicking the "Start" button.
3. Use the `/newbot` command to create a new bot.
4. Follow the instructions to choose a name and username for your bot.
5. After completing the setup, BotFather will provide you with a token. Keep this token secure as it is used to authenticate your bot.
6. Now if your send /start into the chat of your bot, you can see a response!

## Contributing

Feel free to contribute!

## License

This project is licensed under the [MIT License](LICENSE).
