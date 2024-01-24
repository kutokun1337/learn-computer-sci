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
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BP#@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@&GPB@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BPB@@@@@@@@&#@@@@@#PG&@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BGPG&@@@@@@@@@@GG@@@@&GB@@@@@@@@@@@@##@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BPPP#@@@@@@@@@@@@GP&@@@@@&@@@@@@@@@@@@#P&@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PPPB@@@#&@@@@@@@&PG@@@@@@@@@@@@@@@@@@@&G@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PPPG#&&GG@@@@##@@B&@@@@@&@@@@@@@@@@@@@@&@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@&@@@@@GPPPPPPPP&@@&PB@@@@@&@@@&@@@@@@@@@&#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@B#@@@@@@@@&P&@@@@#PPPPPPPGBB#GPP&@@@&G&@@B&@&#@@@@@&G&@@@@@@@@@@@@@@
@@@@@@@@@@&&@@@@@@@@@@@@@@@@@GB@@@@@@@@@@@@BG&@@@@GPPPPPPG#PG#GP#@@@#PG&@##@@GG&@@@@BP&@@@@@@@@@@@@@
@@@@@@@@@@&G#@@@@@@@@@@@@@@@@BPB&@@@@@@&&@@@#PB##BPPPPPPPPPB##BB@@@@BPPP#@@@&GPG&@@@@BP#@@@@@@@@@@@@
@@@@@@@@@@@BG@@@@@@@@@@@@@@@@@BPPG#&@@@@&###GPPPPPPPPPPPPPP#GP&@@@@&GPPPP#@@GPPP&@@@@@#PB@@@@@@@@@@@
@@@@@@@@@@@#PB@@@@@@@@@@@@@@@@@&BGPPB&@@@#PPPPPPPPPPPPPPPPPGGPG#&#BPPPPPG&@@GPG&@#@@@@@#P#@@@@@@@@@@
@@@@@@@@@@@@#GB&@@@@@@@@@##&@@@@@@&BPP&&@&PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG&@@BB@@@BB@@@@@G#@@@@@@@@@@
@@@@@@@@@@@@@@&#&@@@@@@@@@###&@@&&@@PP##&@GPPPPPPPPPPGPPPPPB&BPPPPPP##GPPG&@GB@@@&PB&@@@#@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#&&@@@@@@@@@@@&&PPGPB#PPPPPPPPPPG&BPG##BG&PPPPPG@@&GPPP#BP&&G&BPP&@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&BGGB#@@@@@@@&B@BPPPPPPPPPPPPPGBBGB#&GPPP#GPPPPB#GGGPPPG#PG&#GPPP&@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&@@#@@@&GPG&@@#&@#PB&BPPPGBPPGGPPBBGPPG&GPPPG&PGGPPPPPPPPPPPB#PB@&PPB@@@@@@@@@@@@@@@
@@@@@@@@@&B@@@@@@###BB#&@BPP&@@#B#GPGB#GPG&&#B&#GGPPPPPPPPPPB#B#GPPPPPPPPGGGPBBG@&PB@@&@@@@@@@@@@@@@
@@@@@@@@@@BG#&@@@@#GGPPGB&#GG&@@#BBPPPPBGPPG#&&GGPPPPPPPPPPG&&BPPPPPPPPB&@@@&BBB&#G@#P#@@@@@@@@@@@@@
@@@@@@@@@@@&#BB@@@@#GGPG&#&#B##GPGBBPPGPGPPPPPBGPPPPPPGPPPPB@BPPPPPPPG&@@@@@@@GG##G&PP&@@@@@@@@@@@@@
@@@@@@@@@@@@@@&@@@&@@@&@&PPGPGBPPPPBBP##G#PPPPPPPPBGP#BPPPPG&BPPPPPPB&@@@@@@@@BPB#P&GP#@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&B#@@&GGB#&##BB###&GG&#BPPPPPPPP#GG&PPPPPPPPPPPPP#@@@@@@@@@@#PP#GG#PG@@@@@@@@@@@@@
@@@@@@@@@@&@@@@@@@@&P##@&@&##&GGB&&#&@&&@BPPBGPGGP&BP&GPPPPPPPPPPB#GB@@@@@@@@@#PP#GPG#G&@@@@@@@@@@@@
@@@@@@@@@@&&@@@&#@@&PBG&@&#BGB###&##&#@@@&##&GG&#PG&##&##BPGGGB#B##B#@@@@@@@@#PG#BPPG#G&@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#B#GGGGG&@@#BB&##&##&B#@&#@@B##GPPPPGB#&@@&@@@@@@@@@@@@@@@@#GG##GPPP#B&@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&GGPPPPG@@@@&#&BBB##BG&&G#@#&#GGGPPPGGGB##&&&&@@@@@@&&##BGGB#GGBGP#@BGB&@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@#GPPPPB@&G###@&BBB##&@&&&@@@@@&&BGPGBBBGGBBBBBBBBBBBBBBBBGGB##BG#BB@&PG&@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@&BGPP#@#BGBBBBBBBBGGGPPB@&B@@&@&&GPPGB&#GGGBBGGGGGGGGGBB#&#GPG#@&GG@&PG@@@@@@@@@@
@@@@@@@@@@@@@@@@@&##@@&#B&#BBG###BBGGB##&&&@&GB@@@B&BPPPPPB##GGGB#&&&&@@&&#BGGB#GP#@&PB@GP&@@@@@@@@@
@@@@@@@@@@@@@@@@@@@&&@@@@##B&@&&&&&&@@@@@@GGB&GGB&@@GPPPPPPPGB#BGPGGGGGGPPGBBG&@GPP#@GP@GG@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@#G&@@&#@@@@@@@@####BPPP&GPP&@#G#BPPGB&@GG@@&#GPPPPPGBPPPP#@BBB#BBBG&@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&#@@@@@@@@@@&BPPPPPG&##PPP#@&@BPPP#@@&GB@&#####GPG@#GPPPPB@@&BBB#@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PBBBBBB&GPPPPB@@&BGGG#@@#&&BPPGGGB&B#@@@#GGBBB#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#&@@@@&BPPPG#&BBBBBBB#@@&&&@@@&BPGBBGGBBG&&@@@@@@#GPPGGB@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#&@@@#GPPPPPP#GG&G&BB##@#PPGGPPG#&GPPPP##G&@@@@@@@@#BBB&@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGPPPPPPPB@@@@@@&&@@@@#BBBB&@@@BPPPPPBB#@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGPPPPPPPPGB&&#@@@@@@@@@@@@@@@@@@@@@BPPPPPG#@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#BGPPPPGGGBB#&@@@BPGB&@@@@@@@@@@@@@@@&G&@#GPPPPPG#&@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@BGGB@@@@&GPPG##BBGGGGB#&&&@#GP&@@@#BGPPPPPGB#&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&GPPG#&&&#BBGPPPGGGGGPPPB##GP#@@&#GG#&#BGGGGB#@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#GPPPPPPPPGGBB&&@@&&GPPPGBB#BGPPB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&##BGGBBGBBBGPGGG##BGGPPPPPG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GGBGGPPPPPPPGBBGGB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#GGPPPPPPPPP##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#B#BBB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    """
    print(custom_art)

if __name__ == "__main__":
    main()
