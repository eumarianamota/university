from HangManGame import HangManGame

def main():
    nome = HangManGame('Mariana')
    nome.guess_letter('a')
    nome.guess_letter('m')
    nome.guess_letter('n')
    nome.guess_letter('k')
    nome.guess_letter('v')
    nome.guess_letter('c')
    nome.guess_letter('b')
    nome.guess_letter('e')
    nome.guess_letter('i')

    nome.show_status()
    nome.is_finished()

if __name__ == '__main__':
    main()