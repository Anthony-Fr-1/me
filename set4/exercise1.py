"""All about IO."""


import json
import os
import requests
import inspect
import sys

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print("Be careful that your relative paths are")
    print("relative to where you think they are")
    print("LOCAL", LOCAL)
    print("CWD", CWD)


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """

    json_data = open(LOCAL + "/lazyduck.json").read()

    data = json.loads(json_data)

    lastname = data["results"][0]["name"]["last"]
    password = data["results"][0]["login"]["password"]
    postcode = data["results"][0]["location"]["postcode"]
    ID = data["results"][0]["id"]["value"]
    postcodePlusID = int(postcode) + int(ID)

    # print(lastname, password, postcodePlusID)

    return {
        "lastName": lastname,
        "password": password,
        "postcodePlusID": postcodePlusID,
    }
    # json_data = open(LOCAL + "/lazyduck.json").read()

    # data = json.loads(json_data)
    # last_name = data["results"][0]["name"]["last"]
    # postcode = data["results"][0]["location"]["postcode"]
    # password = data["results"][0]["login"]["password"]
    # id = data["results"][0]["id"]["value"]
    # postcode_id = int(postcode) + int(id)
    # print(data)
    # print(last_name, password, postcode_id)

    # return {"lastName": last_name, "password": password, "postcode_id": postcode_id}


def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=20
    The generator takes a single argument, length (`wordlength`) of the word.
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &wordlength=
    """

    list = []
    for number in range(3, 20, 2):
        ogprt1 = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="
        og = ogprt1 + str(number)
        oglink = requests.get(og)
        list.append(oglink.text)
        # print(oglink.text)
    for number in range(20, 3, -2):
        ogprt1 = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="
        og = ogprt1 + str(number)
        oglink = requests.get(og)
        list.append(oglink.text)
        # print(oglink.text)
    return list
    # import requests

    # word_list = []
    # for i in range(3, 20, 2):
    #     Response = requests.get(
    #         "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="
    #         + str(i)
    #     )
    #     # print(Response.text)
    #     word_list.append(Response.text)
    # for i in range(20, 3, -2):
    #     Response = requests.get(
    #         "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="
    #         + str(i)
    #     )
    #     # print(Response.text)
    #     word_list.append(Response.text)
    # # print(word_list)
    # return word_list


def pokedex(low=1, high=5):
    """Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.

    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """

    template = "https://pokeapi.co/api/v2/pokemon/{id}"

    tallest = 0
    for id in range(low, high):
        url = template.format(id=id)
        r = requests.get(url)
        if r.status_code is 200:
            the_json = json.loads(r.text)
            # print(the_json)
            currentheight = the_json["height"]
            if tallest < currentheight:
                tallest = currentheight
                name = the_json["name"]
                weight = the_json["weight"]
                height = the_json["height"]
    print(name, weight, height)

    return {"name": name, "weight": weight, "height": height}

    # template = "https://pokeapi.co/api/v2/pokemon/{id}"

    # max_height = 0

    # for i in range(1, 5, 1):
    #     template = "https://pokeapi.co/api/v2/pokemon/{id}"
    #     url = template.format(id=i)
    #     r = requests.get(url)
    #     if r.status_code == 200:
    #         the_json = json.loads(r.text)
    #         height = the_json["height"]
    #         if max_height < height:
    #             max_height = the_json["height"]
    #             name = the_json["name"]
    #             weight = the_json["weight"]
    # print(f"'name': {name}, 'weight': {weight}, 'height': {max_height}")

    # return {"name": name, "weight": weight, "height": max_height}

    # for i in range(1, 5, 1):
    # Response = requests.get(
    # "https://pokeapi.co/api/v2/pokemon/" + str(i)

    # req = requests.get("http://pokeapi.co/api/v2/pokemon/1/")
    # API_CALL = "https://pokeapi.co/api/v2/generation/generation-ii"
    # requests.get(API_CALL)
    # RES = requests.get(API_CALL)
    # RES.json()  # returns a dictionary
    # DATA = RES.json()
    # DATA["pokemon_species"]

    # height = ["height"]

    # https://pokeapi.co/api/v2/pokemon/{id or name}/

    # height =
    # name =
    # weight =
    # only between low and high
    # need the top 5 tallest


def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the Set4 directory.
    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    TIP: this might come in handy if you need to hack a 3d print file in the future.
    """

    mode = "r"  # from the docs
    pewbook = open("set4/Trispokedovetiles(laser).gcode", mode)
    pewbookdata = pewbook.read()
    counter = pewbookdata.count("M10 P1")
    pewbook.close()

    mode = "w"
    lasers = open("set4/lasers.pew", mode)
    # or ../me/set4/lasers.pew
    lasers.write(str(counter))
    lasers.close()

    # with open("set4/Trispokedovetiles(laser).gcode", "r") as g_code:
    #     m_code_count = g_code.read().count("M10 P1")

    # with open("set4/lasers.pew", "w") as pew:
    #     pew.write(str(m_code_count))

    # file_path = "set4/Trispokedovetiles(laser).gcode"
    # with open(file_path, "r", encoding="utf-8") as f:
    #     lines = f.readlines()
    # could use a list comprehension
    # print(f.read())
    # way 1
    # counter = 0
    # for line in lines:
    #     if "M10 P1" in line:
    #         counter += 1
    # way 2
    # len gives you the length of something
    # calling len on a string gives you the number of characters in a string
    # read the file, do something to it and then save it again

    # counter = len([x for x in lines if "M10 P1" in x])

    # out_file_path = "set4/lasers.pew"
    # with open(out_file_path, "w", encoding="utf-8") as f:
    #     f.write(str(counter))


if __name__ == "__main__":
    functions = [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if (inspect.isfunction(obj))
    ]
    for function in functions:
        try:
            print(function())
        except Exception as e:
            print(e)
    if not os.path.isfile("lasers.pew"):
        print("diarist did not create lasers.pew")
