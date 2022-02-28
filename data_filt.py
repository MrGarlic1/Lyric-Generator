from termcolor import colored


def main():
    file = open('Lyrics.txt', 'r')

    msg_txt = file.read()

    msg_txt = msg_txt.split('\n')

    i = 0
    while i < len(msg_txt):
        if msg_txt[i].startswith('[') or msg_txt[i] == '':
            del msg_txt[i]
            i -= 1
        i += 1

    for i, txt in enumerate(msg_txt):
        if txt.startswith('source: '):
            msg_txt[i] = 'END\n'

    out = open('Filtered_Lyrics.txt', 'w')

    for i in range(len(msg_txt)):
        out.write(msg_txt[i] + '\n')
        print(f'Appended "{msg_txt[i]}" to file.')

    print(colored(f'\nAdded {len(msg_txt)} entries to file.', 'cyan'))


if __name__ == '__main__':
    main()
