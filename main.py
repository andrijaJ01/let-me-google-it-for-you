from urllib.parse import quote_plus
import configparser
import praw
import typer
from typing import Optional

__author__='Andrija Jovanovic <andrijajovanovic001@gmail.com>'

app=typer.Typer()
config = configparser.ConfigParser()
config.read('config.ini')
client_id=config["DEFAULT"]["CLIENT_ID"]
client_secret=config['DEFAULT']['SECRET_KEY']
user_agent=config["DEFAULT"]["USER_AGENT"]
username=config["DEFAULT"]["USERNAME"]
password=config["DEFAULT"]["PASSWORD"]

QUESTIONS = ["what is", "who is", "what are"]
REPLY_TEMPLATE = "[Let me google that for you](https://lmgtfy.com/?q={})"


@app.command()
def authorinfo():
    typer.secho(__author__,fg=typer.colors.GREEN)

@app.command()
def start(subreddit:str=typer.Option('',help='subreddit to scrape for questions')):
    if not subreddit:
        typer.secho(f"Please select subreddit to scrape for questions")
        typer.Abort()    
    else:
        reddit= praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password)

	
        subreddit = reddit.subreddit(subreddit)
        for submission in subreddit.stream.submissions():
            process_submission(submission)
	
	
        def process_submission(submission):
    	    if len(submission.title.split()) > 10:
                return
	
        normalized_title = submission.title.lower()
        for question_phrase in QUESTIONS:
            if question_phrase in normalized_title:
                url_title = quote_plus(submission.title)
                reply_text = REPLY_TEMPLATE.format(url_title)
                print(f"Replying to: {submission.title}")
                submission.reply(reply_text)
                break

	
	
if __name__ == "__main__":
    app()	
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																										
