import sys
from random import randint

AvgCollectionTime = 3.0
AvgShootingTime = 3.5
CellCapacity = 5
CurrentCellsInRobot = 0
ShotAccuracy = 66.0
DefenseRating = 3   # A range of 1-5 on how effective a defender you are
DriverSkillRating = 7   # A range of 1 (Best) to 10 (Worst) of how good the driver is 
CellsScored = 0



print("------------------------")
print("IBOTS Scouting Simulator")
print("------------------------\n")
print("Average Collection Time: ", AvgCollectionTime)
print("Average Shooting Time: ", AvgShootingTime)
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
    SelectedTaskID = randint(1,5)
    return SelectedTaskID




def PickATask():
    global CurrentCellsInRobot
    global MatchTime
    global CellsScored


    # Make sure we get a valid task
    # i.e. Don't collect if full, or shoot if empty
    TaskValid=False
    while(TaskValid==False):
        Task = GetNewTaskID()

        # Do Nothing
        if(Task==1):
            print("Y - DOING NOTHING")
            TaskValid = True

        # Play Defense
        if(Task==2):
            print("Y - PLAYING DEFENSE")
            TaskValid = True

        # Cell Collection
        if(Task==3):
            if(CurrentCellsInRobot>CellCapacity):
                print("X - CANT COLLECT CELL - ROBOT IS FULL")
                TaskValid=False
            else:
                print("Y - COLLECTING A CELL")
                CurrentCellsInRobot=CurrentCellsInRobot+1
                TaskValid=True

        # Shooting
        if(Task==4):
            if(CurrentCellsInRobot<1):
                print("X - CANT SHOOT - NO CELLS IN ROBOT")
                TaskValid=False
            else:
                print("Y - SHOOTING CELLS")
                CurrentCellsInRobot =  CurrentCellsInRobot -1 
                CellsScored=CellsScored+1
                TaskValid=True

        # Climb
        if(Task==5):
                if(MatchTime < 125):
                    print("X - TOO EARLY TO CLIMB")
                    TaskValid=False
                else:        
                    print("Y - ATTEMPTING TO CLIMB")
                    TaskValid=True

        
        




def Robot_Full():
    RobotFull = False
    if(CurrentCellsInRobot > CellCapacity-1):
        RobotRobotFull = True
        print("ROBOT IS FULL")
    return Robot_Full


def Robot_Empty():
    RobotEmpty = False
    if(CurrentCellsInRobot < 1):
        print("ROBOT IS EMPTY")
        RobotEmpty = True
    return Robot_Empty



while MatchTime < 136:
    print("\nMatch time:",MatchTime)
    print("Current Cell count:",CurrentCellsInRobot)

    PickATask()    
    MatchTime+=1



