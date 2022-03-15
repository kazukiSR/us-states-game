import pandas
import turtle
from writer import Writer

IMAGE_PATH = "blank_states_img.gif"

screen = turtle.Screen()
screen.setup(width=750, height=500)
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)
writer = Writer()

score = 0

data = pandas.read_csv("50_states.csv")
# Sets index to state names
dfStates = data.set_index("state")
# Transposes the DataFrame so state names are keys
stateDict = dfStates.T.to_dict("list")

gameOn = True
while gameOn:
    ans = screen.textinput(title=f"{score}/50 Correct", prompt="What's another state's name?")
    if ans is not None:
        answerState = ans.title()
        if answerState == "Exit":
            break
        if answerState in stateDict:
            score += 1
            writer.writeState(answerState, stateDict[answerState])
            stateDict.pop(answerState)
            if score == 50:
                gameOn = False
missingStates = {
    "States to Learn": stateDict.keys()
}
missingStatesData = pandas.DataFrame(missingStates)
print(missingStatesData)
missingStatesData.to_csv("States_To_Learn.csv")

screen.exitonclick()
