import requests

response = requests.post("http://127.0.0.1:5000/predict", json={"text": "This is an amazing experience!"})
print(response.json())  # Expected output: {'POSITIVE': 0.99, 'NEGATIVE': 0.01}
