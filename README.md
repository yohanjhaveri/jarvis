# Jarvis: A simple CLI tool for interacting with ChatGPT

Say hello to `jarvis`, an awesome tool that conveniently allows you to converse with ChatGPT right from your terminal!

## Installation

> **_NOTE:_** This tool requires [Python](https://www.python.org/downloads/) (`>=3.7`) to be installed on your machine.

To install `jarvis`:
```
pip3 install jarvis-chat
```

## Usage

> **_NOTE:_** You must have a valid API key from OpenAI to use this tool. You can manage your OpenAI API keys [here](https://platform.openai.com/account/api-keys).

To set your OpenAI API key, use the `-k` (or `--key`) argument:
```
jarvis -k <YOUR_API_KEY_HERE>
```

To start talking to jarvis:
```
jarvis
```

## Future Work

- Option to save conversations so they can be continued in a later session
- Option to enter multi-line prompts
- Option to stop or regenerate response
