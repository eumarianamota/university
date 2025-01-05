# 1. Classe HangmanGame :
# Atributos: secret_word (string), discovered_letters (lista de letras certas), remaining_attempts (int).
# Métodos:
# guess_letter(letter) : Verifica se a letra está na palavra e atualiza discovered_letters ou decrementa remaining_attempts . Caso a
# letra já tenha sido usada, lance uma exceção LetterAlreadyGuessedError .
# show_status() : Mostra o progresso (letras descobertas e tentativas restantes).
# is_finished() : Verifica se o jogador ganhou ou perdeu.
