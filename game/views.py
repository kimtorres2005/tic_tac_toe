from django.shortcuts import render, redirect
from .models import Player

def home(request):
    # Fetch top 5 players from the database
    top_players = Player.objects.order_by('-wins')[:5]
    
    return render(request, 'game/home.html', {
        'top_players': top_players,
    })

def game(request):
    if request.method == 'POST':
        # Handle player names
        player1_name = request.POST.get('player1')
        player2_name = request.POST.get('player2')
        
        # Fetch players from the database, or create them if they don't exist
        player1, created1 = Player.objects.get_or_create(name=player1_name)
        player2, created2 = Player.objects.get_or_create(name=player2_name)

        # Store player names in session
        request.session['player1'] = player1.name
        request.session['player2'] = player2.name

        # Clear the game board and reset current player
        request.session['board'] = [' ' for _ in range(9)]  # Reset the board
        request.session['current_player'] = 'X'  # Reset to Player X

        # Redirect to the game board
        return redirect('play_game')

    return render(request, 'game/start_game.html')

def play_game(request):
    # Initialize the game board and current player
    if 'board' not in request.session:
        request.session['board'] = [' ' for _ in range(9)]
        request.session['current_player'] = 'X'  # Player X starts

    board = request.session['board']
    current_player = request.session['current_player']
    indices = list(range(9))  # Create a list of indices from 0 to 8

    # Get player names from the session
    player1_name = request.session.get('player1', 'Player 1')
    player2_name = request.session.get('player2', 'Player 2')

    winner = check_winner(board, player1_name, player2_name)  # Pass player names to check_winner
    is_draw = check_draw(board, player1_name, player2_name)  # Pass player names to check_draw

    if request.method == 'POST':
        if 'reset' in request.POST:
            # Reset the game board and current player, but keep player names
            request.session['board'] = [' ' for _ in range(9)]
            request.session['current_player'] = 'X'  # Reset to Player X
            return redirect('play_game')  # Stay on the same page

        index = int(request.POST.get('index'))

        if board[index] == ' ' and winner is None and not is_draw:
            board[index] = current_player
            request.session['board'] = board
            
            winner = check_winner(board, player1_name, player2_name)
            is_draw = check_draw(board, player1_name, player2_name)

            # If there's a winner, update the player's stats
            if winner:
                try:
                    player = Player.objects.get(name=winner)
                    player.wins += 1
                    player.save()
                    print(f"{winner} wins! Total wins: {player.wins}")
                except Player.DoesNotExist:
                    print(f"Player not found: {winner}")
            else:
                # Switch players only if no winner or draw
                request.session['current_player'] = 'O' if current_player == 'X' else 'X'

    # Determine current player's name based on the current player symbol
    current_player_name = player1_name if request.session['current_player'] == 'X' else player2_name

    return render(request, 'game/play_game.html', {
        'board': board,
        'current_player': request.session['current_player'],
        'indices': indices,
        'winner': winner,
        'is_draw': is_draw,
        'player1': player1_name,
        'player2': player2_name,
        'current_player_name': current_player_name,
    })

def check_winner(board, player1_name, player2_name):
    # Define winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            if board[combination[0]] == 'X':
                return player1_name  # Return player 1's name
            elif board[combination[0]] == 'O':
                return player2_name  # Return player 2's name

    return None  # No winner yet

def check_draw(board, player1_name, player2_name):
    return ' ' not in board and check_winner(board, player1_name, player2_name) is None
