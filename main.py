from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def main():
    # print("Hello from fight-nepal!")
    return "fight-nepal"


if __name__ == "__main__":
    main()
