# 2-D NIM Game
import os
import random
############################### MY CODE ###############################
def discardChoice(chosenNumbers,chosen):
    if input("Do you want to clear? \n(y/n)")=='y' :
        chosenNumbers = []
    else:# player discards choice
        if chosen == 2 :
            chosenNumbers = [chosenNumbers[0]]
        else:
            chosenNumbers = chosenNumbers[:chosen]

def getDiag(table,dim):
    diag = []
    for i in range(dim):
        diag.append(table[(i+dim*i)+1])
    return diag
def playerInput(table, color, dim, diag):
    '''
    Den exw valei thn periptwsh na exei epileksei hdh epilegmeno
    '''
    submit = False
    row = False
    chosen = 0
    chosenNumbers = []

    while not submit :
        try :
            chosenNumbers.append(int(input("Choose a valid Cell :")))
            chosen=len(chosenNumbers)
            if chosenNumbers[chosen-1] in diag :# chosen cell is in diag
                if len(chosenNumbers)==1:# 1st cell is in diag
                    print("You have chosen a cell in the diag. \nYou can\'t choose another cell. \n")
                    if input("Do you want to proceed? \n(y/n)")=='y' :
                        submit = True
                    else:# player does not submit
                        submit = False
                        chosenNumbers = []
                else:# len(chosenNumbers) > 1
                    print("You have chosen a cell in the diag. \nThis is not a valid choice. \n")
                    discardChoice(chosenNumbers,chosen)
            else:
                if chosen > 1:
                    if chosen == 2 :# 2nd cell was chosen
                        if abs(chosenNumbers[0]-chosenNumbers[1]) == 1 :
                            row = True
                        elif abs(chosenNumbers[0]-chosenNumbers[1]) == dim :
                            row = False
                        else:# player discards choice
                            discardChoice(chosenNumbers,chosen)
                    else:# 3rd cell was chosen
                        if abs(chosenNumbers[1]-chosenNumbers[2]) == 1 and row :
                            return chosenNumbers
                        elif abs(chosenNumbers[1]-chosenNumbers[2]) == dim and not row :
                            return chosenNumbers
                        else:# player discards choice
                            discardChoice(chosenNumbers,chosen)
                else:
                    pass
        except ValueError :
            print("Choose a valid integer number")
        finally :
            chosenNumbers = []
    #endwhile
    #select the cells
    for i in chosenNumbers:
        table[i] = color

############################### FG COLOR DEFINITIONS ###############################
class bcolors:
    # pure colors...
    GREY      = '\033[90m'
    RED       = '\033[91m'
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    BLUE      = '\033[94m'
    BLUE      = '\033[94m'
    PURPLE    = '\033[95m'
    CYAN      = '\033[96m'
    # color styles...
    HEADER      = '\033[95m'
    QUESTION    = '\033[93m\033[3m'
    MSG         = '\033[96m'
    WARNING     = '\033[93m'
    ERROR       = '\033[91m'
    ENDC        = '\033[0m'    # RECOVERS DEFAULT TEXT COLOR
    BOLD        = '\033[1m'
    ITALICS     = '\033[3m'
    UNDERLINE   = '\033[4m'

    def disable(self):
        self.HEADER     = ''
        self.OKBLUE     = ''
        self.OKGREEN    = ''
        self.WARNING    = ''
        self.FAIL       = ''
        self.ENDC       = ''

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def initializeBoard(N):
        board = ['']*(N*N+1)

        # this is the COUNTER of cells in the board already filled with R or G
        board[0] = 0

        # each EMPTY cell in the board contains its cardinal number
        for i in range(N*N):
                if i < 9:
                        board[i+1] = ' ' + str(i+1)
                else:
                        board[i+1] = str(i+1)
        return board

