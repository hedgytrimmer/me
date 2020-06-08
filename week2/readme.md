TODO: Reflect on what you learned this week and what is still unclear.
Exercise0
    I've started this early, based on my basic understanding of python.
    ADD 5
        The skeleton of this function is setup, all that requires changing is the "the_answer" line.
        
        Python uses (largely) the same operators as mathematics, addition just uses a "+" sign
        
        "return" outputs the answer
    ADDER
        This is the same as ADD 5, except that 2 arguments are supplied instead of 1

        The arguments are added as before
    SHOUT
        I was not aware of the .upper() function, however I've made use of similar functions before

        Given the argument "a_string", the command is added onto the end of the string, ie "a_string.upper()"
    REALLY SHOUT
        As per the instruction, this command uses the previously defined "shout" function. The really_shout function calls the shout function using the same argument.

        An exclaimation mark is concatinated to the end of the string, ensuring that quotation marks are used to define the exclaimation as a string

        concatinating is merely "adding" two strings together. The + operator is used.
    SHOUT WITH A NUMBER
        This function has two arguments, a string and a number. 

        It is important to cast the number by using "str(a_number)" This turns the number into a string.

        Multiple strings can be concatinated, so I added the space by using " " between the shout function and the str() function.

        This last test took a little longer as I had forgotten some string formatting.

I tried to push ahead, then realised I should probably just wait till next class. I wonder if anyone will read this. Back to Codecademy I go!

EDIT: Some guy pushed ahead so I did too, I realise exercise 1 is not tested and for class. Onto exercise2
Exercise1



Exercise2
    This was a good challenge, a lot of the debugging was changing similar characters, as was alluded to in Week 1
    Examples include: use of different brackets, missing commas in lists
    I was somewhat stumped on the "return alphabet" error, however I just tried removing the index and it worked. This makes sense as the function had already drawn in the index.

Exercise3
    is_odd
        I used a simple if/else statement and the modulo operator to complete this task.
        an even number is divisible by 2, so the modulo must return 0.
        Otherwise, the number is false
    fix_it
        I merely used if statements, however else or elif could be used in combination with this
        "AND" was used to combine the different arms, meaning both values had to be true to pass the test. 
        "or" was used to combined the two no problem results, which completed the challenge of only using 3 return statements.
    loops_1a
        This uses a simple for loop across a range from 0-10 (really 1-10) to add to a star to an empty list
        It returns the list
    loops 1c
        This uses a similar process to the 1a function, however the range is from zero to the input number
    loops_2
        Create 2 empty lists
        In one for loop across range 1-10, append "*" to list1
        In a second for loop across range 1-10, append list2 with list1
    loops_3
        This one stumped me for a bit, I was stuck on how to create multiple lists of 10 numbers.
        I created an empty list and then appended the list with a list of 10 of the temporary variable in a for loop across range(10)
        This worked, however it did not cast it as a string
        I solved this by creating a variable x to cast and then appending the list with 10 versions of x
    loops_4
        This was easier than loops_3.
        2 empty lists were created.
        across range 10, the temporary variable was appended to list1
        then list1 was appended to list2 across range 10
    loops_5
        I was really stuck on this, until I remembered list comprehension is a thing.
        I had worked out how to build the contents of the coordinates, but not how to build the list of lists,similar problem to loops_3
        How I did this function was to create a long list of the contents of the required list.
        Then, I used list comprehension to extract the 5 values of each row
        the list comprehension line puts 5 values of coordinates1 into a list and adds that list to coordinates2, the range outputs values from 0 to the length of coordinates1, in jumps of 5. (ie. 5,10,15..) to create the 10 rows

