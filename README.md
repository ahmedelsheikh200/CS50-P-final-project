    #find_your_online_chess_coach
    #### Video Demo:  <https://youtu.be/dskyE6TOr_A>
    #### Description:
    TODO
    this a code help trainess to find some chess coaches who also use the same program
    this idea i hope one day to become a real mobile app and web app , the steps here that the user pens the program ,
    asked if he is a trainee or a chess coach , depending on this he asked to enter some data that helps us .
    the first thing we do in our program that we imported csv library which we use to save student data and coaches data
    we show some data from coaches csv  to students to choose one from them
    we defined class person which is the parent class to another two classes ( user , coach )
    the person class hase a ttributes first name,last name,country,age  and rating and the two classes mentioned above
    interhirance all these attributes from it . the first and last name should be null , if it was we raise value error, also age couldn't be
    zero or less , rating couldn't be negative  value , we used pycountry library to make sure that the country which user enter is a real one
    i could use list contain names of all cuntries but that is much better.
    the second class we defined is user which is for student have the same attributes from  the parent class , it has its own functions
    1 __init__ to inialize the attributes 2=__str__ to convert the values to a string to treat with it
    3- get_user func which gets all the information from the user and returns it as a user (object in the class)
     the third class we defined is Coach which is for coaches have the same attributes from  the parent class plus experience years which ask about the number of years he worked as a coach which also can not be a negative number   , it has its own functions:
    1 __init__ to inialize the attributes 2=__str__ to convert the values to a string to treat with it
    3- get_coach func which gets all the information from the coach that help students to choose his perfect coach and returns it as a coach  (object in the class)
    after that we made our main function which use another funcs , first we use know_the_user func
    it is a while true loop , asks the user "If you are a coach type 'c', if you are a trainee type 't': ").we
    use here two methods strip() and lower() so if "C" or "T" is accepted if any thing other it repets the question, the answer is returned as
    a variable in main func , depend on the answer  happens the next , if uou are a coach we import Coach.get_coach to get the data from you
    after that comes the role of our next func save_coaches_data which save all the data in csv file to have all coaches data and use it
    the field names in the csv file First Name,Last Name,Country,Age,Rating,experience Years
    and here your role as a coach finished and after that you can receive requests from students
    on the other hand if you are a trainee comes the role of our next func save_user _data which save all the data in csv file to have all students  data and use it
    the field names in the csv file First Name,Last Name,Country,Age,Rating comes the next func choose_coach which read coaches csv and ask you to choose one