def drawNimPalette(board,N):

        EQLINE          = '\t'
        MINUSLINE       = '\t'
        CONSECEQUALS    = ''
        CONSECMINUS     = ''
        for i in range(5):
                CONSECEQUALS    = CONSECEQUALS  + '='
                CONSECMINUS     = CONSECMINUS   + '-'

        for i in range(10):
                EQLINE          = EQLINE        + CONSECEQUALS
                MINUSLINE       = MINUSLINE     + CONSECMINUS

        for i in range(N):
                #PRINTING ROW i...
                if i == 0:
                        print(EQLINE)
                else:
                        print(MINUSLINE)

                printRowString = ''

                for j in range(N):
                        # PRINTING CELL (i,j)...
                        CellString = str(board[N*i+j+1])
                        if CellString == 'R':
                                CellString = ' ' + bcolors.RED + CellString + bcolors.ENDC

                        if CellString == 'G':
                                CellString = ' ' + bcolors.GREEN + CellString + bcolors.ENDC

                        if printRowString == '':
                                printRowString = '\t[ ' + CellString
                        else:
                                printRowString =  printRowString + ' | ' + CellString
                printRowString = printRowString + ' ]'
                print (printRowString)
        print ( EQLINE )
        print ( bcolors.PURPLE + '\t\t\tCOUNTER = [ ' + str(board[0]) + ' ]'  + bcolors.ENDC )
        print ( EQLINE )

def inputPlayerLetter():
        # The player chooses which label (letter) will fill the cells
        letter = ''
        while not(letter == 'G' or letter == 'R'):
                print ( bcolors.QUESTION + '[Q1] What letter do you choose to play? [ G(reen) | R(ed) ]' + bcolors.ENDC )
                letter = input().upper()
                # The first letter corresponds to the HUMAN and the second element corresponds to the COMPUTER
                if letter == 'G':
                        return ['G','R']
                else:
                        if letter == 'R':
                                return ['R','G']
                        else:
                                print (bcolors.ERROR + 'ERROR1: You provided an invalid choice. Please try again...' + bcolors.ENDC)


def whoGoesFirst():
        if random.randint(0,1) == 0:
                return 'computer'
        else:
                return 'player'

def howComputerPlays():

        while True:
                print ( bcolors.QUESTION + '[Q5] How will the computer play? [ R (randomly) | F (first Free) | C (copycat)]' + bcolors.ENDC )
                strategyLetter = input().upper()

                if strategyLetter == 'R':
                        return 'random'
                else:
                        if strategyLetter == 'F':
                                return 'first free'
                        else:
                                if strategyLetter == 'C':
                                        return 'copycat'
                                else:
                                        print( bcolors.ERROR + 'ERROR 3: Incomprehensible strategy was provided. Try again...' + bcolors.ENDC )

def getBoardSize():

        BoardSize = 0
        while BoardSize < 1 or BoardSize > 10:
                GameSizeString = input('Determine the size 1 =< N =< 10, for the NxN board to play: ')
                if GameSizeString.isdigit():
                        BoardSize = int(GameSizeString)
                        if BoardSize < 1 or BoardSize > 10:
                                print( bcolors.ERROR + 'ERROR 4: Only positive integers between 1 and 10 are allowable values for N. Try again...' + bcolors.ENDC )
                else:
                        print( bcolors.ERROR + 'ERROR 5: Only positive integers between 1 and 10 are allowable values for N. Try again...' + bcolors.ENDC )
        return( BoardSize )

def startNewGame():
        # Function for starting a new game
        print(bcolors.QUESTION + '[Q0] Would you like to start a new game? (yes or no)' + bcolors.ENDC)
        return input().lower().startswith('y')

def continuePlayingGame():
        # Function for starting a new game
        print(bcolors.QUESTION + '[Q2] Would you like to continue playing this game? (yes or no)' + bcolors.ENDC)
        return input().lower().startswith('y')

def playAgain():
        # Function for replay (when the player wants to play again)
        print(bcolors.QUESTION + '[Q3] Would you like to continue playing this game? (yes or no)' + bcolors.ENDC)
        return input().lower().startswith('y')

def isBoardFull(board,N):
        return board[0] == N*N

######### MAIN PROGRAM BEGINS #########
screen_clear()

