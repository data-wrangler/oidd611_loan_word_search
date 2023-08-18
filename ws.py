import re

CODE_FILE = 'one_puzzle.txt'
GRID_SIZE = 10
WORD_LIST = [
    'WHARTON',
    'SCHOOL',
    'BUSINESS',
    'FUTURE',
    'MONEY',
]

def get_coord(grid_string,row,col):
    # get grid elements by (row, col) coordinates
    return grid_string[row*GRID_SIZE+col]

def get_diag(grid_string, nth_diag, direction=1):
    # get a diagonal slice of a grid by enumerated diagonal
    # grids have 2*GRID_SIZE - 1 diagonals

    # check that nth_diagonal is valid
    if nth_diag < 1 or nth_diag >= 2*GRID_SIZE:
        return None
    # check that direction is valid (1=L, -1=R)
    if direction not in [1,-1]:
        raise Exception(f'Unrecognized direction: {direction!s}')

    # nth diagonal can be defined as coordinates where row+col = n
    # back into coordinates with sum=n & both values within grid
    str = ''
    for i in range(nth_diag):
        if i not in range(GRID_SIZE) or nth_diag-i-1 not in range(GRID_SIZE):
            pass
        else:
            if direction == 1:
                str += get_coord(grid_string,i,nth_diag-i-1)
            if direction == -1:
                str += get_coord(grid_string,i,GRID_SIZE-(nth_diag-i))
    return str

def do_word_search(grid_string, word_list):
    # search for words in WORD_LIST and print results

    # check that grid length is appropriate
    if not len(grid_string) == GRID_SIZE**2:
        raise Exception(f'Grid does not contain {GRID_SIZE**2!s} characters')

    # deconstruct grid to horizontal rows & use to print initial grid
    ws_h=[grid_string[i:i+GRID_SIZE] for i in range(0,len(grid_string),GRID_SIZE)]
    print("Grid:")
    for h in ws_h:
        print(' '.join(h))
    # deconstruct grid to vertical columns
    ws_v=[''.join([ws_h[i][j] for i in range(GRID_SIZE)]) for j in range(GRID_SIZE)]
    # deconstruct grid to L and R diagonals
    ws_dl=[get_diag(grid_string,x) for x in range(1,GRID_SIZE*2)]
    ws_dr=[get_diag(grid_string,x,-1) for x in range(1,GRID_SIZE*2)]
    # construct reverse grids to search opposite direction
    ws_hr = [w[::-1] for w in ws_h]
    ws_vr = [w[::-1] for w in ws_v]
    ws_dlr = [w[::-1] for w in ws_dl]
    ws_drr = [w[::-1] for w in ws_dr]
    print(ws_h)
    print(ws_hr)
    print(ws_v)
    print(ws_vr)
    print(ws_dl)
    print(ws_dlr)
    print(ws_dr)
    print(ws_drr)

    # search for each word in word list in each set of directional strings
    # if found, store coordinates of found letters
    matches=[]
    for w in WORD_LIST:
        # horizontal
        for i, s in enumerate(ws_h):
            try:
                start = s.index(w)
                found_coords = [(i,x,) for x in range(start,start+len(w))]
                matches.append(found_coords)
            except ValueError:
                pass
        # horizontal reversed
        for i, s in enumerate(ws_hr):
            try:
                start = s.index(w)
                found_coords = [(i,GRID_SIZE-1-x,) for x in range(start,start+len(w))]
                matches.append(found_coords)
            except ValueError:
                pass
        # vertical
        for i, s in enumerate(ws_v):
            try:
                start = s.index(w)
                found_coords = [(x,i,) for x in range(start,start+len(w))]
                matches.append(found_coords)
            except ValueError:
                pass
        # vertical reversed
        for i, s in enumerate(ws_vr):
            try:
                start = s.index(w)
                found_coords = [(GRID_SIZE-1-x,i,) for x in range(start,start+len(w))]
                matches.append(found_coords)
            except ValueError:
                pass
        # diagonal left
        for i, s in enumerate(ws_dl):
            try:
                start = s.index(w)
                diag_start = (((i+1)%GRID_SIZE)*(i//GRID_SIZE),min(i,GRID_SIZE-1),)
                word_start = (diag_start[0]+start, diag_start[1]-start, )
                found_coords = [(word_start[0]+x,word_start[1]-x,) for x in range(len(w))]
                matches.append(found_coords)
            except ValueError:
                pass
        # diagonal left reversed
        for i, s in enumerate(ws_dlr):
            try:
                start = s.index(w)
                diag_start = (((i+1)%GRID_SIZE)*(i//GRID_SIZE),min(i,GRID_SIZE-1),)
                word_start = (diag_start[0]+start, diag_start[1]-start, )
                found_coords = [(word_start[1]-x,word_start[0]+x,) for x in range(len(w))]
                matches.append(found_coords)
            except ValueError:
                pass
        # diagonal right
        for i, s in enumerate(ws_dr):
            try:
                start = s.index(w)
                diag_start = (((i+1)%GRID_SIZE)*(i//GRID_SIZE),GRID_SIZE-1-min(i,GRID_SIZE-1),)
                word_start = (diag_start[0]+start, diag_start[1]+start, )
                found_coords = [(word_start[0]+x,word_start[1]+x,) for x in range(len(w))]
                matches.append(found_coords)
            except ValueError:
                pass
        # diagonal right reversed
        for i, s in enumerate(ws_drr):
            try:
                start = s.index(w)
                diag_start = (((i+1)%GRID_SIZE)*(i//GRID_SIZE),GRID_SIZE-1-min(i,GRID_SIZE-1),)
                word_start = (diag_start[0]+start, diag_start[1]+start, )
                found_coords = [(GRID_SIZE-1-word_start[1]-x,GRID_SIZE-1-word_start[0]-x,) for x in range(len(w))]
                matches.append(found_coords)
            except ValueError:
                pass
    
    # print results & show found words
    print("Found: {0!s}".format(len(matches)))

    # deduplicate coordinates of found words into single set
    print_points = set()
    for fc in matches:
        print_points.update(set(fc))

    # construct a print grid with word chars included and non-word chars as "•"
    print_grid=''
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j, ) in print_points:
                print_grid+=get_coord(grid_string, i, j)
            else:
                print_grid+="•"
    # print grid with found words
    for ps in [print_grid[i:i+GRID_SIZE] for i in range(0,len(print_grid),GRID_SIZE)]:
        print(' '.join(ps))

# if invoked from command line, search CODE_FILE for WORD_LIST
if __name__ == '__main__':
    with open(CODE_FILE,'r') as f:
        pnum=1
        for l in f.readlines():
            print(f"Solving Wordsearch {pnum!s}")
            l_nospace = re.sub(r'[^\w]','',l)
            do_word_search(l_nospace, WORD_LIST)
            pnum+=1