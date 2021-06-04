from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import csv   

app = FastAPI()

@app.post("/result")
async def result(request: Request):
  try :
    res = await request.json()
    to_store =  [datetime.now().strftime("%Y-%m-%d %H:%M")] + list(res.values())
    with open(r'./score.csv','a') as f:
      writer = csv.writer(f)
      writer.writerow(to_store)
  except Exception as e :
    return  {"error": e.message}

  return {"error" : ""}

app.mount("/ranking", StaticFiles(directory="public/ranking", html=True), name="ranking")
app.mount("/", StaticFiles(directory="public/game", html=True), name="public")



