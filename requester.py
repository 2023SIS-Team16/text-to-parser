import request_sender

class Requester:
    text = ""

    #Pushes new characters, returns translation if appropriate
    def push_char(char):
        print(char)
        text = text + char

        if(len(text) > 15):
            res_data = request_sender.buffer_truncate_translate({ 
                "text": text,
                "index": 0,
            })
            text = res_data["new_text"]
            return res_data["result"]

        return ""