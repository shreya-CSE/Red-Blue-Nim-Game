import sys

def print_game_state(maximizing_player,num_red, num_blue):
    print(f"Player : {maximizing_player} --->  Red :{num_red} | Blue :{num_blue}")

def get_computer_move(num_red, num_blue,version,depth,depth_limit):
    best_move = None
    best_eval = -sys.maxsize
    alpha = -sys.maxsize
    beta = sys.maxsize
#    print_game_state(True,num_red,num_blue)
    if depth_limit == True:
        depth = depth -1
    if version == "Misere":
        val = minmax(num_red -1 , num_blue ,alpha,beta, version, depth,depth_limit, False)
        if val > best_eval:
            best_eval = val
            best_move = "red"
        if val >= beta:
            return best_move
        else:
            alpha = max(val, alpha)

 #   print_game_state(True,num_red,num_blue)
    val = minmax(num_red, num_blue -1 , alpha, beta,version , depth,depth_limit, False)
    if val > best_eval:
        best_eval = val
        best_move = "blue" 

    if val >= beta:
         return best_move
    else:
         alpha = max(val, alpha)
    if version == "Standard" :
        val = minmax(num_red -1 , num_blue , alpha, beta,version, depth ,depth_limit, False)
        if val > best_eval:
            best_eval = val
            best_move = "red"

        if val >= beta:
            return best_move
        else:
           alpha = max(val, alpha)

    return best_move

def get_utility(num_red, num_blue ,version):
    if num_red == 0 and num_blue == 0 :
        utility = 0
    elif num_red == 0:
        utility = num_blue*3
    elif num_blue == 0:
        utility = num_red*2
    if version == "Misere":
        return utility
    else :
        return -utility

def minmax(num_red, num_blue,alpha,beta, version, depth,depth_limit , maximizing_player):
    if (depth_limit == True and depth > 0):
        depth = depth -1
        if (depth == 0 ):
            if(maximizing_player):
                utility = max ( num_red * 2, num_blue*3) 
            else :
                utility = min(num_red*2, num_blue*3)
            return utility    
    elif(num_red == 0 or num_blue == 0): 
        utility = get_utility(num_red,num_blue,version)
        return utility
    i = 1
    if maximizing_player:
                    
        max_eval = -sys.maxsize
        if version == "Misere":
         #   print_game_state(maximizing_player,num_red,num_blue)
            max_eval = max(max_eval, minmax(num_red - i, num_blue,alpha, beta,version,depth, depth_limit,False))
            alpha = max(alpha, max_eval)
            if (max_eval >= beta):
                return max_eval
             
        #print_game_state(maximizing_player,num_red,num_blue)
        max_eval = max(max_eval, minmax(num_red, num_blue-i,alpha, beta,version,depth,depth_limit,False))
        alpha = max(alpha, max_eval)
        
        if (max_eval >= beta):
            return max_eval

        if version == "Standard" :
            #print_game_state(maximizing_player,num_red,num_blue)
            max_eval = max(max_eval,minmax(num_red-i,num_blue,alpha,beta,version,depth,depth_limit,False))        
            alpha = max(alpha, max_eval)
            if (max_eval >= beta):
                return max_eval

        return max_eval
    else:
        min_eval = sys.maxsize
        if version == "Misere" :
        #    print_game_state(maximizing_player,num_red,num_blue)
            min_eval = min(min_eval,minmax(num_red-i, num_blue,alpha, beta,version,depth,depth_limit,True))
            beta = min(beta, min_eval)
            if(min_eval <= alpha):
                return min_eval


        #print_game_state(maximizing_player,num_red,num_blue)
        min_eval = min(min_eval,minmax(num_red, num_blue-i, alpha,beta,version,depth,depth_limit,True))
        beta = min(beta, min_eval)
        if(min_eval <= alpha):
            return min_eval
        if version == "Standard":
        #    print_game_state(maximizing_player,num_red,num_blue)
            min_eval = min(min_eval,minmax(num_red-i, num_blue,alpha, beta, version,depth,depth_limit,True))
            beta = min(beta, min_eval)
            if(min_eval <= alpha):
                return min_eval

        return min_eval



def RedBlueNim(num_red, num_blue,version,depth,first_player):
    if(depth == 0):
        depth_limit = False
    else: 
        depth_limit = True    
    current_player = first_player
    while(num_red > 0 and num_blue > 0 and ((depth >0 and depth_limit == True)or(depth_limit == False and depth == 0))):
        print(f" red_balls  = {num_red} , blue_balls = {num_blue}")
        print(f"\n {current_player}'s turn {depth}")
        if current_player == "Computer":
            color_selected = get_computer_move(num_red,num_blue,version,depth,depth_limit)
            if color_selected == "red" :
                num_red -= 1
            else: 
                num_blue -= 1
            print(f"Computer removed one ball from {color_selected} ")
        else:

            sel_color = input("choose a color to remove from :").lower()
            while sel_color  not in ["red", "blue"]:
                print("Invalid choice. Please choose either Red or Blue.")
                sel_color = input("Choose a color (Red/Blue): ").lower()
            
            if sel_color == "red":
                num_red -= 1
            else:
                num_blue -= 1
            print(f"Human removed one ball  from {sel_color} .")
        if depth > 0:
            depth = depth - 1
        current_player = "Computer" if current_player == "Human" else "Human"
    print("\nGame Results")

    print(f" red_balls  = {num_red} , blue_balls = {num_blue}")
    score = num_red * 2 + num_blue * 3  
    if version == "Misere":
        print(f"Version : {version} , {current_player}, wins by {score}")
    else:
        print(f"Version = {version} ,{current_player}, loses by {score}")

def print_error ():
    print("Usage :red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>")
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3 :
        print("Usage :red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>")
        sys.exit(1)

    if len(sys.argv) == 3 :
        num_red = int(sys.argv[1])
        num_blue = int(sys.argv[2])
        version = "Standard"
        first_player = "Computer"
        depth = 0
    elif len(sys.argv) == 4:
        num_red = int(sys.argv[1])
        num_blue = int(sys.argv[2])
        depth = 0 
        if((sys.argv[3] == "Standard") or (sys.argv[3] == "Misere")):
            version = sys.argv[3]
            first_player = "Computer"
        elif((sys.argv[3] == "Computer") or (sys.argv[3] == "Human")):
            first_player = sys.argv[3]
            version = "Standard"
    elif len(sys.argv) == 5:
        num_red = int(sys.argv[1])
        num_blue = int(sys.argv[2])
        depth = 0
        if((sys.argv[3] == "Standard") or (sys.argv[3] == "Misere")):
            version = sys.argv[3]
        else: 
            print_error()        
        if((sys.argv[4] == "Computer") or (sys.argv[4] == "Human")):
            first_player = sys.argv[4]
        else :
            print_error()
    elif len(sys.argv) == 6:
        num_red = int(sys.argv[1])
        num_blue = int(sys.argv[2])
        depth = int(sys.argv[5])
        if((sys.argv[3] == "Standard") or (sys.argv[3] == "Misere")):
            version = sys.argv[3]
        else: 
            print_error()        
        if((sys.argv[4] == "Computer") or (sys.argv[4] == "Human")):
            first_player = sys.argv[4]
        else :
            print_error()
    else:
        print_error()
    print("num_red = ",num_red, "num_blue = ", num_blue , "version = " , version, " first_player = " , first_player, "depth = " ,depth) 
    game = RedBlueNim(num_red,num_blue,version,depth, first_player)    


