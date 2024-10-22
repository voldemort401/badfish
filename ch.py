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
        self.bord = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR - 0 1"
        self.size = self.rank, self.file = (8, 8)
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
        self.size = self.w, self.h = (600,600)
        self.clock = pygame.time.Clock()
    def oninit(self):
        self.surface = pygame.display.set_mode(self.size)
        self.running = True
        self.background = "#A47449"

        self.bishop_black = pygame.image.load("res/chess-bishop-black.png").convert_alpha()
        self.bishop_white = pygame.image.load("res/chess-bishop-white.png").convert_alpha()    
       
        self.bishop_black = pygame.transform.scale(self.bishop_black, (80,80))
        self.bishop_white = pygame.transform.scale(self.bishop_white, (80,80))
        
        self.pawn_black   = pygame.image.load("res/chess-pawn-black.png").convert_alpha()
        self.pawn_white   = pygame.image.load("res/chess-pawn-white.png").convert_alpha()
        
        self.pawn_white = pygame.transform.scale(self.pawn_white, (80,80))
        self.pawn_black = pygame.transform.scale(self.pawn_black, (80,80))

        self.queen_black  = pygame.image.load("res/chess-queen-black.png").convert_alpha()
        self.queen_white  = pygame.image.load("res/chess-queen-white.png").convert_alpha()

        self.queen_black = pygame.transform.scale(self.queen_black, (80,80))
        self.queen_white = pygame.transform.scale(self.queen_white, (80,80))
        
        self.knight_black = pygame.image.load("res/chess-knight-black.png").convert_alpha()  
        self.knight_white = pygame.image.load("res/chess-knight-white.png").convert_alpha() 

        self.knight_white = pygame.transform.scale(self.knight_white, (80,80))
        self.knight_black = pygame.transform.scale(self.knight_black, (80,80))
        
        self.rook_black   = pygame.image.load("res/chess-rook-black.png").convert_alpha() 
        self.rook_white   = pygame.image.load("res/chess-rook-white.png").convert_alpha() 

        self.rook_white = pygame.transform.scale(self.rook_white, (80,80))
        self.rook_black = pygame.transform.scale(self.rook_black, (80,80))
       
        self.king_black   = pygame.image.load("res/chess-king-black.png").convert_alpha() 
        self.king_white   = pygame.image.load("res/chess-king-white.png").convert_alpha() 

        self.king_white = pygame.transform.scale(self.king_white, (80,80))
        self.king_black = pygame.transform.scale(self.king_black, (80,80))
        
        self.board        = pygame.image.load("res/board.png").convert_alpha()
        self.board        = pygame.transform.scale(self.board, (self.w,self.h))
        

    def iclock(self):
        pygame.display.flip()
        self.clock.tick(60)
    def pexit(self):
        pygame.quit()

    def event(self,event):
        if (event.type == pygame.QUIT):
            self.running = False

    def drawBoard(self):
        ## Draw pieces and board 
        self.surface.blit(self.board) 
        self.surface.blit(self.rook_black)
        self.surface.blit(self.knight_black, (75,0))
        self.surface.blit(self.bishop_black, (150,0))
        self.surface.blit(self.queen_black,(225,0))
        self.surface.blit(self.king_black, (300,0)) 
        self.surface.blit(self.rook_black, (525,0))
        self.surface.blit(self.knight_black, (450,0))
        self.surface.blit(self.bishop_black, (375,0))

        self.surface.blit(self.pawn_white, (0,  65*6.65))
        self.surface.blit(self.pawn_white, (75, 65*6.65))
        self.surface.blit(self.pawn_white, (150,65*6.65))
        self.surface.blit(self.pawn_white, (225,65*6.65))
        self.surface.blit(self.pawn_white, (300,65*6.65)) 
        self.surface.blit(self.pawn_white, (525,65*6.65))
        self.surface.blit(self.pawn_white, (450,65*6.65))
        self.surface.blit(self.pawn_white, (375,65*6.65))
    
        self.surface.blit(self.pawn_black, (0,  65))
        self.surface.blit(self.pawn_black, (75, 65))
        self.surface.blit(self.pawn_black, (150,65))
        self.surface.blit(self.pawn_black, (225,65))
        self.surface.blit(self.pawn_black, (300,65)) 
        self.surface.blit(self.pawn_black, (525,65))
        self.surface.blit(self.pawn_black, (450,65))
        self.surface.blit(self.pawn_black, (375,65))


        self.surface.blit(self.rook_white, (0,65*7.85))
        self.surface.blit(self.knight_white, (75, 65*7.85))
        self.surface.blit(self.bishop_white, (150,65*7.85))
        self.surface.blit(self.queen_white,  (225,65*7.85))
        self.surface.blit(self.king_white,   (300,65*7.85)) 
        self.surface.blit(self.rook_white,   (525,65*7.85))
        self.surface.blit(self.knight_white, (450,65*7.85))
        self.surface.blit(self.bishop_white, (375,65*7.85))

        # TODO: make this array backed i'll do it tmrw. 
        square = pygame.Rect(20,20,8,8)
        pygame.draw.rect(self.surface, "green", square)
        j = 0
        i = 0
        while (j != 64):
            i+=1
            square.x += 72
            if (i == 8):
                i = 0
                square.y +=72
                square.x -= 72*8
            j+=1
            pygame.draw.rect(self.surface, "green", square)
        

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
    u = ui()

    u.execute()

#    while True:
#        exit = input("Would you like to exit")
#        if (exit == "yes"):
#            break
#        else:
#            (e.next_mv())
#            (e.my_move()) 
