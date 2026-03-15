from fastapi.testclient import TestClient
import app.main

from fastapi import status 


client=TestClient(app)

def test_return_helt_check():
    response=client.get("/helthy")
    assert response.status_code ==status.HTTP_200_OK 
    assert response.json()=={'status':'helthy'}

