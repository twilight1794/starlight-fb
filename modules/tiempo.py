from fbchat import models
from rules import *
import requests
from datetime import datetime

def cIcon(cod):
    if cod<=202 or 230<=cod<=232:
        return "⛈️"
    elif 210<=cod<=221:
        return "🌩️"
    elif 300<=cod<=321:
        return "🌦️"
    elif 500<=cod<=531:
        return "🌧️"
    elif 600<=cod<=602:
        return "❄️"
    elif 611<=cod<=622:
        return "🌨️"
    elif 700<=cod<=771:
        return "🌁"
    elif cod==781:
        return "🌪️"
    elif cod==800:
        return "☀️"
    elif cod==801:
        return "🌤️"
    elif cod==802:
        return "⛅"
    elif cod==803:
        return "🌥️"
    elif cod==804:
        return "☁️"

@command('tiempo')
def run(**kwargs):
    data = requests.get('http://api.openweathermap.org/data/2.5/weather?id=3514670&appid='+kwargs['config']['tiempo']['api_key']+'&lang=es&units=metric').json()
    msgs = ['Tiempo en Villahermosa, Tabasco']
    msgs.append(cIcon(data['weather'][0]['id'])+' '+data['weather'][0]['description'])
    msgs.append('🌡️ '+str(data['main']['temp'])+ ' ℃ (sensación de '+str(data['main']['feels_like'])+' ℃)')
    msgs.append('🌅 '+datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')+' - 🌇 '+datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M'))
    msgs.append('🌬️ '+str(data['wind']['speed']*3.6)+' km/h - 🌫️ '+str(data['clouds']['all'])+'%')
    msgs.append('⏰ '+datetime.fromtimestamp(data['dt']).strftime('%H:%M'))
    for i in msgs:
        kwargs['fbobj'].send(models.Message(text=i), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
