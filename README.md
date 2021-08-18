## Requirements
* You need to get a [Slack API key](https://api.slack.com/apps?new_app=1).
* You need to get a Bitly username and Bitly API key from [here](https://bitly.com/a/sign_in?rd=/a/oauth_apps)

  **NOTE: You will surely need [this article](https://www.geeksforgeeks.org/python-how-to-shorten-long-urls-using-bitly-api/) later.**
* You need to get a [Youtube Data API](https://console.developers.google.com/apis/credentials?project=_) key.
* You need to get a [Live football score](https://www.football-data.org/client/register) API key.
* You need to create a [Custom Search Engine ID](https://cse.google.com/cse/create/new) by adding any or all of the following websites as per your choice:
  * https://genius.com/
  * http://www.lyricsted.com/
  * http://www.lyricsbell.com/
  * https://www.glamsham.com/
  * http://www.lyricsoff.com/
  * http://www.lyricsmint.com/

  **NOTE: For more information, you may look at the [Lyrics Extractor](https://github.com/Techcatchers/PyLyrics-Extractor) Python Library.**
* You need to get a [Google Custom Search JSON](https://developers.google.com/custom-search/v1/overview) API key.
* You need to get a [News API](https://newsapi.org/) key.

## Usage
1. Clone this repository and set up environment variables in a `.env` file stored in `/src` directory with all the required credentials.
2. Install all the package requirements from the `requirements.txt` file.
    ```python
    pip install -r requirements.txt
    ```
3. Run the program.

   **NOTE: If something doesn't work as expected even after following all the above mentioned steps then please raise an issue and we will try to fix the issue as soon as possible.**

## TODO
* Refactor README.md for `pipenv`
* Strip out silly bits for boring work-centric use cases (i.e., KB article links, NLP)

# SOURCE
[PDF](https://drive.google.com/file/d/1b3v5K1x4ILq1xHJIY-bEu4ZQHXeVC7PP/view?usp=sharing) 

[Video](https://youtu.be/McJr1AOhyj8) 

[Guide to building your own](https://hackernoon.com/a-guide-to-building-a-multi-featured-slackbot-with-python-73ea5394acc) 
