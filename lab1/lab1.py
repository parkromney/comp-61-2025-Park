temperature=input("Hello, what is the temperature in your area? (just enter the number): ")
budget=input("What is your budget for the day? (just enter the number): ")
weatherCondition=input("Is it sunny, rainy, or cloudy right now? (enter in all lowercase): ")
sunny=str("sunny")
rainy=str("rainy")
cloudy=str("cloudy")

if(weatherCondition==str("sunny")) and ((int(temperature)) > 75):
    if((float(budget)) > 20):
        print('Go to the beach!')
    else:
        print('Have a nice picnic in the park.')

if(weatherCondition==str("rainy")):
    if((float(budget)) > 15):
        print('You should visit a museum!')
    else:
        print('You should stay in and watch a movie at home.')

if(weatherCondition==str("cloudy")) or (int(temperature) < 60):
    print('Go to a coffee shop and enjoy a warm drink.')