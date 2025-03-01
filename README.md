# slack_chatbot

## Requirements
* [Slack API key](https://api.slack.com/apps?new_app=1)
* Bitly username and API key from [here](https://bitly.com/a/sign_in?rd=/a/oauth_apps)

  **NOTE: [Useful article](https://www.geeksforgeeks.org/python-how-to-shorten-long-urls-using-bitly-api/) for later.**
* [Youtube Data API](https://console.developers.google.com/apis/credentials?project=_) key
* [Custom Search Engine ID](https://cse.google.com/cse/create/new) then add [Genius](https://genius.com)

  **NOTE: For more information, see the [Lyrics Extractor](https://github.com/Techcatchers/PyLyrics-Extractor) Python Library.**
* [Google Custom Search JSON](https://developers.google.com/custom-search/v1/overview) API key
* [News API](https://newsapi.org/) key

## Usage
* Clone this repository and set up environment variables in a `.env` file stored in `/src` directory with all the required credentials
    * Fill in `.env` from [Slack API - Settings: Basic Information](https://api.slack.com/apps)
    ```
    # .env
    API_KEY=
    SLACK_CLIENT_ID=
    SLACK_CLIENT_SECRET=
    ```
* Create a virtualenv
    ```bash
    python -m venv .venv
    ```
* Install all the package requirements
    ```bash
    # vanilla
    pip install -r requirements.txt

    # pipenv (Pipfile)
    pipenv install -r requirements.txt
    ```
* Run the program
    ```bash
    # vanilla
    python slackbot.py

    # pipenv shell
    pipenv shell
    python slackbot.py

    # pipenv ad-hoc commands
    pipenv run python slackbot.py
    ```
   **NOTE: If something doesn't work as expected even after following all the above mentioned steps then please raise an issue and we will try to fix the issue as soon as possible.**

## TODO
* Refactor README.md for `pipenv`
* Scope permissions
* Setup auth
* Talk to stakeholders
    * Hold off on any security/infra items until signed off
* POC
    * Write class
        * Get request
        * Respond with object
            * Interpret keywords (hard-coded)
            * No config (json), DB, etc initially
    * Assign to specific channel
    * Strip out silly bits for boring work-centric use cases (i.e., KB article links, NLP)
* QA
    * Write tests
* "Prod"
    * Add in config/DB
    * Assign to `#it` or other channels

## SOURCES
[Guide to building your own](https://hackernoon.com/a-guide-to-building-a-multi-featured-slackbot-with-python-73ea5394acc) 

[python-slack-sdk/flask_example.py at main · slackapi/python-slack-sdk](https://github.com/slackapi/python-slack-sdk/blob/main/integration_tests/samples/openid_connect/flask_example.py) 

[Installation — Python Slack SDK](https://slack.dev/python-slack-sdk/installation/index.html) 

[RTM Client — Python Slack SDK](https://slack.dev/python-slack-sdk/real_time_messaging.html#real-time-messaging-rtm) 
