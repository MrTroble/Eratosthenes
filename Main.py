s = int(input());
list_of_numbers = [];
list_of_vals = [];
for x in range(2, s):
    list_of_numbers.append(x);
list_of_vals = list(list_of_numbers);
for z in range(0, len(list_of_vals)):
    if z + 1 >= len(list_of_numbers):
        break;
    for h in range(z + 1, len(list_of_numbers)):
        if list_of_numbers[h] == None:
            continue;
        if list_of_numbers[h] % list_of_vals[z] == 0:
            list_of_numbers[h] = None;
for g in range(0, len(list_of_numbers)):
    c = list_of_numbers[g];
    if c != None:
        print(c);
            
            
        
