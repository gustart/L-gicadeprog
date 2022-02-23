Algoritmo "media"

Var
    nota1,nota2,media: real


Inicio

       escreva("Insira a primeira nota: " )
       leia(nota1)
       
       escreva("Insira a segunda nota: ")
       leia(nota2)
       
       media := (nota1 + nota2)/2
       
       escreva("A media do aluno foi: " , media)
       
       
       se(media >= 6) entao
                escreva("O aluno está aprovado com media: " , media)
       senao
            escreva("O aluno esrtá reprovado com média: " , media)
       
          fimse
Fimalgoritmo