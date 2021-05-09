const woman = ["a scientist", "a queen", "a pirate", "a giant rabbit"]
const man = ["a police officer", "an artist", "your grandfather", "a killer robot"]
const place = ["on pluto", "at the super market", "in a spooky, bat-filled cave"]
const she_wore = ["scuba diving gear", "fairy wings", "a paper bag"]
const he_wore = ["a purple suit", "a shark costume", "a beach towel"]
const woman_says = ["'who are you'", "'how many beans make five'", "'why?'"]
const man_says = ["'beep boop'", "'don't eat frogs'", "'what time do you call this'"]
const consequence = ["world peace", "chaos", "a giant foot squashed them", "rainbows"]
const world_says = ["'errant nonsense'", "'cheese is trending now'", "loading..."]

const random = {
    choice: (wordArray) => wordArray[1]
}

//import random


    console.log(random.choice(woman), "met", random.choice(man), random.choice(place))
    console.log("she was wearing", random.choice(she_wore))
    console.log("he was wearing", random.choice(he_wore))
    console.log("she said,", random.choice(woman_says))
    console.log("he said,", random.choice(man_says))
    console.log("the consequence was", random.choice(consequence))
    console.log("the world said,", random.choice(world_says))
    console.log()
    input("press enter to play again")
    console.log()