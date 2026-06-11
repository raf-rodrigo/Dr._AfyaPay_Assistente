# 🩺 Dr. AfyaPay Assistente

> Assistente Virtual e Mentor Financeiro inteligente guiado por IA Generativa.

O **Dr. AfyaPay Assistente** é uma aplicação interativa desenvolvida como o projeto final do **Bootcamp Afya - Automação de Dados com IA** na plataforma **DIO (Digital Innovation One)**. A solução combina princípios de experiência do usuário (UX), automação em Python e a inteligência do modelo Gemini para oferecer suporte a decisões e simulações financeiras de forma clara, segura e amigável.

---

## 🚀 Funcionalidades Principais

- **🧠 Chat com Memória de Contexto:** O assistente mantém a linha de raciocínio e lembra do histórico da conversa durante a sessão (via `st.session_state`).
- **💡 FAQ Inteligente Integrado:** Respostas rápidas e precisas sobre investimentos iniciais, reserva de emergência e as diferenças entre renda fixa e renda variável.
- **📊 Simulação de Juros Compostos (Automação Real):** Integração com código Python utilizando **Function Calling (Tools)** do Gemini. O modelo compreende a intenção do usuário em linguagem natural, extrai os parâmetros (capital, taxa, tempo), executa a função Python e exibe o resultado formatado.
- **🎨 Design Premium (UX):** Interface moderna construída em Streamlit com estilizações em CSS personalizado, garantindo leitura agradável e usabilidade simples.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3.10+](https://www.python.org/)
- **Interface Gráfica (Frontend):** [Streamlit](https://streamlit.io/)
- **Inteligência Artificial:** [Google GenAI SDK](https://github.com/google/generative-ai-python) (Modelo: `gemini-2.5-flash`)
- **Variáveis de Ambiente:** [python-dotenv](https://github.com/theofidry/django-dotenv)

---

## 📂 Estrutura do Projeto

```text
dr-afyapay-assistente/
├── venv/                   # Ambiente virtual Python (ignorado no git)
├── .env                    # Chaves de API de forma segura (ignorado no git)
├── .env.example            # Exemplo de configuração de variáveis
├── .gitignore              # Configuração de arquivos ignorados pelo Git
├── README.md               # Documentação principal do projeto
└── app.py                  # Código-fonte da aplicação Streamlit e IA
```

---

## ⚙️ Instalação e Execução Local

### Pré-requisitos
Certifique-se de ter o Python 3.10 ou superior instalado no seu sistema.

### 1. Clonar o Repositório e Entrar na Pasta
```bash
git clone https://github.com/SEU-USUARIO/dr-afyapay-assistente.git
cd dr-afyapay-assistente
```

### 2. Criar e Ativar o Ambiente Virtual
*No Linux/macOS:*
```bash
python3 -m venv venv
source venv/bin/activate
```
*No Windows (Command Prompt):*
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```
*(Caso não possua o arquivo requirements.txt, instale diretamente: `pip install streamlit google-genai python-dotenv`)*

### 4. Configurar a Chave da API
Crie um arquivo `.env` na raiz do projeto (ou renomeie o `.env.example`) e insira a sua chave de API do Gemini:
```env
GEMINI_API_KEY=sua_chave_de_api_aqui
```
> ⚠️ **Importante:** Nunca publique a sua chave de API em repositórios públicos do GitHub. O arquivo `.env` já está listado no `.gitignore` para sua segurança.

### 5. Executar a Aplicação
```bash
python -m streamlit run app.py
```
Acesse a aplicação abrindo o link no navegador: **`http://localhost:8501`**

---

## 🎓 Sobre o Bootcamp
Este projeto consolida o aprendizado prático em:
1. **Lógica e Estrutura de Dados:** Utilização de Python vanilla para cálculos financeiros exatos.
2. **Integração de APIs e IA Generativa:** Conexão robusta com o ecossistema Gemini.
3. **Engenharia de Prompts & UX:** Definição de personas de atendimento automatizado eficazes.

Desenvolvido por **[Seu Nome/GitHub]** como projeto prático para a conclusão do Bootcamp Afya.

---

## 👨‍💻 Autor

Desenvolvido por **Rafael Rodrigo** como projeto prático para conclusão do **Bootcamp Afya – Automação de Dados com IA** na plataforma DIO.

GitHub: https://github.com/raf-rodrigo
LinkedIn: https://www.linkedin.com/in/rafael-rodrigo-doimo