# main.py
import os
from flask import Flask, request, jsonify

# Import everything from our new files
from payloads import *
from cards import *

app = Flask(__name__)

@app.route('/', methods=['POST'])
def on_event(request):
    """Handles events from Google Chat."""
    event = request.get_json()
    if event['type'] == 'MESSAGE':
        message = event.get('message', {})
        user_text = message.get('text', '').strip().lower()
        if 'slashCommand' in message:
            user_text = message['slashCommand']['commandName'].lower()
        response = handle_message(user_text)
    elif event['type'] == 'CARD_CLICKED':
        action = event.get('common', {}).get('invokedFunction', '')
        if action == 'echo':
            payload = event.get('common', {}).get('parameters', {}).get('text', 'No payload')
            response = {"text": f"Button clicked! Payload was: `{payload}`"}
        else:
            command = action.replace('show_', '')
            response = handle_message(command)
    else:
        return jsonify({'status': 'event ignored'})
    return jsonify(response)

def handle_message(text):
    """Determines which card to create based on user input."""
    if 'gallery' in text:
        return create_gallery_card(COGNIGY_GALLERY_PAYLOAD)
    elif 'replies' in text:
        return create_quick_replies_card(COGNIGY_QUICK_REPLIES_PAYLOAD)
    elif 'buttons' in text:
        return create_buttons_card(COGNIGY_BUTTONS_PAYLOAD)
    elif 'list' in text:
        return create_list_card(COGNIGY_LIST_PAYLOAD)
    elif 'image' in text:
        return create_image_card(COGNIGY_IMAGE_PAYLOAD)
    else:
        return create_help_card()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
