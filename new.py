import requests

endpoint = "https://fabee-v2-chat.openai.azure.com/"  # Replace if incorrect
deployment_name = "gpt-4o"  # Replace with your actual deployment name
api_version = "2024-05-01-preview"

url = f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version={api_version}"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
data = {
    "messages": [{"role": "system", "content": "Hello, world!"}],
    "max_tokens": 50
}

response = requests.post(url, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
