import math

from flask import Flask, render_template
from poker.game import Game


def card_to_svg_id(card):
    rank = card[0]
    suit = card[1].lower()

    if rank == "Ace":
        rank = "1"
    else:
        rank = rank.lower()

    return f"{suit}_{rank}"


def calculate_opponent_seats(players):
    seat_positions = [
        {"x": 50, "y": 10},

        {"x": 38, "y": 14},
        {"x": 62, "y": 14},

        {"x": 24, "y": 24},
        {"x": 76, "y": 24},

        {"x": 12, "y": 38},
        {"x": 88, "y": 38},

        {"x": 7, "y": 56},
        {"x": 93, "y": 56},
    ]

    position_orders = {
        1: [0],
        2: [1, 2],
        3: [0, 1, 2],
        4: [1, 2, 3, 4],
        5: [0, 1, 2, 3, 4],
        6: [1, 2, 3, 4, 5, 6],
        7: [0, 1, 2, 3, 4, 5, 6],
        8: [1, 2, 3, 4, 5, 6, 7, 8],
        9: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    }

    number_of_players = len(players)

    if number_of_players == 0:
        return []

    selected_positions = position_orders[number_of_players]

    seats = []

    for player, position_index in zip(players, selected_positions):
        position = seat_positions[position_index]

        seats.append({
            "player": player,
            "x": position["x"],
            "y": position["y"]
        })

    return seats


app = Flask(__name__)


@app.route("/")
def poker():
    game = Game()

    game.add_player("Jason")
    game.add_player("Bob")
    game.add_player("Alice")
    game.add_player("Mike")
    game.add_player("Sarah")
    game.add_player("Chris")
    game.add_player("Dave")
    game.add_player("Tom")
    game.add_player("Lisa")
    game.add_player("Steve")

    game.deal_hole_cards()

    player = game.players[0]
    opponents = game.players[1:]

    opponent_seats = calculate_opponent_seats(opponents)

    return render_template(
        "index.html",
        player=player,
        opponent_seats=opponent_seats,
        card_to_svg_id=card_to_svg_id
    )