import os
import sys
import time
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
ascii_art = """
:::    ::: ::::    ::::  :::::::::: :::::::::: :::::::::: 
:+:    :+: +:+:+: :+:+:+ :+:        :+:        :+:        
 +:+  +:+  +:+ +:+:+ +:+ +:+        +:+        +:+        
  +#++:+   +#+  +:+  +#+ +#++:++#   :#::+::#   +#++:++#   
 +#+  +#+  +#+       +#+ +#+        +#+        +#+        
#+#    #+# #+#       #+# #+#        #+#        #+#        
###    ### ###       ### ########## ###        ##########"""
print (ascii_art)
print("                    -Made By HarisXT-")
def animated_loading(stop_condition):
  while not stop_condition():  # Loop until the stop condition is True
      for i in range(4):
          sys.stdout.write('\rLoading' + '.' * i)
          sys.stdout.flush()
          time.sleep(0.5)
  print("\nLoading stopped.")

# Example stop condition
def stop_condition():
  # Add your condition here
  # For example, stop after 10 seconds
  return time.time() > start_time + 10

# Start the loading animation
start_time = time.time()
animated_loading(stop_condition)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

  # Call the function to clear the screen
clear_screen()
ascii_art = """
:::    ::: ::::    ::::  :::::::::: :::::::::: :::::::::: 
:+:    :+: +:+:+: :+:+:+ :+:        :+:        :+:        
 +:+  +:+  +:+ +:+:+ +:+ +:+        +:+        +:+        
  +#++:+   +#+  +:+  +#+ +#++:++#   :#::+::#   +#++:++#   
 +#+  +#+  +#+       +#+ +#+        +#+        +#+        
#+#    #+# #+#       #+# #+#        #+#        #+#        
###    ### ###       ### ########## ###        ##########  """
print (ascii_art)
print("                    -Made By HarisXT-")
def feet_to_meters(feet):
    # 1 foot is approximately equal to 0.3048 meters
    return feet * 0.3048

def meters_to_feet(meters):
    # 1 meter is approximately equal to 3.28084 feet
    return meters * 3.28084

def main():
    try:
        meters = float(input("Enter the length in meters: "))
        feet = meters_to_feet(meters)
        print("{:.2f} meters is equal to {:.2f} feet.".format(meters, feet))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
   main()
time.sleep(5)
def animated_exiting(stop_condition):
  while not stop_condition():  # Loop until the stop condition is True
      for i in range(4):
          sys.stdout.write('\rExiting' + '.' * i)
          sys.stdout.flush()
          time.sleep(0.5)
  print("\nExiting stopped.")

# Example stop condition
def stop_condition():
  # Add your condition here
  # For example, stop after 10 seconds
  return time.time() > start_time + 7

# Start the loading animation
start_time = time.time()
animated_exiting(stop_condition)