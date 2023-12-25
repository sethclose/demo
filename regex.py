# Regular Expressions
import re
def regexes():
    """
    Function for experimenting with regular expressions (regex's)
    """
    
    txt = "The rain in Spain"
    
    if "re.Match" in str(re.search("^The.*Spain$", txt)): 
        print(f"Found '^The.*Spain$' in '{txt}'")
        print("Starts with 'The', then some characters, Ending with 'Spain'")

    search = "ai"
    found = re.findall(search, txt)
    if len(search) > 0:
        print(f"Found '{search}' in '{txt}':  {found}")
    
    return
"""
RegEx Functions
    findall	Returns a list containing all matches
    search	Returns a Match object if there is a match anywhere in the string
    split	Returns a list where the string has been split at each match
    sub	    Replaces one or many matches with a string

Metacharacters
    Character	Description	                                                                Example	
    []	        A set of characters	                                                        "[a-m]"	
    \	        Signals a special sequence (can also be used to escape special characters)	"\d"	
    .	        Any character (except newline character)	                                "he..o"	
    ^	        Starts with	                                                                "^hello"	
    $	        Ends with	                                                                "planet$"	
    *	        Zero or more occurrences	                                                "he.*o"	
    +	        One or more occurrences	                                                    "he.+o"	
    ?	        Zero or one occurrences	                                                    "he.?o"	
    {}	        Exactly the specified number of occurrences	                                "he.{2}o"	
    |	        Either or	                                                                "falls|stays"	
    ()	        Capture and group

Special Sequences
    A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
    Character	Description	Example	
    \A	Returns a match if the specified characters are at the beginning of the string	            "\AThe"	
    \b	Returns a match where the specified characters are at the beginning or at the end of a word r"\bain"
     (the "r" in the beginning is making sure that the string is being treated as a "raw string")   r"ain\b"
    \B	Returns a match where the specified characters are present, but NOT beg or ed of a word     r"\bain"
     (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
    \d	Returns a match where the string contains digits (numbers from 0-9)	                        "\d"	
    \D	Returns a match where the string DOES NOT contain digits	                                "\D"	
    \s	Returns a match where the string contains a white space character	                        "\s"	
    \S	Returns a match where the string DOES NOT contain a white space character	                "\S"	
    \w	Returns a match where the string contains any word characters                               "\w"	
    \W	Returns a match where the string DOES NOT contain any word characters	                    "\W"	
    \Z	Returns a match if the specified characters are at the end of the string	                "Spain\Z"

Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:
    Set	Description	Try it
    [arn]	Returns a match where one of the specified characters (a, r, or n) is present	
    [a-n]	Returns a match for any lower case character, alphabetically between a and n	
    [^arn]	Returns a match for any character EXCEPT a, r, and n	
    [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
    [0-9]	Returns a match for any digit between 0 and 9	
    [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
    [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
    [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any
"""    