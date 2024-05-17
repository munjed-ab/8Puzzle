
from django.http import JsonResponse
from django.shortcuts import render
import random
from .a_star import a_star

def index(request):
    return render(request, 'puzzle/index.html')

def shuffle(request):
    initial_state = list('12345678 ')
    random.shuffle(initial_state)
    state = ''.join(initial_state)
    return JsonResponse({'state': state})

def move(request):
    state = request.GET.get('state')
    tile = request.GET.get('tile')
    tile_idx = state.index(tile)
    empty_idx = state.index(' ')
    if abs(tile_idx - empty_idx) in [1, 3]:
        state = list(state)
        state[tile_idx], state[empty_idx] = state[empty_idx], state[tile_idx]
        state = ''.join(state)
    return JsonResponse({'state': state})

def solve(request):
    state = request.GET.get('state')
    goal_state = '12345678 '
    solution = a_star(state, goal_state)
    if solution:
        return JsonResponse({'solution': solution})
    else:
        return JsonResponse({'error': 'No solution found'})
