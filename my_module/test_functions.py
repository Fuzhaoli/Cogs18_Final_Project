import random
from my_module.functions import *

def test_chatbot():
    assert end('Quit') == True
    assert selector(['A','B','C'],['A','B','C','D','E'],['R']) == 'R'
    assert buy_cd('Can I buy CD?') == 'We sell CD at the livehouse'
    assert fan_meeting('Is there a fan meeting?') == 'No there is not any fan meeting'
    assert other_artist('What about other artists?') == 'Sorry we only sell tickets of Ryo'