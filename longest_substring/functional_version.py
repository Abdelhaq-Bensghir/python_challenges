# def find_longest_string(input_string):
#     """
#     Detect the longest substring with distinct characters in the given string.
#     """
#     c=0 #length of l
#     l=[]
#     for i in input_string:
#         if i in l[c]: l.append(i)
#         else: l[c].append(i)
#         c+=1
    
#     lenghts= [len(i) for i in l]

#     result = [j for (j,k) in (l,lenghts) if k = max(lenghts)]

# if __name__ == '__main__':
#     input_string = 'abdb' #input('enter a string')
#     longest_string(input_string)