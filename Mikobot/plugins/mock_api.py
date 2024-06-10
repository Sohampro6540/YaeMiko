from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for chatbot responses
chatbot_responses = {
    "PALM": {
        "0": "Response from PALM model 0",
        "1": "Response from PALM model 1",
        # Add more responses if needed
    },
    "GPT": {
        "5": "Response from GPT model 5",
        "6": "Response from GPT model 6",
        # Add more responses if needed
    }
}

# Endpoint for chatbot interaction
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    model_id = data.get('model_id')
    prompt = data.get('prompt')

    if model_id in chatbot_responses:
        response = chatbot_responses[model_id].get(prompt, "Default response for the model")
        return jsonify({"content": response}), 200
    else:
        return jsonify({"error": "Model ID not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
