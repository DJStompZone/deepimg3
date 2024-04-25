# Import the necessary modules
import json
import random
import time
from fastapi import FastAPI, Request
from pydantic import BaseModel, ValidationError

# Define the app and the model classes
app = FastAPI()

class Item(BaseModel):
    name: str
    prompt: str

class Collection(BaseModel):
    __root__: dict[str, list[Item]]

# Create a route that accepts a POST with a JSON payload
@app.post("/")
async def create_collection(request: Request):
    # Get the raw JSON data from the request body
    data = await request.json()
    try:
        # Validate the data with pydantic
        collection = Collection.parse_obj(data)
        # Generate a random file name with a 4-digit number and a unix timestamp
        file_name = f"{random.randint(1000, 9999)}-{int(time.time())}.json"
        # Save the data to disk as a JSON file
        with open(file_name, "w") as f:
            json.dump(data, f)
        # Return a success message with the file name
        return {"message": f"Collection saved to {file_name}"}
    except ValidationError as e:
        # Return an error message with the validation errors
        return {"message": "Invalid collection", "errors": e.errors()}