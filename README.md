# LOZ11
Interacting with Items

There is a bug fix in game1.8.1.py.  I would suggest using that file for the bug fix.  Then watch the video programming with your pygame_functions file from last time.  If you get stuck, 1.9 is the complete code from the video.

Video - YouTube - https://youtu.be/NBmzs2c9e-I  
Video - EdPuzzle - https://edpuzzle.com/media/5f204ce0a06b593f23dbf56e  

Extensions:  
1. Use the three sound files to make appropriate sounds when link collects items:  
 - In the collect method if item is a heart object, play sound Get_Heart  
 - else if item is a rupee or blue rupee object, play sound Get_Rupee  
 - else play sound Get_Item  
 
Challenges:
1. In the collect method, the health should only increment if we haven't gone past our maxHealth parameter.  
2. Make the other items work in the game:  
 - The Fairy should increase Link's health back up to maxHealth
 - The Bomb should increment the bomb parameter that you will have to add to the player class list of parameters
 - The Timer should pause all enemies on the screen for about 5 second (5000 milliseconds)  ***This is tough***  Consider adding a timer parameter to the Player Class.  In the while loop check if that parameter is True, if it is, store the speed of each enemy in a parallel list, set each enemy's speed to 0 for several loops.  When that is done, make the timer parameter False and return the enemies back to their original speeds.  One trick is that if an enemy is killed during that time, then the corresponding item in the speeds list should also be removed.
