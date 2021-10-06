woman = ["a scientist", "a queen", "a pirate", "a giant rabbit"]
man = ["a police officer", "an artist", "your grandfather", "a killer robot"]
place = ["on pluto", "at the super market", "in a spooky, bat-filled cave"]
she_wore = ["scuba diving gear", "fairy wings", "a paper bag"]
he_wore = ["a purple suit", "a shark costume", "a beach towel"]
woman_says = ["'who are you'", "'how many beans make five'", "'why?'"]
man_says = ["'beep boop'", "'don't eat frogs'", "'what time do you call this'"]
consequence = ["world peace", "chaos", "a giant foot squashed them", "rainbows"]
world_says = ["'errant nonsense'", "'cheese is trending now'", "loading..."]

import random

while True:
    print(random.choice(woman), "met", random.choice(man), random.choice(place))
    print("she was wearing", random.choice(she_wore))
    print("he was wearing", random.choice(he_wore))
    print("she said,", random.choice(woman_says))
    print("he said,", random.choice(man_says))
    print("the consequence was", random.choice(consequence))
    print("the world said,", random.choice(world_says))
    print()
    input("press enter to play again")
    print()