import math

# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    print("Getting ready to start in 9")
    print("Getting ready to start in 8")
    print("Getting ready to start in 7")
    print("Getting ready to start in 6")
    print("Getting ready to start in 5")
    print("Getting ready to start in 4")
    print("Getting ready to start in 3")
    print("Getting ready to start in 2")
    print("Getting ready to start in 1")
    print("Let's go!")

    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2
    print("area = " + str((triangle["base"] * triangle["height"]) / 2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)



def countdown(message, start, stop, completion_message):
    lst = [i for i in range(stop, start+1)]
    for i in range(1,len(lst)+1):
        print(message + " " + str(lst[-i]))
    print(completion_message)
    return None
        


def calculate_hypotenuse(base, height):
    import math
    hypotenuse = math.sqrt((base**2 + height**2))
    return hypotenuse


def calculate_area(base, height):
    area = 0.5*base*height
    return area


def calculate_perimeter(base, height):
    hypo = calculate_hypotenuse(int(base),int(height))
    perimeter = base + height + hypo
    return perimeter


def calculate_aspect(base, height):
    if height > base:
        aspect = "tall"
    elif base > height:
        aspect = "wide"
    else:
        aspect = "equal"
    return aspect



def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base,height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }



def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    if facts_dictionary["aspect"] == "tall":
        diagram = tall.format(**facts_dictionary)
    if facts_dictionary["aspect"] == "wide":
        diagram = wide.format(**facts_dictionary)
    if facts_dictionary["aspect"] == "equal":
        diagram = equal.format(**facts_dictionary)
    
    facts = pattern.format(**facts_dictionary)
    return (diagram + "\n" + facts)
    


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    info = get_triangle_facts(base, height)
    stuff = tell_me_about_this_right_triangle(info)
    if return_diagram and return_dictionary:
        return {"diagram": stuff, "facts": info}
    elif return_diagram:
        return stuff
    elif return_dictionary:
        return info
    else:
        print("You're an odd one, you don't want anything!")


def get_a_word_of_length_n(length):
    import requests
    
    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={wordlength}"
    path = url.format(wordlength = str(length))
    status = requests.get(path)
    
    if status.status_code is 200:
        string = status.content
        return string.decode("utf-8")

    



def list_of_words_with_lengths(list_of_lengths):
    lst = []
    for i in list_of_lengths:
        lst.append(get_a_word_of_length_n(i))
    return lst

def wordy_pyramid():
    """import requests


    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL.format(api_key="", length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    for i in range(20, 3, -2):
        url = baseURL.format(api_key="", length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    return pyramid_list"""

    pyramid_list = []
    lengths=[3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4]
    pyramid_list.extend(list_of_words_with_lengths(lengths))

    return pyramid_list
    





if __name__ == "__main__":
    #do_bunch_of_bad_things()
    print(wordy_pyramid())
    #countdown("Getting ready to start in ", 9, 1, "Let's Go!")
    #print(triangle_master(5,5,True))
