
def bmi_calculator():
    isMetric = input("Calculate BMI in Metric units?\n")
    [massMultiplier, heightMultiplier, massUnit, heightUnit] = [1, 1, "kg", "metre"] if (
        isMetric == ("yes" or "Yes")) else [0.4536, 0.0254, "lbs", "inches"]
    userMass = float(input("What is your mass in "+massUnit+"?:\n"))
    userHeight = float(input("What is your height in "+heightUnit+"?:\n"))
    print("Your bmi is "+str(round(userMass*massMultiplier /
          ((userHeight*heightMultiplier)**2),2))+massUnit+"/"+heightUnit+"^2")
    bmi_calculator() if (input("restart BMI calculator?:\n")
                         == ("yes" or "Yes")) else exit()


bmi_calculator()
