def text_to_binary(text):
    binary_result = ""
    for char in text:
        binary_result += format(ord(char), '08b') + " "
    return binary_result.strip()

def binary_to_ascii(binary_code):
    ascii_art = ""
    for binary_char in binary_code.split():
        ascii_art += chr(int(binary_char, 2))
    return ascii_art

def main():
    sentence = input("Введіть ваше речення: ")
    binary_code = text_to_binary(sentence)
    print("Бінарний код:", binary_code)

    ascii_art = binary_to_ascii(binary_code)
    print("ASCII-арт:")
    print(ascii_art)

    # Вставити ASCII-арт тут
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


