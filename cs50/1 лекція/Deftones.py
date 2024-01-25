def text_to_binary(text):
    binary_result = ""# add emptyline after
    for char in text:
        binary_result += format(ord(char), '08b') + " " #todo let move '08b' to params
    return binary_result.strip() #todo add emptyline before

def binary_to_ascii(binary_code):
    #todo do we ca use map and lambda for optimizate code
    ascii_art = "" #todo add emty line
    for binary_char in binary_code.split(): #todo do not use split method in loop
        ascii_art += chr(int(binary_char, 2))
    return ascii_art #todo add empty line befor return

def main():
    sentence = input("Введіть ваше речення: ")
    binary_code = text_to_binary(sentence)
    print("Бінарний код:", binary_code)

    ascii_art = binary_to_ascii(binary_code)
    print("ASCII-арт:")
    print(ascii_art)

    #todo make saperate method for output, here we should init data
    # Вставити ASCII-арт тут
    #todo WTF, why do we need it here remove
    custom_art = """
                                      ^7?^                                                    
                                         .?B@5P@!                                                   
                    ^!J5~               ^B@@7 !@J                                                   
                   ^&@@#.              ~&@@7  Y@!                                                   
                   G@@@~              ~&@@J  ^@#.                                                   
                  7@@@5              :#@@P  :B@!                                                    
                 .#@@#:              P@@#: :B@? .:.                                                 
                 Y@@@7              ?@@@! ^#@J5B&B.                                                 
                ^@@@P              :&@@5 ~&&~J@@@7                                                  
                G@@&:              5@@#.?@G:~@@@5                                                   
               ?@@@7              ~@@@J5@J:^#@@&^..                                            ..   
              ^&@@P               G@@@&G^:P&@@@G5P?    ..                          .::.      ^G&@J  
      .^?5PPPP#@@&:  .~JPGPP57.  7@@@#7   7@@@P    ^?PGPPBP7.  !5PG?.75BBBJ.   :7PBBPG#P^   :P@@Y:  
    :J#@#J~:.P@@@7 .J#@#?^.J@@J .#@@5.  ^J&@@#:  !G@@P^..B@@G.:&@@@5G57#@@@^ :Y&@#!. ?@@G ^5GP@@B^  
   !&@@P.   7@@@G ^#@@P. ^J&@P:^G@@B^!JPG@@@@!  Y@@@5   .#@@@^5@@@@P^ ~@@@G ~#@@P..!5@&P?5G7. #@@B  
  ^@@@#.  .J@@@@^ B@@@5YPGPJ7?G@@@@#G57:7@@@5  ~@@@#.   Y@@@J^@@@@Y   B@@&^ B@@@PPPPJ7?5GJ    B@@#. 
  !@@@&!!YBP@@@P^Y@@@&J77?J55??@@@P:    B@@@?JGGP@@&^.^P@&P~ P@@@J   ~@@@P!P#@@@57!7YPYJ&@B!^7@@#!  
   JB&&#GJ: YB#GPJ~?GBBGPY!:  P@@&:     !PGG5?^  !5BGPG57:  :PPPJ    :5BBPJ~.!5GBGPY!. .?5GGP5J!.   
     ::.      .       .      !@@@7                                                                  
                            :#@@5                                                                   
                            G@@#.                                                                   
                           5@@@!                                                                    
                          ?&BP7                                                                     
                          ^:  
    """
    print(custom_art)

if __name__ == "__main__":
    main()


#todo add function for convert from binary code to text

#todo add function for generate console art
# [[0,0,0,1,1][0,0,1,1,0],[0,1,1,0,0]] there is initial param
# use only eng
