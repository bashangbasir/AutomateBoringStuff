# Assertion and assert statement 

market_2nd = {"ns":"green","ew":"red"}

def switch_lights(intersection):
    for keys in intersection.keys():
        if intersection[keys] == "green":
            intersection[keys] = "yellow"
        elif intersection[keys] == "yellow":
            intersection[keys] = "red"
        elif intersection[keys] == "red":
            intersection[keys] = "green"
    assert "red" in intersection.values(), "Neither light is red!" + str(intersection)
    print("Swith lights!")

print("Now lights is : {}".format(market_2nd))
switch_lights(market_2nd)
print("Now lights is : {}".format(market_2nd))
