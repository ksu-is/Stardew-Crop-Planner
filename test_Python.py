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
    seed = input("Which seed are you planting? ")
    if seed.lower() in summer_fall_crops:
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        elif seed.lower() in spring_summer_crops: 
            print("You are planting",seed)
            season = input("Which season is it currently? ")
            elif seed.lower() in spring_crops:
                print("You are planting",seed)
                season = input("Which season is it currently? ")
                elif seed.lower() in summer_crops:
                    print("You are planting",seed)
                    season = input("Which season is it currently? ")
                    elif seed.lower() in fall_crops:
                        print("You are planting",seed)
                        season = input("Which season is it currently? ")
        if season.lower() in summer_fall:
            print("This crop is in season. \n")
            day = input("What day of the season is it? ")
        else:
            print("Not able to be planted in the current season")
            if day >= 14:
                print("It's too late in the season to plant",seed,". It will not yield any product.")
            elif day <= 9:
                print("You will receive 1 harvest and an extra re-growth harvest before the season ends (unless it is summer). ")
            else:
                print("You will only receive 1 harvest once the seeds fully grow (unless it is summer). ")

corn_wheat_sunflower_harvest()
