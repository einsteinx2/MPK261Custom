import Live
from _Framework.EncoderElement import EncoderElement

def make_encoder_relative(name, channel, number, midi_message_type):
    return EncoderElement(midi_message_type, channel, number, Live.MidiMap.MapMode.relative_two_compliment, name=name)
