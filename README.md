# Input-Reverse-Capital-Shift-Treads.

# EXPLANATION OF THE CODE:

An InputThread, a ReverseThread, a CapitalThread, and a ShiftThread are the four threads that are created by this code and we created four classes each of these provides different functionality like in Inputtingthread class what we are doing is we defined a function in it where we are taking input from the user and there is try-except block where we can handle the exceptions if the error occurs while providing the input. 
Then there is ReversedThread class in which reversed string from the input string is kept in the result attribute of the input thread. The result attribute of the InputThread is transformed by the ReverseThread and we get reversed string.
Then there is CapitalizedThread class which is also dependent on the InputThread, in this class we have defined a function in which we are using (.upper) built in function in python that capitalizes the whole string that is provided.
And in the last we have ShiftThread class which is also dependent on InputThread, in this class we have functionality that is used to shift the letters in the string
Before beginning its own work, each thread invokes the InputThread's join() method, which forces the thread to wait until the InputThread has finished. By doing this, it is ensured that the other threads won't begin operating until the InputThread has completed.

# OUTPUT OF THE CODE:

![image](https://user-images.githubusercontent.com/92660593/210552068-2005ac0f-91e3-4ed9-808f-1429983c216b.png)
![image](https://user-images.githubusercontent.com/92660593/210552084-f3f4bfba-0b2b-4dfc-8335-493258e1e217.png)
![image](https://user-images.githubusercontent.com/92660593/210552101-92aac5cf-d16b-44e5-b8ba-995326570149.png)
