import tkinter as tk
from typing import Iterable

from chessington.engine.data import Square
from chessington.ui.colours import Colour
from chessington.ui.images import ImageRepository
from chessington.engine.pieces import Pawn, Knight, Bishop, Rook, Queen, King

WINDOW_SIZE = 30

images = ImageRepository()

def promotion_window ( player ):

    window = tk.Tk()
    window.title('Promotion!')
    window.resizable(False, False)
    pieces = [Knight,Bishop,Rook,Queen]
    image_pieces = []
    for piece in pieces:
        piece.player = player
        image_pieces.append(images.get_image(piece, player))
    for idx,image in enumerate(image_pieces):
        label = tk.Label(window, image=image)
        label.grid(row=0,column=idx)
        label.bind('<Button-1>',lambda e,num=idx:on_image_click(num))

def on_image_click (image_number):
    return image_number

