# Base de Conhecimento

Este documento descreve os dados utilizados pelo **Dr. AfyaPay Assistente** e como eles apoiam o comportamento do agente financeiro.

---

## Dados Utilizados

A base de conhecimento do projeto fica na pasta `data/` e foi criada com dados mockados para simular um cenário real de atendimento financeiro, perfil de cliente, produtos disponíveis, regras regulatórias e histórico de movimentações.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|----------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores do cliente com os canais de atendimento |
| `perfil_investidor.json` | JSON | Personalizar respostas conforme renda, metas, perfil de risco e reserva atual |
| `produtos_financeiros.json` | JSON | Apoiar sugestões educativas de produtos adequados ao perfil e objetivo do cliente |
| `regulatorio_financeiro.json` | JSON | Responder com mais segurança sobre FGC, CDI, poupança e órgãos reguladores |
| `transacoes.csv` | CSV | Analisar receitas, despesas, categorias de gasto e possíveis alertas financeiros |

> [!TIP]
> Para deixar a base mais robusta em versões futuras, o projeto pode usar datasets públicos de finanças, como bases disponíveis no [Hugging Face](https://huggingface.co/datasets), desde que os dados estejam alinhados ao contexto do desafio e não contenham informações sensíveis reais.

---

## Adaptações nos Dados

Os dados foram organizados e expandidos em arquivos separados para representar diferentes partes do contexto financeiro do cliente.

Foram criados:

- um perfil de investidor fictício, com renda mensal, patrimônio, reserva de emergência e metas;
- um catálogo de produtos financeiros com categoria, risco, rentabilidade, aporte mínimo e indicação de uso;
- um histórico de transações com entradas e saídas;
- um histórico de atendimentos anteriores;
- uma base regulatória simplificada com conceitos úteis para respostas financeiras.

Esses dados não representam clientes reais. Eles foram criados apenas para fins de demonstração, documentação e teste do agente.

---

## Estratégia de Integração

### Como os dados são carregados?

No estado atual do projeto, os arquivos da pasta `data/` estão disponíveis como base mockada documentada, mas ainda não são carregados automaticamente pelo `app.py`.

A implementação atual usa:

- FAQ fixo definido diretamente no código;
- histórico de conversa via `st.session_state`;
- chamada ao Gemini com `system_instruction`;
- função Python `calcular_juros_compostos` como ferramenta de cálculo.

Em uma próxima evolução, os arquivos JSON e CSV podem ser carregados no início da aplicação usando `json` e `csv` ou `pandas`, e então transformados em um resumo textual para compor o contexto do agente.

Exemplo de estratégia futura:

```text
1. Carregar perfil_investidor.json
2. Carregar produtos_financeiros.json
3. Carregar transacoes.csv
4. Carregar historico_atendimento.csv
5. Carregar regulatorio_financeiro.json
6. Montar um bloco de contexto financeiro
7. Enviar esse contexto no system prompt ou consultar por tools
```

### Como os dados são usados no prompt?

A estratégia recomendada é usar os dados de duas formas:

1. **Contexto no prompt:** incluir um resumo curto do perfil, metas, produtos e regras mais importantes no `system_instruction`.
2. **Consulta dinâmica por tools:** criar funções específicas para buscar informações de perfil, produtos, transações e regras quando o usuário fizer uma pergunta relacionada.

Para evitar respostas inventadas, o agente deve priorizar os dados da base e informar quando não encontrar uma informação confiável.

---

## Exemplo de Contexto Montado

Abaixo está um exemplo de como os dados poderiam ser formatados e enviados ao modelo como contexto do agente.

```text
Dados do Cliente:
- Nome: João Silva
- Idade: 32 anos
- Profissão: Analista de Sistemas
- Perfil de investidor: Moderado
- Renda mensal: R$ 5.000,00
- Patrimônio total: R$ 15.000,00
- Reserva de emergência atual: R$ 10.000,00
- Objetivo principal: Construir reserva de emergência
- Aceita risco: Não

Metas financeiras:
- Completar reserva de emergência: R$ 15.000,00 até 2026-06
- Entrada do apartamento: R$ 50.000,00 até 2027-12

Produtos disponíveis:
- Tesouro Selic: renda fixa, risco baixo, aporte mínimo de R$ 30,00
- CDB Liquidez Diária: renda fixa, risco baixo, aporte mínimo de R$ 100,00
- LCI/LCA: renda fixa, risco baixo, aporte mínimo de R$ 1.000,00
- Fundo Multimercado: fundo, risco médio, aporte mínimo de R$ 500,00
- Fundo de Ações: fundo, risco alto, aporte mínimo de R$ 100,00

Últimas transações:
- 2025-10-01: Salário - R$ 5.000,00
- 2025-10-02: Aluguel - R$ 1.200,00
- 2025-10-03: Supermercado - R$ 450,00
- 2025-10-05: Netflix - R$ 55,90
- 2025-10-10: Restaurante - R$ 120,00

Regras financeiras relevantes:
- FGC cobre até R$ 250.000,00 por instituição e CPF/CNPJ.
- Tesouro Direto não possui garantia do FGC; possui garantia do Governo Federal.
- CDI é uma taxa usada como referência para produtos de renda fixa privada.
```

---

## Cuidados de Uso

- Os dados são fictícios e usados apenas para simulação.
- O agente não deve inventar produtos, taxas ou regras fora da base.
- Recomendações devem ser educativas, não promessas de rentabilidade.
- Informações sensíveis reais não devem ser adicionadas aos arquivos mockados.
- Perguntas fora do escopo financeiro devem ser recusadas de forma educada.

---

## Melhorias Futuras

- Carregar os dados automaticamente no `app.py`.
- Criar uma função para montar o contexto do agente a partir da pasta `data/`.
- Criar tools para consultar perfil, produtos, transações e regras.
- Adicionar validação dos arquivos JSON e CSV.
- Incluir testes para garantir que o agente use a base corretamente.
