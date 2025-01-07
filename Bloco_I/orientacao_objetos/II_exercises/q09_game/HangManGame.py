# 1. Classe HangmanGame :
# Atributos: secret_word (string), discovered_letters (lista de letras certas), remaining_attempts (int).
# Métodos:
# guess_letter(letter) : Verifica se a letra está na palavra e atualiza discovered_letters ou decrementa remaining_attempts. Caso a letra já tenha sido usada, lance uma exceção LetterAlreadyGuessedError .
# show_status() : Mostra o progresso (letras descobertas e tentativas restantes).
# is_finished() : Verifica se o jogador ganhou ou perdeu.
class LetterAlreadyGuessedError(Exception):
    pass

class HangManGame:
    def __init__(self, secret_word):
        self.secret_word = list(secret_word.upper())
        self.discovered_letters = list('_'*len(self.secret_word))
        self.remaining_attempts = 5
    
    def guess_letter(self, letter):
        letter = letter.upper()
        if letter in self.discovered_letters:
            raise LetterAlreadyGuessedError('Essa letra já foi adivinhada')
        elif letter in self.secret_word:
            numb = self.secret_word.count(letter)
            for _ in range(numb):
                index = self.secret_word.index(letter)
                self.secret_word.pop(index)
                self.secret_word.insert(index, ' ')
                self.discovered_letters.pop(index)
                self.discovered_letters.insert(index, letter)
        elif letter not in self.secret_word:
            self.remaining_attempts -= 1

    def show_status(self):
        print('Discovered letters:', end=' ')
        for i in self.discovered_letters:
            print(i, end=' ')
        print(' ')
        print(f'Remaing attepmts: {self.remaining_attempts}')
    
    def is_finished(self):
        discovered_letters = "".join(self.discovered_letters) 
        if discovered_letters.find('_') == -1:
            print('YOU WON THE GAME')
        elif self.remaining_attempts == 0:
            print('YOU LOST THE GAME')
        else:
            print('THE GAME IS ONGOING')