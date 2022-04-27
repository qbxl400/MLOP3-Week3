from fastapi import FastAPI, status

app= FastAPI()

@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perofrm_healthcheck():
        return {'healthcheck': 'Everthing OK!'}