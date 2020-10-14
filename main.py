import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLUE, BLACK,SCREEN_HEIGHT,SCREEN_WIDTH,VOILET
from checkers.game import Game
from minimax.algorithm import minimax
FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
WIN.fill(VOILET)

def get_row_col_from_mouse(pos):
	x, y = pos
	row = y // SQUARE_SIZE
	col = x // SQUARE_SIZE
	return row, col


def main():
	running = True
	game = Game(win=WIN)
	clock = pygame.time.Clock()
	while running:
		clock.tick(FPS)
		if game.turn == WHITE:
			value, new_board = minimax(game.get_board(), 4, WHITE, game)
			game.ai_move(new_board)
		if game.winner()!=None:
			print(game.winner())
			running=False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				row, col = get_row_col_from_mouse(pos)
				if col<8:
					game.select(row, col)
		game.update()
	pygame.quit()


if __name__ == '__main__':
	main()
