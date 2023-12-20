from app import app
from flask import request, render_template
from matrixFunctions import calcRank, calcReverse, calcSquare


@app.route('/', methods=['GET'])
def index():
    matrix_size = 3
    matrix = [[0 for j in range(matrix_size)] for i in range(matrix_size)]
    selected_operation_id = 0
    is_shown = False
    result = None

    if request.values.get('showButton') and request.values.get('sizeField') is not None:
        matrix_size = int(request.values.get('sizeField'))
        matrix = [[0 for j in range(matrix_size)] for i in range(matrix_size)]
    if request.values.get('clearButton'):
        matrix_size = 3
        matrix = [[0 for j in range(matrix_size)] for i in range(matrix_size)]
        selected_operation_id = 0
        is_shown = False
    if request.values.get('calculateButton'):
        selected_operation_id = int(request.values.get('matrixOperation'))
        matrix_size = int(request.values.get('sizeField'))
        matrix = [[int(request.values.get(f'field{i}_{j}')) for j in range(matrix_size)] for i in range(matrix_size)]
        print(matrix)
        is_shown = True
        if selected_operation_id == 0:
            result = calcSquare(matrix)
        elif selected_operation_id == 1:
            result = calcReverse(matrix)
        else:
            result = calcRank(matrix)

    html = render_template('calc.html',
                           str=str,
                           size=matrix_size,
                           selected=selected_operation_id,
                           matrix=matrix,
                           is_shown=is_shown,
                           result=result,
                           isinstance=isinstance)
    return html
