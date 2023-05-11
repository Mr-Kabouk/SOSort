def classifier(json_data):
    if isinstance(json_data, dict):
        print("Error")
        return
    result = {'urgent': 0, 'not urgent': 0}
    total = 0
    for item in json_data:
        if item['label'] in ['sad', 'surprised', 'fearful', 'disgust', 'angry']:
            result['urgent'] += item['score']
        else:
            result['not urgent'] += item['score']

        total += item['score']

    urgency_sum = result['urgent'] / (result['urgent'] + result['not urgent'])

    return urgency_sum
