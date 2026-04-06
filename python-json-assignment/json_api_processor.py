import json

api_response = '''
{
    "id": "req_123",
    "status": "success",
    "result": {
        "text": "Hello world",
        "confidence": 0.98
    }
}
'''

data = json.loads(api_response)

request_id = data["id"]
status = data["status"]
text = data["result"]["text"]
confidence = data["result"]["confidence"]


print("Request ID:", request_id)
print("Status:", status)
print("Text:", text)
print("Confidence:", confidence)

if confidence < 0.9:
    print("Warning: Low confidence score")

follow_up = {
    "request_id": request_id,
    "status": "processed",
    "message": "Result processed successfully",
    "confidence": confidence
}


json_output = json.dumps(follow_up, indent=4)


with open("response.json", "w") as file:
    file.write(json_output)

print("JSON file created: response.json")