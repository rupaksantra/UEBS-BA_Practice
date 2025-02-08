my_string = 'Today we are learning about conditionals, loops and functions'
my_list = ['conditionals', 'loops', 'functions']
target = 'loops'
target2 = 'variables'


my_coordinates=[]

for i in my_list:
    start_pos = my_string.find(i)
    string_length = len(i)
    end_pos = start_pos+string_length 
    my_coordinates.append((start_pos,end_pos))

print (my_coordinates)