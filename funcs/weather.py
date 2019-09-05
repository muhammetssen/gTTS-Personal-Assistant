def get_weather_info(city):
    import requests
    data = requests.get(('http://api.apixu.com/v1/current.json?key=778d748aa4fe4adfa79104923190409&q={}').format(city)).json()
    try:
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']
        sentences = []
        sentences.append('The weather is {}'.format(str(condition)))
        sentences.append('Temperature is {}'.format(str(temp)[0:-2]))
        return sentences
    except:
        print('There is no such a city')
