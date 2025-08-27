from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# ✅ create database if not exists
con = sqlite3.connect("fights.db", check_same_thread=False)


def initialize_database():
    create_event_table = """
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        eventName TEXT,
        participantOne TEXT,
        participantTwo TEXT,
        time TEXT,
        winner TEXT
    );
    """
    cursor = con.cursor()
    cursor.execute(create_event_table)
    con.commit()


# initialize DB
initialize_database()


@app.get("/")
def main():
    return {"message": "flight-nepal"}


class CreateEventRequest(BaseModel):
    eventName: str
    participantOne: str
    participantTwo: str
    time: str
    winner: str


@app.post("/event")
def create_event(event: CreateEventRequest):
    insert_statement = """
    INSERT INTO events (eventName, participantOne, participantTwo, time, winner)
    VALUES (?, ?, ?, ?, ?)
    """
    cursor = con.cursor()
    cursor.execute(
        insert_statement,
        (event.eventName, event.participantOne, event.participantTwo, event.time, event.winner)
    )
    con.commit()
    return {"message": "Event created successfully", "event": event}


@app.get("/event/get-all")
def get_all_events():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        events.append({
            "id": row[0],
            "eventName": row[1],
            "participantOne": row[2],
            "participantTwo": row[3],
            "time": row[4],
            "winner": row[5]
        })
    return {"events": events}


@app.delete("/event/{event_id}")
def delete_event(event_id: int):
    cursor = con.cursor()
    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
    con.commit()
    return {"message": f"Event with id {event_id} deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
