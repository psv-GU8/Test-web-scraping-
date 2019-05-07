from rasa_nlu.model import Interpreter
import actions as act

model_directory = "./models/current/nlu/default/model_20190507-094448"
interpreter = Interpreter.load(model_directory)
slots = {
    'color' : '',
    'size':'',
}

def nextAction(intent,entities='',slots_value=''):
    if entities =="shirts":
       return act.get_y_data()
    if entities:
        if slot_value=='color':
            slots[slot_value] = entities
        else:
            slots[slot_value]= entities
    if intent == 'color_search': return act.get_ebay_data(slots['color'])
    if intent == 'size_search': return act.get_size_data(slots['size'])
    if entities =="shoes": return act.get_shoe_data()
    if entities =="smart bands": return act.get_band_data()
    if entities =="speakers": return act.get_speaker_data()
    if entities =="sunglasses": return act.get_sunglass_data()
    if entities =="saree": return act.get_saree_data()
    if entities =="memory card": return act.get_memory_data()
    if entities =="pants": return act.get_pant_data()
    if entities =="mouse": return act.get_mouse_data()
    if entities =="caps": return act.get_cap_data()
    if entities =="football": return act.get_ball_data()
    if entities =="mobile": return act.get_mobile_data()


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
