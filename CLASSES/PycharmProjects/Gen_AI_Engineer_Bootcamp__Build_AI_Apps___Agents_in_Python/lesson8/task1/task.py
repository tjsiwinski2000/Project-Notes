from langchain.chat_models import init_chat_model
from flask import Flask, request, jsonify

app = Flask(__name__)

model = init_chat_model(
    model='llama3.2:1b',
    model_provider="ollama"
)

# TODO: Change "/ask" to "/chat"
@app.route("/ask", methods=['POST'])
def chat():
    data = request.get_json()
    response = model.invoke(data['messages'])
    return jsonify(
        {"message": {"role": "assistant",
                     "content": response.content}}
    )

if __name__ == "__main__":
    # TODO: Change port to 5002
    app.run(debug=True, port=5001)
