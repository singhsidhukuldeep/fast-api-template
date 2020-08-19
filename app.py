# Core Pkg
import uvicorn
from fastapi import FastAPI,Query

# ML Aspect
from modelPredict import getPrediction

# useful info
info = {
"text": "Hello this is a Fast API",
"http://127.0.0.1/": "You can then navigate to the localhost to see your app in action.",
"http://127.0.0.1/docs": "This yields the OpenAPI Swagger UI.",
"http://127.0.0.1/redoc": "This uses the Redoc UI with some documentations out of the box.",
}

# init app
app = FastAPI()

# Routes
@app.get('/')
async def index():
	return info

@app.post('/')
async def index():
	return info

# Sample
@app.get('/sample/')
async def sample(text:str = Query(None,min_length=None,max_length=None)):
	return {"text":text}

@app.post('/sample/')
async def sample(text:str = Query(None,min_length=None,max_length=None)):
	return {"text":text}



# ML Aspect
@app.get('/predict/')
async def predict(text:str = Query(None,min_length=None,max_length=None)):
	return getPrediction(text)

@app.get('/predict/{text}')
async def predict(text):
	return getPrediction(text)

# Using Post
@app.post('/predict/{text}')
async def predict(text):
	return getPrediction(text)



if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
