# Game - Circle the Cat


Como isso funciona?

**Cat** - O algoritimo usado para o gato se movimentar foi o **_busca em largura_**, para cada coordenada em volta ele busca todas as opções e no fim guarda em uma lista o caminho com menos movimentos até saída. <br />

**Catcher** - Para o pegador foi utilizado duas técnicas, para bloquear a saída mais próxima foi usado o algotimo de **_busca em largura_**, o mesmo utilizado no gato para se encontrar a saída mais próxima, e a segunda técnica foi moldar o tabuleiro para um formato que seria mais eficaz para conseguir prender o gato, o molde utilizado foi o hexágono (hexágono é a forma com maior área e menor perimetro, então seria o modo mais fácil de prender o gato).

| Hexágonos  | Exemplo de funcionamento  |
| --- | --- |
|  <img src="/Hexagons.png">  |  <img src="/game.gif">  |

### Legenda

![#000000](https://placehold.it/15/000000/000000?text=+) - Gato<br>
![#1589F0](https://placehold.it/15/1589F0/000000?text=+) - Saídas<br>
![#f03c15](https://placehold.it/15/f03c15/000000?text=+) - Bloqueados

### Como executar
```python
python3 game.py "Posicão inicial do gato" "[ Bloqueios iniciais ]" "[ Saídas ]"
```
### Exemplo

```python
python3 game.py "(5, 5)" "[(3, 6), (8, 7), (0, 7), (0, 8), (8, 2), (4, 10)]" "[(0, 0), (0, 0), (10, 0), (0, 10), (0, 1), (1, 0), (10, 1), (1, 10), (0, 2), (2, 0), (10, 2), (2, 10), (0, 3), (3, 0), (10, 3), (3, 10), (0, 4), (4, 0), (10, 4), (4, 10), (0, 5), (5, 0), (10, 5), (5, 10), (0, 6), (6, 0), (10, 6), (6, 10), (0, 7), (7, 0), (10, 7), (7, 10), (0, 8), (8, 0), (10, 8), (8, 10), (0, 9), (9, 0), (10, 9), (9, 10), (0, 10), (10, 0), (10, 10), (10, 10)]"
```
Um gif no diretório será criado após a execução - `game.gif`

Desenvolvedores:<br/>
[Alfredo Albélis](https://github.com/AlfredoFilho)<br/>
[Brenda Alexsandra](https://github.com/brendajanuario)<br/>
[Cléofas Peres](https://github.com/CleoPeres)<br/> 
