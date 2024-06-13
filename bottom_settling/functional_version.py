# Move all the periods ('.') in a given array to the end of the array.
# For example: 'a,b,.,c,.,.,k' becomes 'a,b,c,k,.,.,.'
# and ['a','.', 'b', 'c', '.', '.', 'k'] becomes ['a', 'b', 'c', 'k', '.', '.', '.']

def move_periods_to_end(l):
    periods = [i for i in l if i == '.']
    non_periods = [i for i in l if i != '.']
    result = non_periods + periods
    # print(result)
    if type(l)==str: return ''.join(result)
    else: return result


if __name__ == '__main__':
    s = 'a,b,.,c,.,.,k'
    print(type(move_periods_to_end(s)),':',move_periods_to_end(s))
    print('---')
    li = ['a','.', 'b', 'c', '.', '.', 'k']
    print(type(move_periods_to_end(li)),':',move_periods_to_end(li))