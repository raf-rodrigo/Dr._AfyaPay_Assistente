# Pitch (3 minutos)

> [!TIP]
> Você pode usar alguns slides para apoiar o pitch e mostrar o agente funcionando no Streamlit. Uma gravação curta da tela também ajuda a demonstrar a solução de forma objetiva.

---

## Roteiro Sugerido

### 1. O Problema

Muitas pessoas têm dificuldade para organizar a vida financeira, entender conceitos básicos de investimento e simular o impacto de juros ao longo do tempo. Além disso, em contextos de atendimento financeiro, respostas genéricas ou imprecisas podem gerar insegurança, decisões ruins e perda de confiança.

O problema que o **Dr. AfyaPay Assistente** resolve é a falta de um apoio simples, acessível e seguro para orientar usuários em dúvidas financeiras, explicar conceitos essenciais e realizar simulações matemáticas com clareza.

---

### 2. A Solução

O **Dr. AfyaPay Assistente** é um agente financeiro inteligente criado com Python, Streamlit e Gemini. Ele atua como um mentor financeiro digital, com uma persona clara, tom amigável e regras de segurança para evitar respostas inventadas.

A solução combina quatro elementos principais:

- **Chat com memória de sessão:** o agente mantém o contexto da conversa durante o uso.
- **FAQ financeiro integrado:** responde dúvidas sobre reserva de emergência, renda fixa, renda variável e primeiros investimentos.
- **Function Calling:** quando o usuário pede uma simulação, o agente aciona uma função Python para calcular juros compostos com mais precisão.
- **Base de conhecimento mockada:** os arquivos da pasta `data/` representam perfil de investidor, produtos financeiros, transações, histórico de atendimento e regras regulatórias para evoluções do agente.

Com isso, o projeto demonstra como IA generativa pode ser combinada com automação em Python para criar um atendimento financeiro mais claro, seguro e útil.

---

### 3. Demonstração

Na demonstração, mostre o agente funcionando na prática pelo Streamlit.

Sugestão de sequência:

1. ![](image-principal-do-agente.png)
2. ![](imagem-com-sidebar.png)
3. Fazer uma pergunta conceitual:

```text
O que é uma reserva de emergência?
```
![](imagem-com-pergunta.png)

4. Resposta estruturada do agente:
```
Olá! Que ótimas perguntas para começarmos a organizar suas finanças!

Vamos por partes:

O que é uma Reserva de Emergência?
Uma Reserva de Emergência é um valor que você guarda para usar em situações inesperadas, como despesas médicas urgentes, perda de emprego, conserto de carro ou qualquer imprevisto que possa surgir. É como um "colchão" financeiro para te dar tranquilidade.

Características importantes:

Montante: O ideal é ter de 3 a 6 meses do seu custo de vida mensal guardado. Se suas despesas mensais são R 1.000, por exemplo, você deveria ter entre R 3.000 e R$ 6.000.
Local Seguro: Deve estar em um lugar seguro, onde não haja risco de perder o dinheiro.
Liquidez Diária: É fundamental que você possa resgatar o dinheiro a qualquer momento, sem perdas ou burocracia.
Qual a melhor aplicação para investir com pouco?
Considerando que você tem R$ 500 para começar a investir, e pensando em aplicações acessíveis e com boa segurança, minhas sugestões são:

Tesouro Direto: Especialmente o Tesouro Selic, que acompanha a taxa básica de juros, tem baixo risco e liquidez diária. É ótimo para iniciantes!
CDBs (Certificados de Depósito Bancário) de 100% do CDI com liquidez diária: Muitos bancos e corretoras oferecem CDBs que rendem 100% do CDI (taxa de juros de referência do mercado) e permitem o resgate a qualquer momento. Também são seguros, pois contam com a proteção do FGC (Fundo Garantidor de Créditos) para valores até R$ 250 mil por CPF e por instituição.
Ambas as opções são excelentes para quem está começando e busca segurança e a possibilidade de resgatar o dinheiro quando precisar.

Simulação de Investimento de R$ 500 por 10 meses
Para calcular o montante final de um investimento de R$ 500 por 10 meses, preciso de mais uma informação: a taxa de juros anual da aplicação.

Com a taxa de juros, posso fazer uma simulação precisa para você! Por exemplo, se a taxa for de 10% ao ano, 12% ao ano, ou outra.

Assim que me informar a taxa, farei o cálculo com prazer!

Estou aqui para te ajudar a entender melhor cada passo!
```

5. Fazer uma simulação financeira:

```text
Quero simular um investimento de R$ 5.000 a 10% ao ano por 5 anos.
```
```
Com um investimento inicial de R 5.000,00** a uma taxa de **10% ao ano** durante **5 anos**, seu montante final será de **R 8.052,55.

Isso significa que você terá ganhado R$ 3.052,55 em juros ao longo desse período. É o poder dos juros compostos trabalhando para você!

Estou à disposição para mais simulações ou dúvidas!
``` 

6. O agente usa a ferramenta `calcular_juros_compostos` para executar o cálculo em Python.
7. A pasta `docs/` está com a documentação do agente, base de conhecimento, prompts, avaliações e pitch.

O projeto não é apenas um chatbot: ele tem persona, regras, memória, documentação, base mockada e uma ferramenta real de cálculo.

---

### 4. Diferencial e Impacto

O diferencial do **Dr. AfyaPay Assistente** está na combinação entre IA generativa e lógica determinística. O modelo conversa com o usuário de forma natural, mas os cálculos financeiros são executados por código Python, reduzindo o risco de erro numérico.

O impacto social está em tornar educação financeira mais acessível. Um assistente como esse pode ajudar pessoas a entenderem reserva de emergência, investimentos iniciais, riscos e planejamento financeiro sem linguagem complicada.

Além disso, o projeto mostra uma arquitetura simples e evolutiva: no futuro, os dados mockados podem ser integrados diretamente ao agente para gerar alertas de gastos, recomendações mais personalizadas e análises de perfil.

---

## Roteiro de Fala Resumido

```text
Olá, eu sou Rafael Rodrigo e este é o Dr. AfyaPay Assistente, meu projeto final do Bootcamp Afya de Automação de Dados com IA na DIO.

O problema que eu quis resolver é a dificuldade que muitas pessoas têm para entender conceitos financeiros, organizar decisões simples e simular investimentos com segurança. Em finanças, uma resposta errada ou inventada pode gerar insegurança e decisões ruins.

A solução é um agente financeiro inteligente desenvolvido com Python, Streamlit e Gemini. Ele funciona como um mentor financeiro digital, com uma persona amigável, memória de conversa, FAQ integrado e regras de segurança para evitar alucinações.

Um dos diferenciais é o uso de Function Calling. Quando o usuário pede uma simulação de juros compostos, o Gemini entende a intenção e chama uma função Python, que faz o cálculo de forma determinística. Assim, o modelo não precisa inventar o resultado.

Na prática, o usuário pode perguntar o que é uma reserva de emergência, entender a diferença entre renda fixa e renda variável ou simular um investimento, por exemplo: R$ 5.000 a 10% ao ano por 5 anos.

O projeto também possui uma base mockada com perfil de investidor, produtos financeiros, transações, histórico de atendimento e regras regulatórias. Esses dados mostram como o agente pode evoluir para análises mais personalizadas no futuro.

O impacto da solução é tornar educação financeira mais acessível, clara e segura. O Dr. AfyaPay mostra como IA generativa e automação em Python podem trabalhar juntas para melhorar o relacionamento financeiro com o usuário.
```


