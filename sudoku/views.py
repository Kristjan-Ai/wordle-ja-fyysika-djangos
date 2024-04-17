from django.shortcuts import render
from django.http import HttpResponse
import random

def sudoku(request):
    return render(request, 'sudoku.html', {'field': [], 'i':  0})

# field on terve ruudustik
# row on ruudustiku rida (väärtuses 0-8)
# row koosneb 3st subrow'st (väärtuses 0-2)
# field koosneb 3st block'ist, iga block on 3x3 ruudustik
# block koosneb 3st subrow'st, mis asetsevad üksteise kohal
# visuaalselt on seda kergem ette kujutada, kui vaadata field'i listi create_field()'i all
# block() tagastab field'ist kindla block'i listina, kui on teada row ja subrow
def block(field, row, subrow):
    if row >= 0 and row <= 2:
        if subrow == 0:
            block = field[0][0] + field[1][0] + field[2][0]
        elif subrow == 1:
            block = field[0][1] + field[1][1] + field[2][1]
        elif subrow == 2:
            block = field[0][2] + field[1][2] + field[2][2]
    elif row >= 3 and row <= 5:
        if subrow == 0:
            block = field[3][0] + field[4][0] + field[5][0]
        elif subrow == 1:
            block = field[3][1] + field[4][1] + field[5][1]
        elif subrow == 2:
            block = field[3][2] + field[4][2] + field[5][2]
    elif row >= 6 and row <= 8:
        if subrow == 0:
            block = field[6][0] + field[7][0] + field[8][0]
        elif subrow == 1:
            block = field[6][1] + field[7][1] + field[8][1]
        elif subrow == 2:
            block = field[6][2] + field[7][2] + field[8][2]
    return block

# place on elemendi index subrow's (väärtuses 0-2)
# column() tagastab field'ist kindla tulba listina, kui on teada subrow ja place
def column(field, subrow, place):
    column = []
    for i in range(9):
        column.append(field[i][subrow][place])
    return column

# is_correct() tagastab True, kui field'is olev nr on reeglipärane
def is_correct(field, row, subrow, place, nr):
    if nr > 0:
        if (field[row][0] + field[row][1] + field[row][2]).count(nr) == 0:
            if column(field, subrow, place).count(nr) == 0:
                if block(field, row, subrow).count(nr) == 0:
                    return True
    return False

# create_field() proovib luua ja tagastada täidetud suduoku-ruudustiku
# kui ta hakkama ei saa, tagastatakse "unsuccessful"
def attempt_to_create_field():
    # esmalt täidetakse kolm diagonaalset block'i suvaliselt (ent reegleid järgides)
    field = [
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],

    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],

    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]
    block1 = random.sample(range(1, 10), 9)
    block2 = random.sample(range(1, 10), 9)
    block3 = random.sample(range(1, 10), 9)
    field[0][0] = block1[:3]
    field[1][0] = block1[3:6]
    field[2][0] = block1[6:]
    field[3][1] = block2[:3]
    field[4][1] = block2[3:6]
    field[5][1] = block2[6:]
    field[6][2] = block3[:3]
    field[7][2] = block3[3:6]
    field[8][2] = block3[6:]
    # ülejäänud block'idesse püütakse reegleid järgides arve sobitada
    for row in range(9):
        for subrow in range(3):
            if field[row][subrow] == [0, 0, 0]:
                for place in range(3):
                    for nr in range(1, 10):
                        if is_correct(field, row, subrow, place, nr):
                            field[row][subrow][place] = nr
                    if field[row][subrow][place] == 0:
                        return "unsuccessful"
    return field
# infinite loop jooksutab create_field()'i nii kaua, kuni tagastatakse field
# peaks aega võtma ca 1 sek
def create_field():
    while True:
        result = attempt_to_create_field()
        if result != "unsuccessful":
            break
    return result

# tagastab ruudustiku, kus on osa ruute tühjaks tehtud 
def create_sudoku(request):
    field = create_field()
    nr_of_empty_slots = 50
    # eemaldame field'ilt subrow'd
    for i in range(9):
        field[i] = field[i][0] + field[i][1] + field[i][2]

    empty_slots = []
    while len(empty_slots) < nr_of_empty_slots:
        row, column = random.randint(0, 8), random.randint(0, 8)
        if (row, column) not in empty_slots:
            empty_slots.append((row, column))

    for row, column in empty_slots:
        field[row][column] = " "

    return render(request, 'sudoku.html', {'field': field })


