# Classe Product :
# Atributos: name , price , stock_quantity .
# 2. Classe ShoppingCart :
# Atributos: Lista de produtos no carrinho.
# Métodos:
# add_product(product, quantity) : Adiciona produtos ao carrinho, verificando o estoque. Caso não haja estoque suficiente, lance uma
# exceção InsufficientStockError .
# remove_product(product_name) : Remove produtos do carrinho. Caso o produto não esteja no carrinho, lance uma exceção
# ProductNotInCartError .
# calculate_total() : Retorna o valor total do carrinho.
# 3. Classe Sale :
# Atributos: Informações do cliente e carrinho.
# Métodos:
# finalize_sale() : Exibe o resumo da venda (produtos, quantidade e total).
