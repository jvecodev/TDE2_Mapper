# Atividade de Implementação de Algoritmos de Substituição de Páginas

Este repositório contém a implementação de três algoritmos de substituição de páginas (MRU, LRU e FIFO) como parte da avaliação do RA1 para a disciplina de `Performance de Sistemas Ciberfísicos`.


## Acadêmicos (Grupo)

| Nome Completo        | 
| ------------------- | 
| `João Vitor Correa Oliveira` |
| `Eduardo Henrique Fabri` |
| `Lucas Stopinski` |


---

## 🎥 Link do Vídeo Explicativo

O vídeo a seguir contém a explicação detalhada do projeto, abordando os conceitos teóricos de cada algoritmo, a implementação do código e a análise dos resultados obtidos nos testes.

- **Link:** `LINK NÃO LISTADO DO YOUTUBE`

---

## 📝 Descrição do Projeto

O objetivo deste trabalho é aprofundar o conhecimento sobre gerenciamento de memória em sistemas operacionais, especificamente nas políticas de substituição de páginas. Para isso, foram implementados os seguintes algoritmos na linguagem `[Python]`:

1.  **MRU (Most Recently Used / Mais Recentemente Usado)**
2.  **LRU (Least Recently Used / Menos Recentemente Usado)**
3.  **FIFO (First-In, First-Out / Primeiro a Entrar, Primeiro a Sair)**

Os algoritmos foram testados com sequências de páginas pré-definidas para uma memória com 8 quadros, e os resultados foram analisados para responder às questões propostas.

---

## 📂 Estrutura do Repositório

O projeto está organizado em dois diretórios principais, conforme solicitado:

```
/
├── com_comentarios/
│   ├── mru.py
│   ├── lru.py
│   └── fifo.py
│
├── sem_comentarios/
│   ├── mru.py
│   ├── lru.py
│   └── fifo.py
│
└── README.md
```

- **`com_comentarios/`**: Contém os códigos-fonte com todas as variáveis em português e comentários explicativos para facilitar o entendimento da lógica.
- **`sem_comentarios/`**: Contém os mesmos códigos, mas sem nenhum comentário, para fins de avaliação de autoria, caso necessário.


## ⚙️ Como Executar

Para executar os testes e verificar os resultados, siga os passos abaixo:

1.  Clone o repositório:
    ```sh
    git clone https://github.com/jvecodev/TDE2_Mapper
    ```

## 🧠 Explicação dos Algoritmos

### MRU (Most Recently Used)
O algoritmo MRU parte do princípio de que a página mais recentemente usada é a mais provável de não ser necessária em um futuro próximo. Portanto, quando ocorre uma falta de página e a memória está cheia, a página que foi acessada mais recentemente é a escolhida para ser substituída. Esta política pode ser útil em situações específicas, como acessos repetidos a um grande conjunto de dados onde os itens mais recentes são menos prováveis de serem revisitados imediatamente.

### LRU (Least Recently Used)
O algoritmo LRU se baseia na ideia de que as páginas usadas recentemente têm uma alta probabilidade de serem usadas novamente em breve (localidade temporal). Dessa forma, quando é preciso liberar um quadro de memória, o LRU substitui a página que não é utilizada há mais tempo. É uma das políticas mais eficientes, embora sua implementação possa ser mais complexa que a do FIFO.

### FIFO (First-In, First-Out)
Esta é a política mais simples. Ela gerencia os quadros de página como uma fila. A primeira página que foi alocada na memória será a primeira a ser removida quando um novo espaço for necessário. Sua principal desvantagem é que ela pode remover páginas importantes que são usadas com frequência, apenas porque estão na memória há mais tempo.

---

### 2 - Qual a melhor política de substituição?

Não existe uma única política de substituição que seja "a melhor" para todas as situações. A eficiência de um algoritmo depende diretamente do padrão de acesso às páginas gerado pelos programas em execução.

- O **LRU** é frequentemente considerado o melhor para um propósito geral, pois se aproxima do algoritmo ótimo (que é impossível de implementar na prática) e explora bem o princípio da localidade temporal, resultando em uma baixa taxa de *page faults* na maioria dos casos.
- O **FIFO** é o mais simples de implementar, mas seu desempenho pode ser inconsistente e sofrer da Anomalia de Belady (onde aumentar o número de quadros pode, paradoxalmente, aumentar o número de *page faults*).
- O **MRU** é situacional. Ele performa mal na maioria dos cenários de uso geral, mas se destaca em padrões de acesso específicos, como varreduras sequenciais completas em arquivos grandes, onde a página mais recentemente lida é de fato a menos provável de ser necessária novamente.

**Conclusão da análise:** Para as sequências de teste fornecidas e para a maioria das aplicações do dia a dia, o **LRU** tende a apresentar a melhor performance ao minimizar o número de faltas de página.
