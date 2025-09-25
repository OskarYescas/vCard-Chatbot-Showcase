# cards.py
def create_gallery_card(payload):
    """Translates a Cognigy Gallery into a list of separate Google Chat cards."""
    gallery_data = payload['_cognigy']['_default']['_gallery']
    cards_list = []
    for item in gallery_data.get('items', []):
        buttons = []
        for btn_data in item.get('buttons', []):
            button = {"text": btn_data['title']}
            if btn_data.get('type') == 'open_url':
                button['onClick'] = {"openLink": {"url": btn_data['url']}}
            else:
                button['onClick'] = {"action": {"function": "echo", "parameters": [{"key": "text", "value": btn_data.get('payload', '')}]}}
            buttons.append(button)
        card_item = {"cardId": f"gallery_item_{item.get('title', 'card')}", "card": {"header": {"title": item.get('title', 'Gallery Item'), "subtitle": item.get('subtitle', ''), "imageUrl": item.get('imageUrl', ''), "imageType": "SQUARE"}, "sections": [{"widgets": [{"buttonList": {"buttons": buttons}}]}]}}
        cards_list.append(card_item)
    return {"cardsV2": cards_list}
def create_quick_replies_card(payload):
    """Translates a Cognigy Quick Replies payload into a Google Chat card."""
    qr_data = payload['_cognigy']['_default']['_quickReplies']
    buttons = []
    for reply in qr_data['quickReplies']:
        buttons.append({"text": reply['title'], "onClick": {"action": {"function": "echo", "parameters": [{"key": "text", "value": reply['payload']}]}}})
    card_widgets = []
    if qr_data.get('text'):
        card_widgets.append({"textParagraph": {"text": qr_data['text']}})
    card_widgets.append({"buttonList": {"buttons": buttons}})
    return {"cardsV2": [{"cardId": "quick_replies_card", "card": {"header": {"title": "Quick Replies Showcase"}, "sections": [{"widgets": card_widgets}]}}]}
def create_buttons_card(payload):
    """Translates a Cognigy Buttons payload into a Google Chat card."""
    btn_data = payload['_cognigy']['_default']['_buttons']
    buttons = []
    for btn in btn_data['buttons']:
        button = {"text": btn['title']}
        if btn.get('type') == 'open_url':
            button['onClick'] = {"openLink": {"url": btn['url']}}
        else:
            button['onClick'] = {"action": {"function": "echo", "parameters": [{"key": "text", "value": btn['payload']}]}}
        buttons.append(button)
    card_widgets = []
    if btn_data.get('text'):
        card_widgets.append({"textParagraph": {"text": btn_data['text']}})
    card_widgets.append({"buttonList": {"buttons": buttons}})
    return {"cardsV2": [{"cardId": "buttons_card", "card": {"header": {"title": "Buttons Showcase"}, "sections": [{"widgets": card_widgets}]}}]}
def create_list_card(payload):
    """Translates a Cognigy List payload into a Google Chat card."""
    list_data = payload['_cognigy']['_default']['_list']
    widgets = []
    for item in list_data['items']:
        widgets.append({"decoratedText": {"topLabel": item.get('title', ''), "text": item.get('subtitle', ''), "startIcon": {"knownIcon": "BOOKMARK"}}})
    list_button = list_data.get('button')
    if list_button:
        widgets.append({"buttonList": {"buttons": [{"text": list_button['title'], "onClick": {"action": {"function": "echo", "parameters": [{"key": "text", "value": list_button['payload']}]}}}]}})
    return {"cardsV2": [{"cardId": "list_card", "card": {"header": {"title": "List Showcase"}, "sections": [{"widgets": widgets}]}}]}
def create_image_card(payload):
    """Translates a Cognigy Image payload into a Google Chat card."""
    img_data = payload['_cognigy']['_default']['_image']
    return {"cardsV2": [{"cardId": "image_card", "card": {"header": {"title": "Image Showcase"}, "sections": [{"widgets": [{"image": {"imageUrl": img_data['imageUrl']}}]}]}}]}
def create_help_card():
    """Creates a default help/welcome card."""
    return {
        "cardsV2": [{
            "cardId": "help_card",
            "card": {
                "header": {
                    "title": "Cognigy Showcase Bot",
                    "subtitle": "Select a component to display",
                    "imageUrl": "https://www.pngitem.com/pimgs/m/43-433432_cognigy-logo-hd-png-download.png",
                    "imageType": "CIRCLE"
                },
                "sections": [{
                    "header": "Component Demonstrations",
                    "collapsible": True,
                    "widgets": [
                        {"decoratedText": {"text": "Showcases a multi-card carousel.", "startIcon": {"knownIcon": "STAR"}, "button": {"text": "Show Gallery", "onClick": {"action": {"function": "show_gallery"}}}}},
                        {"decoratedText": {"text": "Shows a list of interactive quick replies.", "startIcon": {"knownIcon": "STAR"}, "button": {"text": "Show Replies", "onClick": {"action": {"function": "show_replies"}}}}},
                        {"decoratedText": {"text": "Displays text with a button.", "startIcon": {"knownIcon": "STAR"}, "button": {"text": "Show Button", "onClick": {"action": {"function": "show_buttons"}}}}},
                        {"decoratedText": {"text": "Renders a vertical list of items.", "startIcon": {"knownIcon": "STAR"}, "button": {"text": "Show List", "onClick": {"action": {"function": "show_list"}}}}},
                        {"decoratedText": {"text": "Displays a single image.", "startIcon": {"knownIcon": "STAR"}, "button": {"text": "Show Image", "onClick": {"action": {"function": "show_image"}}}}}
                    ]
                }]
            }
        }]
    }
