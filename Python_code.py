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
spring_crops = ['blue jazz','cauliflower','coffee bean','garlic','green bean','kale','parsnip','potato','rhubarb','strawberry','tulip','unmilled rice']
summer_crops = ['blueberry','hops','hot pepper','melon','poppy','radish','red cabbage','starfruit','summer spangle','tomato','corn','wheat','sunflower']
fall_crops = ['amaranth','artichoke','beet','bok choy','cranberries','eggplant','fairy rose','grape','pumpkin','yam','corn','wheat','sunflower']



#Creating function to calculate plant growth time for corn, wheat and sunflowers because they are able to be grown in Summer and Fall which is unique

def corn_wheat_sunflower_harvest():
    seed = input("Enter the seed of which you are planting? (or enter 'quit' to exit) ")
    if seed.lower() in summer_fall_crops:
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "summer":
            print("This crop is in season.") 
            if seed.lower().startswith('cor'):
                print('If it is before the 14th, then you will receive one harvest plus 6-7 re-growths in the fall. (14 day growth + 4 day regrowth)')
            elif seed.lower().startswith('whe'):
                print('If it is before the 25th, you will receive one harvest (4 day growth)')
            elif seed.lower().starts('sun'):
                print('As long as it is before the 20th, you will receive one harvest for summer.')
        elif season.lower() == "fall":
            print("This crop is in season.")
            if seed.lower().startswith('cor'):
                print('If it is before the 14th, then you will receive one harvest. (14 day growth + 4 day regrowth)')
            elif seed.lower().startswith('whe'):
                print('If it is before the 24th, you will receive one harvest (4 day growth)')
            elif seed.lower().starts('sun'):
                print('As long as it is before the 20th, you will receive one harvest for the fall.')
        else: 
            print("It is not the season to plant and grow these seeds. ")
    elif seed.lower() in spring_summer_crops: 
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "spring":
            print("This crop is in season.")
            if seed.lower().startswith('coff'):
                print('If it is before the 18th, you will receive one harvest before end of season. (10 day growth + 2 day regrowth)')
        elif season.lower() == "summer": 
            print("This crop is in season.")
            print('If it is before the 18th, you will receive one harvest before end of season. (10 day growth + 2 day regrowth)')
        else:
            print("It is not the season to plant and grow these seeds. ")
    elif seed.lower() in spring_crops:
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "spring":
            print("This crop is in season. ")
            if seed.lower().startswith('blue'):
                print('As long as it is before the 21st, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('cauli'):
                print('As long as it is before the 16th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('coffee'):
                print('If it is before the 18th, you will receive one harvest before end of season. (10 day growth + 2 day regrowth)')
            elif seed.lower().startswith('garl'): 
                print('As long as it is before the 24th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('green'):
                print('As long as it is before the 18thth, this crop will fully grow before end of the season. (10 day growth + 3 day regrowth)')
            elif seed.lower().startswith('kal'):
                print('As long as it is before the 22th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('pars'):
                print('As long as it is before the 24thth, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('pota'):
                print('As long as it is before the 22nd, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('rhub'):
                print('As long as it is before the 15th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('straw'):
                print('As long as it is before the 20th, this crop will fully grow before end of the season. (8 day growth + 4 day regrowth)')
            elif seed.lower().startswith('tuli'):
                print('As long as it is before the 22nd, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('unmill'):
                print('As long as it is before the 20th, this crop will fully grow before end of the season.')
        else: 
            print("It is not the season to plant and grow these seeds. ")
    elif seed.lower() in summer_crops:
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "summer": 
            print("This crop is in season. ") 
            if seed.lower().startswith('bluebe'):
                print('As long as it is before the 15th, this crop will fully grow before end of season. (13 day growth + 4 day regrowth)')
            elif seed.lower().startswith('coffee'):
                print('As long as it is before the 18th, this crop will fully grow before end of the season. (10 day growth + 2 day regrowth)')
            elif seed.lower().startswith('cor'):
                print('As long as it is before the 14th, this crop will fully grow before end of the season. (14 day growth + 4 day regrowth)')
            elif seed.lower().startswith('hop'):
                print('As long as it is before the 17th, this crop will fully grow before end of the season. (11 day growth + 1 day regrowth)')
            elif seed.lower().startswith('hot'):
                print('As long as it is before the 23rd, this crop will fully grow before end of the season. (5 day growth + 3 day regrowth)')
            elif seed.lower().startswith('melo'):
                print('As long as it is before the 16th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('popp'):
                print('As long as it is before the 21st, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('radis'):
                print('As long as it is before the 22nd, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('red ca'):
                print('As long as it is before the 19th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('starf'):
                print('As long as it is before the 15th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('summer'):
                print('As long as it is before the 20th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('sunf'):
                print('As long as it is before the 20th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('toma'):
                print('As long as it is before the 17th, this crop will fully grow before end of the season. (11 day growth + 4 day regrowth)')
            elif seed.lower().startswith('whea'):
                print('As long as it is before the 24th, this crop will fully grow before end of the season.')
        else: 
            print("Is is not the season to plant and grow these seeds")
    elif seed.lower() in fall_crops:
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() == "fall":
            print("This crop is in season. ") 
            if seed.lower().startswith('amara'):
                print('As long as it is before the 21st, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('artic'):
                print('As long as it is before the 20th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('bee'):
                print('As long as it is before the 22nd, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('bok'):
                print('As long as it is before the 24th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('corn'):
                print('As long as it is before the 14th, this crop will fully grow before end of the season. (14 day growth + 4 day regrowth)')
            elif seed.lower().startswith('cranb'):
                print('As long as it is before the 21st, this crop will fully grow before end of the season. (7 day growth + 5 day regrowth)')
            elif seed.lower().startswith('eggp'):
                print('As long as it is before the 23rd, this crop will fully grow before end of the season. (5 day growth + 5 day regrowth)')
            elif seed.lower().startswith('fairy'):
                print('As long as it is before the 16th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('cauli'):
                print('As long as it is before the 18th, this crop will fully grow before end of the season. (10 day growth + 5 day regrowth)')
            elif seed.lower().startswith('pump'):
                print('As long as it is before the 15th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('sunfl'):
                print('As long as it is before the 20th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('whea'):
                print('As long as it is before the 24th, this crop will fully grow before end of the season.')
            elif seed.lower().startswith('yam'):
                print('As long as it is before the 18th, this crop will fully grow before end of the season.')
        else: 
            print("Is is not the season to plant and grow these seeds")
    elif seed.lower() == "quit": 
        return
    else:
        print("Unrecognized seed: check spelling and try again. ")
corn_wheat_sunflower_harvest() 



corn_wheat_sunflower_harvest()
