import json

class EmergencyCall:
    def __init__(self, is_call_urgent, key_words_recognized, call_summary, emotions_value):
        self.final_urgency_transcript = 0
        self.is_call_urgent= is_call_urgent
        self.key_words_recognized = key_words_recognized
        self.call_summary = call_summary
        self.emotion_value = emotions_value

    def update_key_words_recognized(self, key_word_list):
        self.key_words_recognized = key_word_list
    def print_emergency(self):
        urgency = 0
        if self.is_call_urgent == True:
            urgency = "High"
        print("Urgency: {}, Keywords: {} , Emotion level: {}".format(self.is_call_urgent, self.key_words_recognized, self.emotion_value))

    def update_urgency_transcript(self):
        urgency = 0
        urgency_from_transcript = 1
        self.final_urgency_transcript += urgency_from_transcript

    def urgency_check(self):
        urgency_level = self.final_urgency_transcript + self.emotion_value
        if urgency_level > 1:
            self.is_call_urgent = True

    def to_json(self, filename):
        call_data = {"Reason of call": self.key_words_recognized, "Summary": self.call_summary}
        with open(filename, 'w') as file:
            json.dump(call_data, file)
