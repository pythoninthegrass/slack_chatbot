import os
from decouple import AutoConfig
from slack_sdk import WebClient
from slack_sdk.oauth import AuthorizeUrlGenerator
from slack_sdk.oauth.installation_store import FileInstallationStore, Installation
from slack_sdk.oauth.state_store import FileOAuthStateStore
from slack_sdk.rtm_v2 import RTMClient

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
    SLACK_CLIENT_SECRET= config('SLACK_CLIENT_SECRET')
else:
    API_KEY = os.getenv('API_KEY')
    SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID')
    SLACK_CLIENT_SECRET= os.getenv('SLACK_CLIENT_SECRET')

# Issue and consume state parameter value on the server-side.
state_store = FileOAuthStateStore(expiration_seconds=300, base_dir="../data")
# Persist installation data and lookup it by IDs.
installation_store = FileInstallationStore(base_dir="../data")

# Build https://slack.com/oauth/v2/authorize with sufficient query parameters
authorize_url_generator = AuthorizeUrlGenerator(
    client_id=SLACK_CLIENT_ID,
    scopes=["app_mentions:read", "chat:write"],
    redirect_uri='https://localhost:3000/slack/oauth_redirect',
    # user_scopes=["search:read"],
)

from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/slack/install", methods=["GET"])
def oauth_start():
    # Generate a random value and store it on the server-side
    state = state_store.issue()
    # https://slack.com/oauth/v2/authorize?state=(generated value)&client_id={client_id}&scope=app_mentions:read,chat:write&user_scope=search:read
    url = authorize_url_generator.generate(state)
    return f'<a href="{url}">' \
           f'<img alt=""Add to Slack"" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>'

@app.route("/slack/oauth_redirect", methods=["GET"])
def post_install():
    # Verify the "state" parameter

    # Retrieve the auth code from the request params
    code_param = request.args['code']

    # An empty string is a valid token for this request
    client = WebClient()

    # Request the auth tokens from Slack
    response = client.oauth_v2_access(
        client_id=SLACK_CLIENT_ID,
        client_secret=SLACK_CLIENT_SECRET,
        code=code_param
    )
    print(response)

    # TODO: verify access token is getting generated; pass to `rtm`
    with open('access_token.txt', 'w') as output:
        output.write(response['access_token'])

    with open('access_token.txt', 'r') as output:
        access_token = output.read()

rtm = RTMClient(token=access_token)

@rtm.on("message")
def handle(client: RTMClient, event: dict):
    # try:
    #     rtm = RTMClient(token=access_token)
    #     print("Bot is up and running!")
    #     rtm.start()
    # except Exception as err:
    #     print(err)
    if 'Hello' in event['text']:
        channel_id = event['channel']
        thread_ts = event['ts']
        user = event['user']                # This is not username but user ID (the format is either U*** or W***)

        client.web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",
            thread_ts=thread_ts
        )

if __name__ == "__main__":
    # export SLACK_CLIENT_ID=111.222
    # export SLACK_CLIENT_SECRET=xxx
    # export FLASK_ENV=development
    # python3 integration_tests/samples/openid_connect/flask_example.py

    if len(access_token) > 1:
        rtm.start()

    context = ('/etc/ssl/server.crt', '/etc/ssl/server.key')
    app.run('localhost', debug=True, ssl_context=context, port=3000)
