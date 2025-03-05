from dotenv import load_dotenv
from datetime import datetime
import json, requests
from git import Repo
import os

def fetch_wordle(today: str):
    url = f"https://www.nytimes.com/svc/wordle/v2/{today}.json"
    wordle = json.loads(open("wordles.json", "r").read())
    
    try:
        response = requests.get(url).json()
        wordle[today] = response.get("solution", "Error")
        print(f"{today}: {wordle[today]}")
    except Exception as e:
        print(f"Error fetching {today}: {e}")

    with open("wordles.json", "w") as f:
        json.dump(wordle, f, indent=4)

def git_push(msg: str):
    if repo.is_dirty(untracked_files=True) or repo.index.diff(None):
        try:
            repo = Repo(os.getenv("REPO"))
            origin = repo.remote(name='origin')
            
            repo.git.add(all=True)
            repo.index.commit(msg)
            origin.push()

        except Exception as e:
            print(f"Error occured:", e)

if __name__ == "__main__":
    load_dotenv()
    today = datetime.date.today().strftime("%Y-%m-%d")
    fetch_wordle(today)
    git_push()