katz_deli = []

def line(katz_deli):
    message = 'The line is currently:'  
    if len(katz_deli) == 0:
     print('The line is currently empty.')
    else:
        for name in katz_deli:
            num = katz_deli.index(name) + 1
            message2 = f' {num}. {name}' 
            message += message2 

        print(message)
 

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = katz_deli.index(name) + 1
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
   if len(katz_deli) > 0:
      print(f"Currently serving {katz_deli.pop(0)}.")
   else:
      print("There is nobody waiting to be served!")
 
      
   