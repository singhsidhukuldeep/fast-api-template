# sample function to get a prediction from the model
def getPrediction(text):
    if type(text) is str:
        return len(text)
    else:
        return -1