print(bcolors.HEADER + """
---------------------------------------------------------------------
                     CEID NE509 / LAB-1
---------------------------------------------------------------------
STUDENT NAME:           < Alexios Ntavlouros >
STUDENT AM:             < 1059653 >
JOINT WORK WITH:        < - >
---------------------------------------------------------------------
""" + bcolors.ENDC)

input("Press ENTER to continue...")
screen_clear()

print(bcolors.HEADER + """
---------------------------------------------------------------------
                     2-Dimensional NIM Game: RULES (I)
---------------------------------------------------------------------
    1.      A human PLAYER plays against the COMPUTER.
    2.      The starting position is an empty NxN board.
    3.      One player (the green) writes G, the other player
                (the red) writes R, in empty cells.
""" + bcolors.ENDC )

input("Press ENTER to continue...")
screen_clear()

print(bcolors.HEADER + """
---------------------------------------------------------------------
                     2-Dimensional NIM Game: RULES (II)
---------------------------------------------------------------------
    4.      The cells within the NxN board are indicated as
            consecutive numbers, from 1 to N^2, starting from the
            upper-left cell. E.g. for N=4, the starting position
            and some intermediate position of the game would be
            like those:
                    INITIAL POSITION        INTERMEDIATE POSITION
                    =====================   =====================
                    [  1 |  2 |  3 |  4 ]   [  1 |  2 |  3 |  4 ]
                    ---------------------   ---------------------
                    [  5 |  6 |  7 |  8 ]   [  5 |  R |  7 |  8 ]
                    ---------------------   ---------------------
                    [  9 | 10 | 11 | 12 ]   [  9 |  R | 11 | 12 ]
                    ---------------------   ---------------------
                    [ 13 | 14 | 15 | 16 ]   [  G |  G | 15 |  G ]
                    =====================   =====================
                       COUNTER = [ 0 ]         COUNTER = [ 5 ]
                    =====================   =====================
""" + bcolors.ENDC )

input("Press ENTER to continue...")
screen_clear()

print(bcolors.HEADER + """
---------------------------------------------------------------------
                     2-Dimensional NIM Game: RULES (III)
---------------------------------------------------------------------
    5.      In each round the current player's turn is to fill with
            his/her own letter (G or R) at least one 1 and at most
            3 CONSECUTIVE, currently empty cells of the board, all
            of them lying in the SAME ROW, or in the SAME COLUMN
            of the board. Alternatively, the player may choose ONLY
            ONE empty diagonal cell to play.
    6.      The player who fills the last cell in the board WINS.
    7.      ENJOY!!!
---------------------------------------------------------------------
""" + bcolors.ENDC)


maxNumMoves = 3

playNewGameFlag = True

while playNewGameFlag:

        if not startNewGame():
                break
        N = getBoardSize()

        nimBoard = initializeBoard(N)
        diag = getDiag(nimBoard,N)

        playerLetter, computerLetter = inputPlayerLetter()

        turn = whoGoesFirst()

        computerStrategy = howComputerPlays()

        print( bcolors.MSG + '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'    + bcolors.ENDC )
        print( bcolors.MSG + 'A new ' +str(N) +'x' + str(N) +' game is about to start. The ' + turn + ' makes the first move.' + bcolors.ENDC )
        print( bcolors.MSG + ' * The computer will play according to the ' + bcolors.HEADER + computerStrategy + bcolors.MSG +' strategy.' + bcolors.ENDC )
        print( bcolors.MSG + ' * The player will use the letter ' + playerLetter + ' and the computer will use the ' + computerLetter +'.' + bcolors.ENDC )
        print( bcolors.MSG + ' * The first move will be done by the ' + turn +'.' + bcolors.ENDC )
        print( bcolors.MSG + '---------------------------------------------------------------------'    + bcolors.ENDC )
        print( bcolors.MSG + 'Provide your own code here, to implement the workflow of the game:'       + bcolors.ENDC )
        print( bcolors.MSG + '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'    + bcolors.ENDC )
        drawNimPalette(nimBoard,N)
        # My code
        while 1 :
            if turn == 'computer':# computer turn
                turn='player'
                input("a")
            else:# player turn
                turn='computer'
                input("b")


######### MAIN PROGRAM ENDS #########