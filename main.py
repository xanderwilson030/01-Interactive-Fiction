#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "216ACD94-C70D-42CE-80F1-FA90A0D7F747",
  "name": "Zork",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1630601285901,
  "passages": [
    {
      "name": "West of House",
      "tags": "",
      "id": "1",
      "text": "This is an open field west of a white house, with a boarded front door.\n\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[WEST->Forest]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
          "original": "[[NORTH->North of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of House",
          "original": "[[SOUTH->South of House]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Forest",
          "original": "[[WEST->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is an open field west of a white house, with a boarded front door."
    },
    {
      "name": "North of House",
      "tags": "",
      "id": "2",
      "text": "You are facing the north side of a white house. There is no door here, and all the windows are barred.\n\n[[WEST->West of House]]\n[[EAST->East of House]]\n[[NORTH->Forest]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of House",
          "original": "[[WEST->West of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of House",
          "original": "[[EAST->East of House]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "Forest",
          "original": "[[NORTH->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the north side of a white house. There is no door here, and all the windows are barred."
    },
    {
      "name": "South of House",
      "tags": "",
      "id": "3",
      "text": "You are facing the south side of a white house. There is no door here, and all the windows are barred.\n\n[[WEST->West of House]]\n[[EAST->East of House]]\n[[SOUTH->Forest]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of House",
          "original": "[[WEST->West of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of House",
          "original": "[[EAST->East of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the south side of a white house. There is no door here, and all the windows are barred."
    },
    {
      "name": "Forest",
      "tags": "",
      "id": "4",
      "text": "This is a forest, with trees in all directions around you.\n\n[[NORTH->Sunlit Forest]]\n[[EAST->Forest]]\n[[SOUTH->Forest]]\n[[WEST->Forest]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Sunlit Forest",
          "original": "[[NORTH->Sunlit Forest]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Forest",
          "original": "[[EAST->Forest]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Forest",
          "original": "[[WEST->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is a forest, with trees in all directions around you."
    },
    {
      "name": "East of House",
      "tags": "",
      "id": "5",
      "text": "You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is slightly ajar.\n\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[EAST->Sunlit Forest]]\n[[WEST->Kitchen]]\n[[ENTER->Kitchen]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
          "original": "[[NORTH->North of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of House",
          "original": "[[SOUTH->South of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Sunlit Forest",
          "original": "[[EAST->Sunlit Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Kitchen",
          "original": "[[WEST->Kitchen]]"
        },
        {
          "linkText": "ENTER",
          "passageName": "Kitchen",
          "original": "[[ENTER->Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is slightly ajar."
    },
    {
      "name": "Sunlit Forest",
      "tags": "",
      "id": "6",
      "text": "This is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here.\n\n[[NORTH->Forest]]\n[[SOUTH->Forest]]\n[[EAST->Forest]]\n[[WEST->East of House]]\n[[UP->Tree]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Forest",
          "original": "[[NORTH->Forest]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Forest",
          "original": "[[EAST->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "East of House",
          "original": "[[WEST->East of House]]"
        },
        {
          "linkText": "UP",
          "passageName": "Tree",
          "original": "[[UP->Tree]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here."
    },
    {
      "name": "Kitchen",
      "tags": "",
      "id": "7",
	  "score": 20,
      "text": "You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open.\n\n[[EAST->East of House]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "East of House",
          "original": "[[EAST->East of House]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open."
    },
    {
      "name": "Tree",
      "tags": "",
      "id": "8",
	  "score": 10,
      "text": "You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest.\n\n[[DOWN->Sunlit Forest]]",
      "links": [
        {
          "linkText": "DOWN",
          "passageName": "Sunlit Forest",
          "original": "[[DOWN->Sunlit Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest."
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

location_label = "West of House"
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
