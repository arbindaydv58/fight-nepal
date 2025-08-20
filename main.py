from fastapi import FastAPI
import sqlite3
con = sqlite3.connect("fights.db")
from pydantic import BaseModel

def initalize_databse():
    create_event_table = """
    CREATE TABLE events (
        eventName TEXT,
        participantOne TEXT,
        participantTwo TEXT,
        time TEXT,
        winner TEXT
    );
    """
    cursor = con.cursor()
    cursor.execute(create_event_table)
app = FastAPI()


@app.get("/")   
def main():
    return "flight-nepal"

class CreateEventRequest(BaseModel):  # <-- add colon here and fix typo in "Crete"
    eventName: str
    participantOne: str
    participantTwo: str
    time: str
    winner: str

@app.post("/event")
def create_event(event: CreateEventRequest):



    return event


@app.get("/event/delete")
def delete_event():
    return "delete event"

@app.get("/event/get-all")
def get_all_events():
    return "All event"


if __name__ == "__main__":
    main()


# from fastapi import FastAPI
# from pydantic import BaseModel
# import sqlite3

# app = FastAPI()

# # ✅ Define request body with Pydantic
# class Event(BaseModel):
#     name: str
#     fighterOne: str
#     fighterTwo: str
#     date: str  # ISO format: YYYY-MM-DD

# # ✅ Create database and table if not exists
# con = sqlite3.connect("fights.db", check_same_thread=False)
# cur = con.cursor()
# cur.execute("""
# CREATE TABLE IF NOT EXISTS events (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     fighterOne TEXT NOT NULL,
#     fighterTwo TEXT NOT NULL,
#     date TEXT NOT NULL
# )
# """)
# con.commit()


# @app.get("/")
# def main():
#     return {"message": "flight-nepal"}


# # ✅ Insert event into database
# @app.post("/event")
# def create_event(event: Event):
#     cur.execute(
#         "INSERT INTO events (name, fighterOne, fighterTwo, date) VALUES (?, ?, ?, ?)",
#         (event.name, event.fighterOne, event.fighterTwo, event.date),
#     )
#     con.commit()
#     return {"message": "Event created successfully", "event": event.dict()}


# # ✅ Delete all events (just for demo)
# @app.get("/event/delete")
# def delete_event():
#     cur.execute("DELETE FROM events")
#     con.commit()
#     return {"message": "All events deleted"}


# # ✅ Get all events
# @app.get("/event/get-all")
# def get_all_events():
#     cur.execute("SELECT * FROM events")
#     rows = cur.fetchall()
#     events = [
#         {"id": row[0], "name": row[1], "fighterOne": row[2], "fighterTwo": row[3], "date": row[4]}
#         for row in rows
#     ]
#     return {"events": events}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)