# payloads.py
COGNIGY_GALLERY_PAYLOAD = {
    "type": "gallery",
    "_cognigy": {"_default": {"_gallery": {"type": "carousel", "items": [{"title": "Test Gallery", "subtitle": "", "imageUrl": "https://api.scon-assets.schwarz/scon-bot-assets/images/lidl_support_mylidl/gps_pt_new_max_working_time.png", "buttons": [{"title": "Test Gallery", "type": "postback", "payload": "Test Gallery 1"}]}, {"title": "Test Gallery 2", "subtitle": "", "imageUrl": "https://storage.googleapis.com/gweb-cloudblog-publish/images/data-security-threat-protection.max-1100x1100.jpg", "buttons": [{"title": "Test Gallery 2", "type": "open_url", "url": "https://google.com"}]}]}}}
}
COGNIGY_QUICK_REPLIES_PAYLOAD = {
    "type": "quickReplies",
    "_cognigy": {"_default": {"_quickReplies": {"type": "quick_replies", "text": "", "quickReplies": [{"title": "Test Quick Replies", "contentType": "postback", "payload": "Test Quick Replies"}]}}}
}
COGNIGY_BUTTONS_PAYLOAD = {
    "type": "buttons",
    "_cognigy": {"_default": {"_buttons": {"type": "buttons", "text": "", "buttons": [{"title": "Text with Buttons", "type": "postback", "payload": "Text with Buttons"}]}}}
}
COGNIGY_LIST_PAYLOAD = {
    "type": "list",
    "_cognigy": {"_default": {"_list": {"type": "list", "items": [{"title": "Test List", "subtitle": ""}, {"title": "Test List 2", "subtitle": ""}, {"title": "Test List3", "subtitle": ""}], "button": {"title": "Test Button List", "type": "postback", "payload": "Test List"}}}}
}
COGNIGY_IMAGE_PAYLOAD = {
    "type": "image",
    "_cognigy": {"_default": {"_image": {"type": "image", "imageUrl": "https://api.scon-assets.schwarz/scon-bot-assets/images/lidl_support_mylidl/gps_pt_new_max_working_time.png", "fallbackText": "Test Image"}}}
}
