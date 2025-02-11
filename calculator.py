import math #imports math module to give us some needed function

def binary_calculator(bin1, bin2, operator): #defines our function and accecpts the three inputs
  

    if len(bin1) < 8: #initially checks if bin1 is less than 8 characters
        return("Error") #if it is less than 8 characters, it returns "Error" because it should be 8 if its a binary
    if len(bin2) < 8: #initially checks if bin2 is less than 8 characters
        return("Error") #if it is less than 8 characters, it returns "Error" because it should be 8 if its a binary
    if any(char in "23456789abcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_+-=`\2|[{]}:;'?/>.<," for char in bin1[:8]): #checks if any characters in bin1 are anything other than a 1 or 0
        return("Error") #returns Error if there is something in the binary that isnt a 1 or 0
    else:
    
        if any(char in "23456789abcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_+-=`\2|[{]}:;'?/>.<," for char in bin2[:8]): #checks if any characters in bin2 are anything other than a 1 or 0
            return("Error") #returns Error if there is something in the binary that isnt a 1 or 0
        else:

    #bin1
            pos1 = 0 #sets up a zero value for the number 1 position in bin 1
            pos2 = 0 #sets up a zero value for the number 2 position in bin 1
            pos3 = 0 #sets up a zero value for the number 3 position in bin 1
            pos4 = 0 #sets up a zero value for the number 4 position in bin 1
            pos5 = 0 #sets up a zero value for the number 5 position in bin 1
            pos6 = 0 #sets up a zero value for the number 6 position in bin 1
            pos7 = 0 #sets up a zero value for the number 7 position in bin 1
            pos8 = 0 #sets up a zero value for the number 8 position in bin 1
            sum_of_bin1 = 0 #sets the sum of bin 1 to zero to start out

            if bin1[0] == "1": #checks if the number 1 character in bin1 is a "1"
                pos1 = 128 #sets number 1 position value in bin 1 equal to 128

            if bin1[1] == "1": #checks if the number 2 character in bin1 is a "1"
                pos2 = 64 #sets number 2 position value in bin 1 equal to 64

            if bin1[2] == "1": #checks if the number 3 character in bin1 is a "1"
                pos3 = 32 #sets number 3 position value in bin 1 equal to 32

            if bin1[3] == "1": #checks if the number 4 character in bin1 is a "1"
                pos4 = 16 #sets number 4 position value in bin 1 equal to 16

            if bin1[4] == "1": #checks if the number 5 character in bin1 is a "1"
                pos5 = 8 #sets number 5 position value in bin 1 equal to 8

            if bin1[5] == "1": #checks if the number 6 character in bin1 is a "1"
                pos6 = 4 #sets number 6 position value in bin 1 equal to 4

            if bin1[6] == "1": #checks if the number 7 character in bin1 is a "1"
                pos7 = 2 #sets number 7 position value in bin 1 equal to 2

            if bin1[7] == "1": #checks if the number 8 character in bin1 is a "1"
                pos8 = 1 #sets number 8 position value in bin 1 equal to 1
        
            sum_of_bin1 = pos1 + pos2 + pos3 + pos4 + pos5 + pos6 + pos7 + pos8 #adds all the values of all positions in bin 1 to get a sum

            #bin2
            tpos1 = 0 #sets up a zero value for the number 1 position in bin 2
            tpos2 = 0 #sets up a zero value for the number 2 position in bin 2
            tpos3 = 0 #sets up a zero value for the number 3 position in bin 2
            tpos4 = 0 #sets up a zero value for the number 4 position in bin 2
            tpos5 = 0 #sets up a zero value for the number 5 position in bin 2
            tpos6 = 0 #sets up a zero value for the number 6 position in bin 2
            tpos7 = 0 #sets up a zero value for the number 7 position in bin 2
            tpos8 = 0 #sets up a zero value for the number 8 position in bin 2
            sum_of_bin2 = 0 #sets the sum of bin 2 to zero to start out

            if bin2[0] == "1": #checks if the number 1 character in bin2 is a "1"
                tpos1 = 128  #sets number 1 position value in bin2 equal to 128

            if bin2[1] == "1": #checks if the number 2 character in bin2 is a "1"
                tpos2 = 64  #sets number 2 position value in bin2 equal to 64

            if bin2[2] == "1": #checks if the number 3 character in bin2 is a "1"
                tpos3 = 32  #sets number 3 position value in bin2 equal to 32

            if bin2[3] == "1": #checks if the number 4 character in bin2 is a "1"
                tpos4 = 16  #sets number 4 position value in bin2 equal to 16

            if bin2[4] == "1": #checks if the number 5 character in bin2 is a "1"
                tpos5 = 8  #sets number 5 position value in bin2 equal to 8

            if bin2[5] == "1": #checks if the number 6 character in bin2 is a "1"
                tpos6 = 4  #sets number 6 position value in bin2 equal to 4

            if bin2[6] == "1": #checks if the number 7 character in bin2 is a "1"
                tpos7 = 2  #sets number 7 position value in bin2 equal to 2

            if bin2[7] == "1": #checks if the number 8 character in bin2 is a "1"
                tpos8 = 1  #sets number 8 position value in bin2 equal to 1

            sum_of_bin2 = tpos1 + tpos2 + tpos3 + tpos4 + tpos5 + tpos6 + tpos7 + tpos8 #adds all the values of all positions in bin 2 to get a sum


            answer_num = 0 #sets a value equal to 0

            if sum_of_bin2 == 0: #checks if the sum of bin2 is equal to 0
                        return("NaN") #if true, returns NaN or not a number because we dont want to divid by 0
            else:
                        if operator == "+": #checks if the operator is a +
                            answer_num = (sum_of_bin1 + sum_of_bin2) #if true, it adds the two bin sums together and sets that value equal to our answer_num variable

                        if operator == "-": #checks if the operator is a -
                            answer_num = (sum_of_bin1 - sum_of_bin2) #if true, it subtracts the two bin sums together and sets that value equal to our answer_num variable

                        if operator == "*": #checks if the operator is a *
                            answer_num = (sum_of_bin1 * sum_of_bin2) #if true, it multiplies the two bin sums together and sets that value equal to our answer_num variable

                        if operator == "/": #checks if the operator is a /
                            answer_num = int(math.floor(sum_of_bin1 / sum_of_bin2)) #if true, it divides the two bin sums together, then it floors the answer to the nearest whole number, then it sets that value equal to our answer_num variable

                        if answer_num < 0: #checks if our answer is less than 0
                            return("Overflow") #if true, we return "Overflow"
                        
                        if answer_num > 255: #checks if our answer is more than 255
                            return("Overflow") #if true, we return "Overflow"
                        else:

                            bin_empty = "00000000" #creates a string of 8 zeros
                            bin_list = list(bin_empty) #makes the string a list
                            if answer_num >= 128: #checks if the answer number is  greater than 128
                                bin_list[0] = "1" #if true, it changes the corrasponding position equal to 1
                                answer_num = answer_num - 128 #if true it subtracts 128 from our answer number

                            if answer_num >= 64: #checks if the answer number is  greater than 64
                                bin_list[1] = "1" #if true, it changes the corrasponding position equal to 1
                                answer_num = answer_num - 64 #if true it subtracts 64 from our answer number

                            if answer_num >= 32: #checks if the answer number is  greater than 32
                                bin_list[2] = "1" #if true, it changes the corrasponding position equal to 1
                                answer_num = answer_num - 32 #if true it subtracts 32 from our answer number

                            if answer_num >= 16: #checks if the answer number is  greater than 16
                                bin_list[3] = "1" #if true, it changes the corrasponding position equal to 1
                                answer_num = answer_num - 16 #if true it subtracts 16 from our answer number

                            if answer_num >= 8: #checks if the answer number is  greater than 8
                                bin_list[4] = "1" #if true, it changes the corrasponding position equal to 1
                                answer_num = answer_num - 8 #if true it subtracts 8 from our answer number
                                
                            if answer_num >= 4: #checks if the answer number is  greater than 4
                                bin_list[5] = "1" #if true, it changes the corrasponding position equal to 1
                                answer_num = answer_num - 4 #if true it subtracts 4 from our answer number

                            if answer_num >= 2: #checks if the answer number is  greater than 2
                                bin_list[6] = "1" #if true, it changes the corrasponding position equal to 1
                                answer_num = answer_num - 2 #if true it subtracts 2 from our answer number

                            if answer_num >= 1: #checks if the answer number is  greater than 1
                                bin_list[7] = "1" #if true, it changes the corrasponding position equal to 1
                                answer_num = answer_num - 1 #if true it subtracts 1 from our answer number

                            bin_list = ''.join(bin_list) #joins the list together                                       
                            
                            return(bin_list) #returns the correct string
                            


binary_calculator("00000001", "00000001", "+") #calls our function and gives it the manual inputs.
