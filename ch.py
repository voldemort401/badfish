import pygame
import chess

class en:
    def __init__(self):
        self.board = chess.Board()
        self.rook = 5
        self.king = 10
        self.queen = 9
        self.knight = 4 
        self.bishop = 3
        self.pawn = 1 
        self.eval = 0.0
    def eva(self, move):
        if (self.board.is_legal(move)):
            if (self.board.is_en_passant(move)):
                self.eval += 100
                return self.eval 
            elif (self.board.is_check()):
                self.eval -= 0.2
                return self.eval 
            elif (self.board.gives_check(move)):
                self.eval += 0.5
                return self.eval
            elif (self.board.is_capture(move)):
                self.eval+=0.5
                return self.eval
            elif (str(move) == 'e2e4'):
                self.eval+=0.5
                return self.eval
            else:
                self.eval=0.0
                return self.eval

        else: 
            return 0

    def next_mv(self):
        legal_moves = self.board.legal_moves
        eval_moves = {}
        for i in legal_moves:
            eval_moves[str(i)] = self.eva(i)
        a = max(eval_moves,key=eval_moves.get)
        self.board.push_uci(a)
        print(self.board)
    def my_move(self): # WILL BE IMPROVED IN THE FUTURE
        move = input("enter the move in uci notation")
        try:
            self.board.push_uci(move)
            print(self.board)
        except Exception:
            print("Enter a valid input")


class ui:
    def __init__(self):
        self.size = self.w, self.h = (600,500)
        self.clock = pygame.time.Clock()
    def oninit(self):
        self.surface = pygame.display.set_mode(self.size)
        self.running = True
        self.background = "#A47449"
            
        self.bishop_black = pygame.image.load("res/chess-bishop-black.png").convert_alpha()
        self.bishop_white = pygame.image.load("res/chess-bishop-white.png").convert_alpha()    

        self.pawn_black   = pygame.image.load("res/chess-pawn-black.png").convert_alpha()
        self.pawn_white   = pygame.image.load("res/chess-pawn-white.png").convert_alpha()
 
        self.queen_black  = pygame.image.load("res/chess-queen-black.png").convert_alpha()
        self.queen_white  = pygame.image.load("res/chess-queen-white.png").convert_alpha()

        self.knight_black = pygame.image.load("res/chess-knight-black.png").convert_alpha()  
        self.knight_white = pygame.image.load("res/chess-knight-white.png").convert_alpha() 

        self.rook_black   = pygame.image.load("res/chess-rook-black.png").convert_alpha() 
        self.rook_white   = pygame.image.load("res/chess-rook-white.png").convert_alpha() 

        self.king_black   = pygame.image.load("res/chess-king-black.png").convert_alpha() 
        self.king_white   = pygame.image.load("res/chess-king-white.png").convert_alpha() 

        self.board        = pygame.image.load("res/board.png") 

    def iclock(self):
        pygame.display.flip()
        self.clock.tick(60)
    def pexit(self):
        pygame.quit()
    
    def event(self,event):
        if (event.type == pygame.QUIT):
            self.running = False
    
    def drawBoard(self):
        pygame.draw.circle(self.surface,"red", (0,0), 3 )

    def loop(self):
        # creating chess lines 
        self.surface.fill(self.background) 
        self.drawBoard()
        
    def execute(self):
        self.oninit()
        while (self.running):
            for event in pygame.event.get():
                self.event(event)
            self.loop()
            self.iclock()

if __name__ == "__main__":
    e = en()
    u = ui()
    
    u.execute()


#    while True:
#        exit = input("Would you like to exit")
#        if (exit == "yes"):
#            break
#        else:
#            (e.next_mv())
#            (e.my_move()) 
