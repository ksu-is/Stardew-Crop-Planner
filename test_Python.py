seasons = ['spring','summer','fall','winter']
spring = ['spring']
summer = ['summer']
fall = ['fall']
winter = ['winter']
summer_fall = ['summer','fall']
spring_summer = ['spring','summer']
ancient_seeds = ['spring','summer','fall']
summer_fall_crops = ['corn','wheat','sunflower']
spring_summer_crops = ['coffee beans']
spring_crops = ['blue jazz','cauliflower','garlic','green bean','kale','parsnip','potato','rhubarb','strawberry','tulip','unmilled rice']
summer_crops = ['blueberry','hops','hot pepper','melon','poppy','radish','red cabbage','starfruit','summer spangle','tomato']
fall_crops = ['amaranth','artichoke','beet','bok choy','cranberries','eggplant','fairy rose','grape','pumpkin','yam']
special_crops = ['ancient fruit','cactus fruit','pineapple','qi fruit','sweet gem berry','taro root','tea leaves']


#Creating function to calculate plant growth time for corn, wheat and sunflowers because they are able to be grown in Summer and Fall which is unique

def corn_wheat_sunflower_harvest():
    seed = input("Enter the seed of which you are planting? (or enter 'quit' to exit) ")
    if seed.lower() in summer_fall_crops:
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "summer":
            print("This crop is in season.") 
            day = input("What day of the season is it? ")
        elif season.lower() == "fall":
            print("This crop is in season.")
            day = input("What day of the season is it? ")
        else: 
            print("It is not the season to plant and grow these seeds. ")
    elif seed.lower() in spring_summer_crops: 
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "spring":
            print("This crop is in season.")
            day = input("What day of the season is it? ")
        elif season.lower() == "summer": 
            print("This crop is in season.")
            day = input("What day of the season is it? ")
        else:
            print("It is not the season to plant and grow these seeds. ")
    elif seed.lower() in spring_crops:
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "spring":
            print("This crop is in season. ")
            day = input("What day of the season is it? ")
        else: 
            print("It is not the season to plant and grow these seeds. ")
    elif seed.lower() in summer_crops:
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "summer": 
            print("This crop is in season. ") 
            day = input("What day of the season is it? ")
        else: 
            print("Is is not the season to plant and grow these seeds")
    elif seed.lower() in fall_crops:
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "fall":
            print("This crop is in season. ") 
            day = input("What day of the season is it? ")
        else: 
            print("Is is not the season to plant and grow these seeds")
    elif seed.lower() in special_crops: 
        print("You are planting", seed)
        season = input("Which season is it currently? ")
    elif seed.lower() == "quit": 
        return
    else:
        print("Unrecognized seed: check spelling and try again. ")
        corn_wheat_sunflower_harvest() 



corn_wheat_sunflower_harvest()
