from fastapi import FastAPI, Request
import uvicorn
import argparse

# Create a FastAPI instance
app = FastAPI()


# Define a route
@app.get("/")
async def read_root(request: Request):
    return {"Hello": "World", 'headers': request.headers}

# Get the port number from command-line argument
parser = argparse.ArgumentParser(description="FastAPI application.")
parser.add_argument("--port", type=int, help="Port to listen on", default=8000)
args = parser.parse_args()

# Run the server
if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=args.port, reload=True)

"""bash
python main.py --port 8000
python main.py --port 8001
nginx -t
nginx -c /path/to/nginx.conf
curl localhost:8081

nginx -s stop
"""
