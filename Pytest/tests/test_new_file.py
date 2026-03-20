import requests

def test_post_request():
    url ="https://example.com"
    params = {'id':123}
    headers = {
        "Cotent-Type":"application/json"
    }
    payload = {
        "name": "jphn doe",
        "age": 30
    }
    response = requests.post(url,headers=headers, json=payload, params=params)
    assert response.status_code == 200
    print(response.json())