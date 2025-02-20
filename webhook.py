import os
import dialogflow_v2 as dialogflow
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Set up Dialogflow credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-dialogflow-key.json"
DIALOGFLOW_PROJECT_ID = "your-dialogflow-project-id"

def detect_intent(text, session_id):
    """Send user message to Dialogflow and return response."""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)

    text_input = dialogflow.TextInput(text=text, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    return response.query_result.fulfillment_text

@app.route("/webhook", methods=["POST"])
def webhook():
    """Handle incoming messages from Tawk.to."""
    data = request.json
    if "message" in data:
        user_message = data["message"]["text"]
        user_id = data["message"]["sender"]

        # Get AI response from Dialogflow
        bot_response = detect_intent(user_message, user_id)

        # Send response back to Tawk.to (or any system)
        return jsonify({"text": bot_response})

    return jsonify({"status": "ignored"}), 200

if __name__ == "__main__":
    app.run(port=5000)
