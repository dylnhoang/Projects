# Nutritional Tracker Program
    #### Video Demo:  https://www.youtube.com/watch?v=uK4fqM7xusM
    #### Description:

    This project aims to aid people interested in personal health to track their caloric input, including fat, carbohydrate, and protein intake. As a person interested in their own personal health and
    keeping healthy, I believe this program will aid heavily in allowing for better health knowledge and personal growth for its users.

    This project uses many different tools to help its functionality. For example, a dictionary was used to hold the caloric input of specific days, allowing for furthered versatility in the project.
    Secondly, I am utilizing the requests module that was outlined in Unit 4 of the CS50P course, allowing me to obtain valuable information from the United States Food Central Database, which has robust information regarding the calories, fats, carbohydrates, and protein of almost every whole food on the market. This is something I would not have been able to do had I not taken this course.
    Furthermore, I am also using regular expressions to check whether a certain date that the user inputs is valid or not. This is also an example of something that I have learned from this course and
    implemented into my own program.
    Finally, I am using a csv file to store and extract information regarding information the user may have already inputted before. The user can import, export, or even clear this file as they see fit.
    I believe this program demonstrates my growth as a Python developer greatly, by implementing many core aspects of the language into one project.

    The project has three main functions: search_food, add_food, and set_date.
    search_food allows the user to search for a certain food's FDC ID by inputting the name of the food. After a food is inputted, its FDC ID is reported back to the user which can then be used to access
    the second function, add_food.
    add_food is used to add a certain food to the nutritional database by inputting an FDC ID and an amount of grams. This will then add [amount of grams] of said food to the day that the user has set the current day to. If no current day is set, the program has error handling to aid in telling the user their mistake. This error handling will also occur if the FDC ID or amount of grams is not numeric.
    set_date is used to set the current date, and uses regex functions to ensure the date is a valid date. It uses MM/DD/YYYY format, which is made known to the user to limit confusion.

    I hope you enjoy this program and its many functions. Thank you for your teachings.
