from rasa_nlu.model import Interpreter
from shirt import *
from shoes import *
from memory import *
from bands import *
from sunglasses import *
from sarees import *
from pant import *
from mouse import *
from caps import *
from ball import *
from mobile import *
from size import *
model_directory = "./models/current/nlu/default/model_20190507-094448"
interpreter = Interpreter.load(model_directory)
slots = {
    'color' : '',
}
slot ={
    'size':'',
}
def nextAction(intent,entities='',slots_value=''):
    if entities =="shirts":
       return get_y_data()
    if entities:
        if slot_value=='color':
            slots[slot_value] = entities
        else:
            slot[slot_value]= entities
    if intent == 'color_search': return get_ebay_data(slots['color'])
    if intent == 'size_search': return get_size_data(slot['size'])
    if entities =="shoes": return get_shoe_data()
    if entities =="smart bands": return get_band_data()
    if entities =="speakers": return get_speaker_data()
    if entities =="sunglasses": return get_sunglass_data()
    if entities =="saree": return get_saree_data()
    if entities =="memory card": return get_memory_data()
    if entities =="pants": return get_pant_data()
    if entities =="mouse": return get_mouse_data()
    if entities =="caps": return get_cap_data()
    if entities =="football": return get_ball_data()
    if entities =="mobile": return get_mobile_data()
while True:
    raw_data = input(">> ")
    if raw_data == 'quit':
       break

    data = interpreter.parse(raw_data)
    intent = data['intent']['name']
    if data['entities']:
        entities = data['entities'][0]['value']
        slot_value = data['entities'][0]['entity']
        print(nextAction(intent,entities,slot_value))
    else:
        print(nextAction(entities))
