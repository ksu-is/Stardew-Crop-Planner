seasons = ['spring','summer','fall',"winter"]
two_season_crop = ['summer','fall']
ancient_seeds = ['spring','summer','fall']


#Creating function to calculate plant growth time for corn, wheat and sunflowers because they are able to be grown in Summer and Fall which is unique

def corn_wheat_sunflower_harvest():
    seed = input("Which seed are you planting? ")
    if seed.lower() == "corn":
        print("You are planting",seed)
        season = input("Which season is it currently? ")
        if season.lower() in two_season_crop:
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
