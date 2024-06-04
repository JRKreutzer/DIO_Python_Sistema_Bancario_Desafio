# Sistema Bancário

Este é um código desenvolvido como parte do desafio proposto pelo Bootcamp Python Backend da Digital Innovation One. Trata-se de um programa simples de console em Python que simula algumas operações bancárias básicas, como depósito, saque e verificação de extrato.

## Funcionalidades

1. **Depositar:** Permite ao usuário adicionar fundos à sua conta bancária.
2. **Sacar:** Permite ao usuário retirar fundos da sua conta bancária, com a devida validação do saldo e do limite de saque diário.
3. **Extrato:** Mostra ao usuário o saldo atual da conta, bem como o registro de todas as transações realizadas.
4. **Sair:** Encerra o programa.

## Requisitos

- Python 3.x instalado no sistema.

## Como Usar

1. Clone este repositório ou faça o download do arquivo `menu_bancario.py`.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo `sistema_bancario.py` está localizado.
4. Execute o seguinte comando: python sistema_bancario.py
5. Siga as instruções apresentadas no console para realizar as operações desejadas.

## Observações

- Certifique-se de inserir apenas valores válidos ao realizar depósitos e saques.
- O limite de saques diários é configurado para 3, mas pode ser ajustado alterando a variável `LIMITE_SAQUES`.
- O limite de saque por transação é de R$ 500,00, mas também pode ser alterado, se necessário, modificando a variável `limite`.
- As mensagens de erro e confirmação foram projetadas para orientar o usuário durante a interação com o programa.

Este programa foi desenvolvido como uma demonstração educacional e não deve ser utilizado para transações financeiras reais.

## Autor

Desenvolvido por José Rodolfo Kreutzer - [jose.kreutzer@gmail.com]

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar sugestões de melhorias, relatar problemas ou enviar solicitações de pull requests.
