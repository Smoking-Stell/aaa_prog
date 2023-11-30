from abc import abstractproperty, abstractstaticmethod, ABC

bulbasaur = Pokemon(name='Bulbasaur', category='grass')
bulbasaur.increase_experience(100)
assert bulbasaur.experience == 200, 'Try harder, Neeman'
