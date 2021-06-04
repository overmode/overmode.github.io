# Breakout

Customized version of the BREAKOUT by Hyoko

## Setup

1. `cd ./app`
2. `pip install -r requirements.txt`
2. `uvicorn main:app --reload`  | --reload used to develop



#### Docker
 1. `docker-compose up --build`


## Play and see scores

Play at `localhost:8000`
scores are stored in `score.csv`



## TODO 
- Adding a database instead of a csv file
- Secure the game (encrypt score)
- show a descent ranking page
