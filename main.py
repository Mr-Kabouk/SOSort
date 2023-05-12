import requests
import re
from EmergencyClass import EmergencyCall
import Emotion_lib as emotion

API_URL_1 = "https://api-inference.huggingface.co/models/facebook/wav2vec2-large-960h-lv60-self"
#API_URL_2 = "https://api-inference.huggingface.co/models/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
API_URL_2 = "https://api-inference.huggingface.co/models/harshit345/xlsr-wav2vec-speech-emotion-recognition"

headers = {"Authorization": "Bearer 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"}

common_words = ["Help", "Accident", "Fire", "Injured", "Police",
                "Ambulance", "Heart attack", "Robbery", "Shot",
                "Breathing", "Emergency", "Shooting"]

def query_1(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL_1, headers=headers, data=data)
    return response.json()


def query_2(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL_2, headers=headers, data=data)
    return response.json()

def main():
    output_1 = query_1("sample2.flac")
    output_2 = query_2("sample1.mp3")
    print(output_1)
    print(output_2)

    call_transcript = output_1['text']
    key_word_list = []
    emotions_lvl = emotion.classifier(output_2)

    EmergencyCall_test = EmergencyCall(is_call_urgent =False, key_words_recognized = key_word_list, call_summary = call_transcript, emotions_value = emotions_lvl)

    for word in common_words:
        match = re.search(word, output_1['text'], re.IGNORECASE)
        if match:
            #print(f"The word '{word}' was found in the text.")
            key_word_list.append(word)
            EmergencyCall_test.update_urgency_transcript()

    EmergencyCall_test.urgency_check()
    EmergencyCall_test.update_key_words_recognized(key_word_list)
    EmergencyCall_test.print_emergency()
    EmergencyCall_test.to_json("test.txt")

if __name__ == '__main__':
    main()