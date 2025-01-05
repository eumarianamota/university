# Implemente um jogo de cartas com as seguintes classes:
# 1. Classe Card :
# Atributos: suit ( spades , clubs , hearts , diamonds ) e value (1 a 13, onde 1 é ace , 11 é jack , 12 é queen , 13 é king ).
# Método:
# __str__ : Retorna uma string representando a carta. Exemplos: "10C" (ten of clubs), "AH" (ace of diamonds) ou "JD" (jack of diamonds).
# 2. Classe Deck :
# Atributos: cards (lista de objetos Card ).
# Métodos:
# generate_deck() : Cria um baralho completo com 52 cartas.
# shuffle() : Embaralha as cartas. Caso o baralho esteja vazio, lance uma exceção EmptyDeckError .
# deal_card() : Remove a carta do topo do baralho e a retorna. Caso o baralho esteja vazio, lance uma exceção EmptyDeckError .
# remaining_cards() : Mostra quantas cartas ainda estão no baralho.
