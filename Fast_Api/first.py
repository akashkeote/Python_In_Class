from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def foo():
    return{'akash':'keote'}
@app.get("/about")
def about():
    return{'about':'this is an about page'}
