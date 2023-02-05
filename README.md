# MBA - Engenharia de Software: Exercício de Teste de Unidade e TDD (Software Quality and Metrics)

## Atividade 01
Como usuário gostaria de uma funcionalidade que valide se uma frase ou palavra é
palíndromo.
#### Critérios de aceite:
##### Verdadeiro:
* “Rotator”
* “bob”
* “madam”
* “mAlAyAlam”
* “1”
* “Able was I, ere I saw Elba”
* “Madam I’m Adam”
* “Step on no pets.”
* “Top spot!”
* “02/02/2020”
* “Socorram-me subi no ônibus em marrocos”
##### Falso:
* “xyz”
* “elephant”
* “Country”
* “Top . post!”
* “Wonderful-fool”
* “Wild imagination!”

O componente deve receber os exemplos acima e retornar verdadeiro ou falso, conforme a
regra. **Fazer o componente usando a metodologia TDD.** Atividade em grupo ou individual.
Enviar a URL do Github com todo o código fonte.
Fonte: [Wiki Palindrome](https://en.wikipedia.org/wiki/Palindrome)


## Execução da atividade
Usando a metodologia *Test Driven Development*(TDD), foi criado inicialmente o teste para verificação do palíndromo, cujo código se encontra em: `src/palindrome_test.py`:
 ```
python palindrome-test.py -v

Traceback (most recent call last):
  File "/home/gian/Documentos/MBA - Engenharia de Software/Software Quality and Metrics/mba.engenharia-software.software-quality.tdd-unitytesting/src/palindrome-test.py", line 4, in <module>
    class TestPalindrome(unittest.TestCase):
  File "/home/gian/Documentos/MBA - Engenharia de Software/Software Quality and Metrics/mba.engenharia-software.software-quality.tdd-unitytesting/src/palindrome-test.py", line 5, in TestPalindrome
    palindromes = Palindrome() 
NameError: name 'Palindrome' is not defined
 ```
O erro acima já era esperado, tento em vista de que o teste foi criado sem ter o código implementado. 
Com isto, segue-se a implementação do código de palídromo para as palavras palíndromas somente:
```
python palindrome_test.py -v

test_palindrome_sentence (__main__.TestPalindrome) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Após isso, foi implementado um novo teste para as palavras normais, tendo o seguinte resultado:
```
python palindrome_test.py -v
test_normal_words (__main__.TestPalindrome) ... expected failure
test_palindrome_words (__main__.TestPalindrome) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK (expected failures=1)
```
