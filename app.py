from flask import Flask, request, render_template
import requests

app = Flask(__name__)
YOUR_API_TOKEN="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"
API_URL = "https://api-inference.huggingface.co/models/openchat/openchat-3.5-0106"
headers = {"Authorization": f"Bearer {YOUR_API_TOKEN}"}  # Replace with your API token

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["GET","POST"])
def chat():
    user_input = request.form["user_input"]
    response = query({"inputs": user_input})
    bot_response = response[0]["generated_text"][len(user_input)+2:]+"....!"
    print(response)
    note="Note: The responses may be differnent based on your prompt, the better prompts pull better replies!"
    return render_template("index.html", user_input=user_input, bot_response=bot_response, note=note)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
