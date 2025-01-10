import math
def binary_calculator(bin1, bin2, operator):
  
    #bin1
    pos1 = 0
    pos2 = 0
    pos3 = 0
    pos4 = 0
    pos5 = 0
    pos6 = 0
    pos7 = 0
    pos8 = 0
    sum_of_bin1 = 0

    if bin1[0] == "1":
        pos1 = 128
    if bin1[1] == "1":
        pos2 = 64
    if bin1[2] == "1":
        pos3 = 32
    if bin1[3] == "1":
        pos4 = 16
    if bin1[4] == "1":
        pos5 = 8
    if bin1[5] == "1":
        pos6 = 4
    if bin1[6] == "1":
        pos7 = 2
    if bin1[7] == "1":
        pos8 = 1
  
    sum_of_bin1 = pos1 + pos2 + pos3 + pos4 + pos5 + pos6 + pos7 + pos8

    #bin2
    tpos1 = 0
    tpos2 = 0
    tpos3 = 0
    tpos4 = 0
    tpos5 = 0
    tpos6 = 0
    tpos7 = 0
    tpos8 = 0
    sum_of_bin2 = 0

    if bin2[0] == "1":
        tpos1 = 128
    if bin2[1] == "1":
        tpos2 = 64
    if bin2[2] == "1":
        tpos3 = 32
    if bin2[3] == "1":
        tpos4 = 16
    if bin2[4] == "1":
        tpos5 = 8
    if bin2[5] == "1":
        tpos6 = 4
    if bin2[6] == "1":
        tpos7 = 2
    if bin2[7] == "1":
        tpos8 = 1

    sum_of_bin2 = tpos1 + tpos2 + tpos3 + tpos4 + tpos5 + tpos6 + tpos7 + tpos8


    #print(sum_of_bin1)
    #print(sum_of_bin2)
    #print(operator)
    answer_num = 0
    #if bin1[0][1][2][3][4][5][6][7] in "23456789":
    #for i in range(8):
        #if bin1[i] in "23456789":
            #print("Error")
        #else:
    if any(char in "23456789abcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_+-=`\2|[{]}:;'?/>.<," for char in bin1[:8]):
        print("Error")
    else:
    
        if any(char in "23456789abcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_+-=`\2|[{]}:;'?/>.<," for char in bin2[:8]):
            print("Error")
        else:
            if sum_of_bin2 == 0:
                print("NaN")
            else:
                if operator == "+":
                    answer_num = (sum_of_bin1 + sum_of_bin2)
                if operator == "-":
                    answer_num = (sum_of_bin1 - sum_of_bin2)
                if operator == "*":
                    answer_num = (sum_of_bin1 * sum_of_bin2)
                if operator == "/":
                    answer_num = int(math.floor(sum_of_bin1 / sum_of_bin2))
                #print(answer_num)
                if answer_num < 0:
                    print("Overflow")
                    return()
                if answer_num > 255:
                    print("Overflow")
                    return()
                else:
                    bin_empty = "00000000"
                    bin_list = list(bin_empty)
                    if answer_num >= 128:
                        bin_list[0] = "1"
                        answer_num = answer_num - 128
                    if answer_num >= 64:
                        bin_list[1] = "1"
                        answer_num = answer_num - 64
                    if answer_num >= 32:
                        bin_list[2] = "1"
                        answer_num = answer_num - 32
                    if answer_num >= 16:
                        bin_list[3] = "1"
                        answer_num = answer_num - 16
                    if answer_num >= 8:
                        bin_list[4] = "1"
                        answer_num = answer_num - 8
                    if answer_num >= 4:
                        bin_list[5] = "1"
                        answer_num = answer_num - 4
                    if answer_num >= 2:
                        bin_list[6] = "1"
                        answer_num = answer_num - 2
                    if answer_num >= 1:
                        bin_list[7] = "1"
                        answer_num = answer_num - 1

                    bin_list = ''.join(bin_list)                                        
                    print(bin_list)
                    return()
                #print(answer_num)
                                


binary_calculator("00000001", "00000001", "+")
