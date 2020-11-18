def getWelcome(meal_options, restart=False):
    meal_options_string = __convertListToNumberedString(meal_options)

    if (restart):
        return (
            "Haiyaaa, why you no say from the start, waste my time 🤬\n\n"
            "🍽️ Come, tell me, what you want?\n"
            "{}".format(meal_options_string)
        )
    else:
        return (
            "Eh handsome, welcome to Subway! 😊\n\n"
            "🍽️ What kind of meal you want today ah?\n"
            "{}".format(meal_options_string)
        )


def getAskBreads(bread_options):
    return (
        "🍞 What bread you want? All so fresh\n"
        "{}".format(__convertListToNumberedString(bread_options))
    )


def getAskMains(main_options):
    return (
        "🍖 Not bad, good choice. Mains leh?\n"
        "{}".format(__convertListToNumberedString(main_options))
    )


def getAskVeggies(veggie_options):
    return (
        "🥬 Fuyohhh, very good. Come, pick your veggie\n"
        "{}".format(__convertListToNumberedString(veggie_options))
    )


def getAskSauces(sauce_options):
    return (
        "🥣 Sauce? If not dry like eating sand\n"
        "{}".format(__convertListToNumberedString(sauce_options))
    )


def getAskTopups(topup_options):
    return (
        "🧀 Got people behind, faster pick your topups\n"
        "{}".format(__convertListToNumberedString(topup_options))
    )


def getAskSides(side_options):
    return (
        "🍪 Okay almost done, pick your sides now, faster\n"
        "{}".format(__convertListToNumberedString(side_options))
    )


def getOrderSummary(meals, breads, mains, veggies, sauces, topups, sides):
    return (
        "Swee lah, come, I repeat your order\n\n"
        "<b>🍽️ Meal</b>\n"
        "{meals}\n"
        "<b>🍞 Bread</b>\n"
        "{breads}\n"
        "<b>🍖 Main</b>\n"
        "{mains}\n"
        "<b>🥬 Veggie</b>\n"
        "{veggies}\n"
        "<b>🥣 Sauce</b>\n"
        "{sauces}\n"
        "<b>🧀 Topup</b>\n"
        "{topups}\n"
        "<b>🍪 Side</b>\n"
        "{sides}\n"
        "Bye!"
    ).format(
        meals=__convertListToNumberedString(meals), 
        breads=__convertListToNumberedString(breads), 
        mains=__convertListToNumberedString(mains), 
        veggies=__convertListToNumberedString(veggies), 
        sauces=__convertListToNumberedString(sauces), 
        topups=__convertListToNumberedString(topups), 
        sides=__convertListToNumberedString(sides)
    )


def __convertListToNumberedString(list_input):
    string = ""
    for item in list_input:
        string += "• {item}\n".format(item=item.capitalize().replace("_", " "))
    return string
    