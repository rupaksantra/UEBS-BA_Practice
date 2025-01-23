celcius = int(input("Enter Celcius Value : " ))

def C2F (celcius) :
    f = ((celcius * 1.8) + 32)

    return f

fahrenhite = C2F(celcius)

print (str(celcius) + " degree celcius is equals to " + str(fahrenhite))