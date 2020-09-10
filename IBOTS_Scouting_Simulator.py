import sys
from random import randint
from termcolor import colored, cprint

AvgCollectionTime = 3.0
ShootingTime = 4
CellCapacity = 5
CurrentCellsInRobot = 0
ShotAccuracy = 66.0
DefenseRating = 3  # A range of 1-5 on how effective a defender you are
DriverSkillRating = 7  # A range of 1 (Worst) to 10 (Best) of how good the driver is
CellsScored = 0
ClimbMinTime = 6  # min number of seconds to climb
ClimbPercentage = 80  # % of time climb is successful (remaining is park)





print("------------------------")
print("IBOTS Scouting Simulator")
print("------------------------\n")
print("Average Collection Time: ", AvgCollectionTime)
print("Shooting Time: ", ShootingTime)
print("Cell Capacity: ", CellCapacity)
print("Shot Accuracy: ", ShotAccuracy, "%")
print("\n")

print("Starting Match...")

MatchTime = 0


def GetNewTaskID():
    # Task IDs
    # 1 - Do nothing
    # 2 - Defense
    # 3 - Collect
    # 4 - Shoot
    # 5 - Climb
    SelectedTaskID = randint(1, 5)
    return SelectedTaskID


def PickATask():
    global CurrentCellsInRobot
    global MatchTime
    global CellsScored
    global task
    global DriverSkillRating

    # Make sure we get a valid task
    # i.e. Don't collect if full, or shoot if empty
    TaskValid = False
    while TaskValid == False:
        Task = GetNewTaskID()

        # Do Nothing
        if Task == 1:
            if DriverSkillRating < randint(0, 10):
                print(MatchTime, " | ", CurrentCellsInRobot, " | ", CellsScored, " |  \u001b[31mDOING NOTHING \u001b[0m")
                TaskValid = True
                MatchTime += 1
                break
            else:
              #  task = "\u001b[35mDOING Something \u001b[0m"
                TaskValid = False


        # Play Defense
        if Task == 2:
            print(MatchTime, " | ", CurrentCellsInRobot, " | ", CellsScored, " |  \u001b[36mPLAYING DEFENSE \u001b[0m")
            TaskValid = True
            MatchTime += 1

        # Cell Collection
        if Task == 3:
            if CurrentCellsInRobot >= CellCapacity:
                print("X - CANT COLLECT CELL - ROBOT IS FULL")
                TaskValid = False
            else:
                # print("Y - COLLECTING A CELL")
                TaskCollect()
                TaskValid = True

        # Shooting
        if Task == 4:
            if CurrentCellsInRobot < 1:
                print("X - CANT SHOOT - NO CELLS IN ROBOT")
                TaskValid = False
            else:
               # print("Y - SHOOTING CELLS")
                TaskShoot()
               # CurrentCellsInRobot = CurrentCellsInRobot - 1
               # CellsScored = CellsScored + 1
                TaskValid = True

        # Climb
        if Task == 5:
            if MatchTime < 125:
                # print("X - TOO EARLY TO CLIMB")
                TaskValid = False
            else:
                # print("Y - ATTEMPTING TO CLIMB")
                TaskClimb()
                TaskValid = True
                MatchTime += 1

def TaskClimb():
    global CurrentCellsInRobot
    global MatchTime
    global CellsScored
    global DriverSkillRating

    global ClimbMinTime  # min number of seconds to climb
    global ClimbPercentage  # % of time climb is successful (remaining is park)

    climbstatus = ""
    # if T < time to climb min - fail

    if ClimbMinTime <= (135 - MatchTime):
        if ClimbPercentage >= randint(0, 100):
            climbstatus = "Climb - \u001b[34mSuccess\u001b[0m"
        else:
            climbstatus = "Climb - \u001b[31mFailed, No Skills\u001b[0m"
        print(MatchTime, " | ", CurrentCellsInRobot, " | ", CellsScored, " | ", climbstatus)
    else:
        print(MatchTime, " | ", CurrentCellsInRobot, " | ", CellsScored, " |  Climb - \u001b[31mFailed, Not Enough Time\u001b[0m Needs:", ClimbMinTime, " Has:", (135 - MatchTime))
    for x in range(135 - MatchTime):
        MatchTime += 1
        print(MatchTime, " | ", CurrentCellsInRobot, " | ", CellsScored, " |  Finishing Climb")



def TaskDoNothing():
    global CurrentCellsInRobot
    global MatchTime
    global CellsScored
    global DriverSkillRating
    MatchTime += 1
    TimeCollect = randint(1, int(AvgCollectionTime * 2))
    print(MatchTime, " | ", CurrentCellsInRobot, " | ", CellsScored, " |  \u001b[31mDOING NOTHING \u001b[0m")

def TaskCollect():
    global CurrentCellsInRobot
    global MatchTime
    global CellsScored
    MatchTime += 1
    TimeCollect = randint(1, int(AvgCollectionTime * 2))
    print(MatchTime, " | ", CurrentCellsInRobot, " | ", CellsScored, " |  \u001b[34mCollecting Cells\u001b[0m (", TimeCollect, ")")
    if MatchTime + TimeCollect <= 135:
        CurrentCellsInRobot += 1
    for x in range(TimeCollect - 2):
        MatchTime += 1
        print(MatchTime, " | ", CurrentCellsInRobot, " | ", CellsScored, " |  \u001b[34mStill Collecting Cells\u001b[0m (", TimeCollect - x - 1 , ")")
    MatchTime += 1
    print(MatchTime, " | \u001b[32m", CurrentCellsInRobot, "\u001b[0m | ", CellsScored, " |  \u001b[34mCollected Cell - Hooray!\u001b[0m")

def TaskShoot():
    global CurrentCellsInRobot
    global CellsScored
    global MatchTime
    global ShotAccuracy
    if MatchTime + ShootingTime <= 135:

        for x in range(ShootingTime -1 ):
            MatchTime += 1
            print(MatchTime, " | ", CurrentCellsInRobot, " | ", CellsScored, " |  \u001b[33mShooting\u001b[0m (", ShootingTime - x, ")")
    MatchTime += 1
    # determine if scored
    if ShotAccuracy <= randint(0, 100):
        # score
        CurrentCellsInRobot -= 1
        CellsScored += 1
        print(MatchTime, " | ", CurrentCellsInRobot, " | \u001b[32m", CellsScored, "\u001b[0m |  \u001b[33mSCORE - \u001b[32mHooray!\u001b[0m", CellsScored)
    else:
        # miss
        CurrentCellsInRobot -= 1
        print(MatchTime, " | \u001b[31m", CurrentCellsInRobot, "\u001b[0m | ", CellsScored, " |  \u001b[33mMISS - \u001b[31mBOO!\u001b[0m", CellsScored)






def Robot_Full():
    RobotFull = False
    if CurrentCellsInRobot > CellCapacity - 1:
        RobotRobotFull = True
        print("ROBOT IS FULL")
    return Robot_Full


def Robot_Empty():
    RobotEmpty = False
    if CurrentCellsInRobot < 1:
        print("ROBOT IS EMPTY")
        RobotEmpty = True
    return Robot_Empty


while MatchTime < 136:


    PickATask()

