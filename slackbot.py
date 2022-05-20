import json
import os
from decouple import AutoConfig
from flask import Flask, Response
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from threading import Thread

# env
home = os.path.expandvars("$HOME")
# now = datetime.datetime.now()
# out = f"{home}/Downloads/result_{now:%Y%m%d_%H%M%S}.csv"
env = os.getcwd() + '/.env'

# pwd
cwd = os.path.dirname(os.path.abspath("__file__"))
dir_path = os.path.dirname(os.path.realpath(__file__))

if cwd != dir_path:
    os.chdir(dir_path)
    print(os.getcwd())

# creds
config = AutoConfig(os.getcwd())
if os.path.exists(env):
    API_KEY = config('API_KEY')
    SLACK_CLIENT_ID = config('SLACK_CLIENT_ID')
    SLACK_CLIENT_SECRET = config('SLACK_CLIENT_SECRET')
else:
    API_KEY = os.getenv('API_KEY')
    SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID')
    SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET')

slack_token = API_KEY
VERIFICATION_TOKEN = os.environ['VERIFICATION_TOKEN']

# This `app` represents your existing Flask app
app = Flask(__name__)

greetings = ["hi", "hello", "hello there", "hey"]

#instantiating slack client
slack_client = WebClient(slack_token)

# An example of one of your Flask app's routes
@app.route("/")
def event_hook(request):
    json_dict = json.loads(request.body.decode("utf-8"))
    if json_dict["token"] != VERIFICATION_TOKEN:
        return {"status": 403}

    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
    return {"status": 500}
    return


slack_events_adapter = SlackEventAdapter(
    SLACK_CLIENT_SECRET, "/slack/events", app
)


@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    def send_reply(value):
        event_data = value
        message = event_data["event"]
        if message.get("subtype") is None:
            command = message.get("text")
            channel_id = message["channel"]
            if any(item in command.lower() for item in greetings):
                message = (
                    "Hello <@%s>! :tada:"
                    % message["user"]  # noqa
                )
                slack_client.chat_postMessage(channel=channel_id, text=message)
    thread = Thread(target=send_reply, kwargs={"value": event_data})
    thread.start()
    return Response(status=200)


# Start the server on port 3000
if __name__ == "__main__":
    app.run(port=3000)
