from f_acmd import acmd
import time
#import TIMC_GUIrD

def isError(str, ser):
    #Returns a 1 if error, otherwise returns a zero
    if "!" in str:
        print("ERROR CODE = " + str)
        print("     Execution not successful")
        print("     Not valid command")
        print("     Argument missing or not valid")
        print(" ")
        return 1
    elif "#" in str:
        print("ERROR CODE = " + str)
        print("     Correct command but cannot execute sucessfully")
        print("     Task error generated")
        return 1
    elif "$" in str:
        print("ERROR CODE = " + str)
        print("     Command TIMEOUT")
        return 1
    elif str == "":
        print("ERROR: NO Serial Data")
        print("     Possible serial connection error")
        print("     Possible controller loss of power")
        time.sleep(3)
        print("\n\nProgram must now shutdown.")
        time.sleep(2)
        exit()
        return 1
    else:
        return 0
