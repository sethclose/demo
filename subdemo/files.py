# Files 
def files():
    """
    Function to experiment with Files
    """
    filename = "textfile.txt"

    # Open the file to Read print a few lines
    file = open("/home/sethclose/python/"+filename, "r")
    linecount = 0
    for line in file:
        print("   " + line)
        linecount += 1
        if linecount == 13: 
            break
    file.close()

    # Open the file to Write (this erases)
    file = open("./"+filename, "w")
    file.close()

    # Open the file to Append
    file = open("./"+filename, "a")
    file_text = ""
    for x in range(1,4):
        file_text = file_text + str(x) + ")  This got added by files.py, called by demo.py.\r"
    file.write(file_text)
    file.close()    

    
    return
    
