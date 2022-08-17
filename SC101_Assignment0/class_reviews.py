"""
File: class_reviews.py
Name:李知穎
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for the class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

# The program will end immediately when the EXIT code is entered
EXIT = -1


def main():
    """
    TODO: This program will calculate the maximum, minimum, and average of the sc001 or sc101 score entered.
    """
    # the user will enter either sc001 or sc101 (case-insensitive)
    code = input("Which class? ")
    if code == str(EXIT):
        # id the user entered the EXIT code on first step, the program will print the following sentence and stop
        print("No class scores were entered")
    else:
        # the code sets the maximum, minimum, total, and the number of scores entered to its initial value
        sc001max = maximum(float('-inf'), float('-inf'))
        sc101max = maximum(float('-inf'), float('-inf'))
        sc001total = total(float('-inf'), float('-inf'))
        sc101total = total(float('-inf'), float('-inf'))
        sc001time = time(float('-inf'), float('-inf'))
        sc101time = time(float('-inf'), float('-inf'))
        sc001min = minimum(float('inf'), float('inf'))
        sc101min = minimum(float('inf'), float('inf'))
        # identify the class the user entered
        code = class_code(code)
        # the user will enter the score they got from the class they just entered
        score = int(input("Score: "))
        if code == "0":
            # if sc001 is entered, the score will be record under the sc001 category and undergo the following process
            sc001max = maximum(score, sc001max)
            sc001min = minimum(score, sc001min)
            sc001time = time(score, sc001time)
            sc001total = total(score, sc001total)
        else:
            # if sc101 is entered, the score will be record under the sc001 category and undergo the following process
            sc101max = maximum(score, sc101max)
            sc101min = minimum(score, sc101min)
            sc101time = time(score, sc101time)
            sc101total = total(score, sc101total)
    while not code == str(EXIT):
        # the program will continue if they did not enter the EXIT code on the first step
        code = input("Which class? ")
        if code == str(EXIT):
            # the program will print the result once the EXIT code is entered
            print("=============SC001=============")
            if sc001max == float('-inf'):
                print("No score for SC001")
            else:
                print("Max(001): " + str(sc001max))
                print("Min(001): " + str(sc001min))
                print("Avg(001): " + str(sc001total/sc001time))
            print("=============SC101=============")
            if sc101max == float('-inf'):
                print("No score for SC101")
            else:
                print("Max(101): " + str(sc101max))
                print("Min(101): " + str(sc101min))
                print("Avg(101): " + str(sc101total/sc101time))
            break
        code = class_code(code)
        score = int(input("Score: "))
        # everytime a new score is entered, the max, min, total, and number of scores will be update if necessary
        if code == "0":
            sc001max = maximum(score, sc001max)
            sc001min = minimum(score, sc001min)
            sc001time = time(score, sc001time)
            sc001total = total(score, sc001total)
        else:
            sc101max = maximum(score, sc101max)
            sc101min = minimum(score, sc101min)
            sc101time = time(score, sc101time)
            sc101total = total(score, sc101total)


def class_code(code):
    """
    :param code: either sc001 or sc101
    :return: 0 to represent sc001 or 1 to represent sc101
    """
    for ch in code:
        # the function will identify the right class base on the 3rd character
        if ch == "0":
            code = "0"
            return code
        elif ch == "1":
            code = "1"
            return code


def maximum(score, maximum1):
    """
   :param score: the score entered
   :param maximum1: the maximum of the sc001/ sc101 scores that were entered previously
   :return: the (updated) maximum value
   """
    if score == float('-inf'):
        # the user cannot enter -inf, therefore -inf is used to set the initial value
        maximum1 = score
        # the initial value of the score is negative infinity since negative infinity is less than any integer
    elif score > maximum1:
        # if the score entered is greater than the maximum, the maximum value will be updated
        maximum1 = score
    return maximum1


def minimum(score, minimum1):
    """
   :param score: the score entered
   :param minimum1: the minimum of the sc001/ sc101 scores that were entered previously
   :return: the (updated) minimum value
   """
    if score == float('inf'):
        # the user cannot enter inf, therefore inf is used to set the initial value
        minimum1 = score
        # the initial value of the score is infinity since infinity is greater than any integer
    elif score < minimum1:
        # if the score entered is less than the minimum, the minimum value will be updated
        minimum1 = score
    return minimum1


def total(score, total1):
    """
   :param score: the score entered
   :param total1: the total of the sc001/ sc101 scores that were entered previously
   :return: the (updated) total value
   """
    if score == float('-inf'):
        # the user cannot enter -inf, therefore -inf is used to set the initial value
        total1 = 0
        # no score was entered, therefore the total is 0
    else:
        # update the total value by adding the score entered
        total1 += score
    return total1


def time(score, time1):
    """
   :param score: the score entered
   :param time1: the number of the sc001/ sc101 scores that were entered previously
   :return: the (updated) times value
   """
    if score == float('-inf'):
        # the user cannot enter -inf, therefore -inf is used to set the initial value
        time1 = 0
        # no score has been entered, therefore the number of scores entered is 0
    else:
        time1 += 1
        # update the time value by adding 1 whenever a score is entered
    return time1


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
