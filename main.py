#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "E9ED8A9A-379E-46D9-98BD-39EC7BADDB72",
  "name": "Pyramid",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1630987096723,
  "passages": [
    {
      "name": "Desert",
      "tags": "",
      "id": "1",
      "text": "You are at the edge of a great expanse. Around you lies nothing but sand and bones. In the distance, you notice a large pyramid rising out of the sand to your north. To your east and west lie more sand. Your exit is to your south.\n\n[[NORTH->Pyramid Base]]\n[[WEST->Glass Desert]]\n[[EAST->Mirage]]\n[[SOUTH->Leave]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Pyramid Base",
          "original": "[[NORTH->Pyramid Base]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Glass Desert",
          "original": "[[WEST->Glass Desert]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Mirage",
          "original": "[[EAST->Mirage]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Leave",
          "original": "[[SOUTH->Leave]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at the edge of a great expanse. Around you lies nothing but sand and bones. In the distance, you notice a large pyramid rising out of the sand to your north. To your east and west lie more sand. Your exit is to your south."
    },
    {
      "name": "Pyramid Base",
      "tags": "",
      "id": "2",
      "text": "You gaze up at the mighty pyramid, the stones covered in layers of dust and sand. There appears to be a hole in the wall that you can climb in through. Dare you ENTER?\n\n[[ENTER->Pyramid Interior]]\n[[BACK->Desert]]",
      "links": [
        {
          "linkText": "ENTER",
          "passageName": "Pyramid Interior",
          "original": "[[ENTER->Pyramid Interior]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Desert",
          "original": "[[BACK->Desert]]"
        }
      ],
      "hooks": [],
      "cleanText": "You gaze up at the mighty pyramid, the stones covered in layers of dust and sand. There appears to be a hole in the wall that you can climb in through. Dare you ENTER?"
    },
    {
      "name": "Glass Desert",
      "tags": "",
      "id": "3",
      "text": "After traveling a fair distance to the east, you notice you've come upon a desert made entirely out of glass. Unfortunately for you, your shoes do not have enough padding to cross this glass basin. It would prove fatal to do so.\n\n[[WEST->Desert]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "Desert",
          "original": "[[WEST->Desert]]"
        }
      ],
      "hooks": [],
      "cleanText": "After traveling a fair distance to the east, you notice you've come upon a desert made entirely out of glass. Unfortunately for you, your shoes do not have enough padding to cross this glass basin. It would prove fatal to do so."
    },
    {
      "name": "Mirage",
      "tags": "",
      "id": "4",
      "text": "In the distance you notice a speck of green. Could it be an oasis?! Wrong. It was just mirage. All you did was look foolish.\n\n[[WEST->Desert]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "Desert",
          "original": "[[WEST->Desert]]"
        }
      ],
      "hooks": [],
      "cleanText": "In the distance you notice a speck of green. Could it be an oasis?! Wrong. It was just mirage. All you did was look foolish."
    },
    {
      "name": "Leave",
      "tags": "",
      "id": "5",
      "text": "You choose to leave the desert. Perhaps a very untraditional choice. It's not very nice to ignore all the work the narrator has put in for you. You can either move FORWARD with your life, or turn BACK.\n\n[[BACK->Desert]]\n[[FORWARD->New Life]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Desert",
          "original": "[[BACK->Desert]]"
        },
        {
          "linkText": "FORWARD",
          "passageName": "New Life",
          "original": "[[FORWARD->New Life]]"
        }
      ],
      "hooks": [],
      "cleanText": "You choose to leave the desert. Perhaps a very untraditional choice. It's not very nice to ignore all the work the narrator has put in for you. You can either move FORWARD with your life, or turn BACK."
    },
    {
      "name": "New Life",
      "tags": "",
      "id": "6",
      "score":10,
      "text": "It looks like you're really doing this, aren't you? A bit heartbreaking, but lets continue. After escaping the desert, you return to your hotel room and go to the airport, returning home. Your parents aren't too happy to see you back, after all, you are 30, and you still live in their basement. They kick you out of the house for good, wanting you to make something of yourself. You start to think, what if you wrote a novel about your experiences? Or maybe a movie. You can either move forward for a NOVEL or a MOVIE, or you can go back.\n\n[[BACK->Leave]]\n[[Novel->Novel Idea]]\n[[Movie->Movie Idea]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Leave",
          "original": "[[BACK->Leave]]"
        },
        {
          "linkText": "NOVEL",
          "passageName": "Novel Idea",
          "original": "[[NOVEL->Novel Idea]]"
        },
        {
          "linkText": "MOVIE",
          "passageName": "Movie Idea",
          "original": "[[MOVIE->Movie Idea]]"
        }
      ],
      "hooks": [],
      "cleanText": "It looks like you're really doing this, aren't you? A bit heartbreaking, but lets continue. After escaping the desert, you return to your hotel room and go to the airport, returning home. Your parents aren't too happy to see you back, after all, you are 30, and you still live in their basement. They kick you out of the house for good, wanting you to make something of yourself. You start to think, what if you wrote a novel about your experiences? Or maybe a movie. You can either move forward for a NOVEL or a MOVIE, or you can go back."
    },
    {
      "name": "Novel Idea",
      "tags": "",
      "id": "7",
      "text": "A writing storm has overtaken you! Furiously transcribing your answers down on the pages, you create a beautiful masterpiece. There might be some slight exaggerations present inside, but if you removed them there wouldn't be much of a book left. All that's left is for you to choose, SELFPUBLISH or go with a traditional PUBLISHER. You can always go back to your parent's basement... maybe.\n\n[[SELFPUBLISH->Self Publish]]\n[[PUBLISHER->Publish]]\n[[BACK->New Life]]",
      "links": [
        {
          "linkText": "SELFPUBLISH",
          "passageName": "Self Publish",
          "original": "[[SELFPUBLISH->Self Publish]]"
        },
        {
          "linkText": "PUBLISHER",
          "passageName": "Publish",
          "original": "[[PUBLISHER->Publish]]"
        },
        {
          "linkText": "BACK",
          "passageName": "New Life",
          "original": "[[BACK->New Life]]"
        }
      ],
      "hooks": [],
      "cleanText": "A writing storm has overtaken you! Furiously transcribing your answers down on the pages, you create a beautiful masterpiece. There might be some slight exaggerations present inside, but if you removed them there wouldn't be much of a book left. All that's left is for you to choose, SELFPUBLISH or go with a traditional PUBLISHER. You can always go back to your parent's basement... maybe."
    },
    {
      "name": "Movie Idea",
      "tags": "",
      "id": "8",
      "score": 20,
      "text": "A movie! That's what's all the rage these days. Why bother writing a book when you can write a much longer script. You furiously piece together your script and travel to the annual Director's convention in Hollywood, CA. Who will you show your script to? Steven SPIELBERG or George LUCAS.\n\n[[LUCAS->No Movie]]\n[[SPIELBERG->No Movie]]",
      "links": [
        {
          "linkText": "LUCAS",
          "passageName": "No Movie",
          "original": "[[LUCAS->No Movie]]"
        },
        {
          "linkText": "SPIELBERG",
          "passageName": "No Movie",
          "original": "[[SPIELBERG->No Movie]]"
        }
      ],
      "hooks": [],
      "cleanText": "A movie! That's what's all the rage these days. Why bother writing a book when you can write a much longer script. You furiously piece together your script and travel to the annual Director's convention in Hollywood, CA. Who will you show your script to? Steven SPIELBERG or George LUCAS."
    },
    {
      "name": "Self Publish",
      "tags": "",
      "id": "9",
      "text": "Publishers aren't really your thing, so you decide to self publish. It is difficult to source the money for legal fees and printing, but eventually you get your book available for sale. It ends up on the New York Times #1 don't read list. ...Hold on a second, that can't be right. I thought the whole point of this was for you to be independent and live on your own? I guess the writers over there spotted your lies pretty quickly. Nobody would believe you found bananas in a desert.\n\n[[BACK->New Life]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "New Life",
          "original": "[[BACK->New Life]]"
        }
      ],
      "hooks": [],
      "cleanText": "Publishers aren't really your thing, so you decide to self publish. It is difficult to source the money for legal fees and printing, but eventually you get your book available for sale. It ends up on the New York Times #1 don't read list. ...Hold on a second, that can't be right. I thought the whole point of this was for you to be independent and live on your own? I guess the writers over there spotted your lies pretty quickly. Nobody would believe you found bananas in a desert."
    },
    {
      "name": "Publish",
      "tags": "",
      "id": "10",
      "text": "You are a person of great tradition, and you decide to go with a very esteemed publisher. Unfortunately, publishers tend to fact check your information. After realizing your book is full of lies, you get dropped, and banned from every publisher in North America. Maybe your parents would take you back in.\n\n[[BACK->New Life]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "New Life",
          "original": "[[BACK->New Life]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are a person of great tradition, and you decide to go with a very esteemed publisher. Unfortunately, publishers tend to fact check your information. After realizing your book is full of lies, you get dropped, and banned from every publisher in North America. Maybe your parents would take you back in."
    },
    {
      "name": "No Movie",
      "tags": "",
      "id": "11",
      "text": "They ignore you... After laughing, of course\n\n[[BACK->New Life]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "New Life",
          "original": "[[BACK->New Life]]"
        }
      ],
      "hooks": [],
      "cleanText": "They ignore you... After laughing, of course"
    },
    {
      "name": "Pyramid Interior",
      "tags": "",
      "id": "12",
      "text": "You make it inside the pyramid. In front of you lies a PASSAGE into darkness. On your right rests a DOOR with a large scorpion on it. Where do you dare go?\n\n[[PASSAGE->Riches]]\n[[DOOR->Scorpions]]\n[[BACK->Desert]]",
      "links": [
        {
          "linkText": "PASSAGE",
          "passageName": "Riches",
          "original": "[[PASSAGE->Riches]]"
        },
        {
          "linkText": "DOOR",
          "passageName": "Scorpions",
          "original": "[[DOOR->Scorpions]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Desert",
          "original": "[[BACK->Desert]]"
        }
      ],
      "hooks": [],
      "cleanText": "You make it inside the pyramid. In front of you lies a PASSAGE into darkness. On your right rests a DOOR with a large scorpion on it. Where do you dare go?"
    },
    {
      "name": "Riches",
      "tags": "",
      "id": "13",
      "score":100,
      "text": "At the end of the dark passage is a tomb filled with unimagineable riches. You've done it! Take that Mr. Baker, you were actually paying attention in history class.\n\n[[BACK->Pyramid Interior]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Pyramid Interior",
          "original": "[[BACK->Pyramid Interior]]"
        }
      ],
      "hooks": [],
      "cleanText": "At the end of the dark passage is a tomb filled with unimagineable riches. You've done it! Take that Mr. Baker, you were actually paying attention in history class."
    },
    {
      "name": "Scorpions",
      "tags": "",
      "id": "14",
      "score": 1,
      "text": "Oh, if only you had heeded the warning! You fall into a pit of scorpions and lay trapped. If you're careful, you might be able to CLIMB back up.\n\n[[CLIMB->Pyramid Interior]]",
      "links": [
        {
          "linkText": "CLIMB",
          "passageName": "Pyramid Interior",
          "original": "[[CLIMB->Pyramid Interior]]"
        }
      ],
      "hooks": [],
      "cleanText": "Oh, if only you had heeded the warning! You fall into a pit of scorpions and lay trapped. If you're careful, you might be able to CLIMB back up."
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
    if "passages" in world:
        for passage in world["passages"]:
            if location_label == passage["name"]:
                return passage
    return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
    if "name" in current_location and "cleanText" in current_location:
        print("Moves: " + str(moves) + ", Score: " + str(score))
        print("You are at the " + str(current_location["name"]))
        print(current_location["cleanText"] + "\n")
    

def get_input():
    response = input("What do you want to do? ")
    response = response.upper().strip()
    return response

def update(current_location, location_label, response):
    if response == "":
        return location_label
    if "links" in current_location:
        for link in current_location["links"]:
            if link["linkText"] == response:
                return link["passageName"]
    print("I don't understand what you are trying to do. Try again.")
    return location_label


# ----------------------------------------------------------------

location_label = "Desert"
current_location = {}
response = ""
score = 0
moves = 0

while True:
    if response == "QUIT":
        break
    moves += 1

    location_label = update(current_location, location_label, response)
    current_location = find_current_location(location_label)

    if "score" in current_location:
        score = score + current_location["score"]

    render(current_location, score, moves)
    response = get_input()


print("Thanks for playing!")
