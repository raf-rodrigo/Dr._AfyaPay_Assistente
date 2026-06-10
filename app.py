import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Carregar variáveis de ambiente do arquivo .env (com override para detectar mudanças sem reiniciar o servidor)
load_dotenv(override=True)

# Configuração da página Streamlit
st.set_page_config(
    page_title="Dr. AfyaPay Assistente",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização CSS personalizada para um design premium
st.markdown("""
<style>
    /* Estilo geral */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Cabeçalho principal com gradiente */
    .main-title {
        background: linear-gradient(135deg, #0d6efd 0%, #0dcaf0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    
    .subtitle {
        color: #6c757d;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Estilo dos cards de FAQ */
    .faq-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        border-left: 5px solid #0d6efd;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .faq-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    
    .faq-question {
        color: #212529;
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 0.5rem;
    }
    
    .faq-answer {
        color: #495057;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    /* Rodapé */
    .footer {
        text-align: center;
        color: #adb5bd;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #dee2e6;
    }
</style>
""", unsafe_allow_html=True)

# Função de cálculo financeiro (Tool/Function Calling para o Gemini)
def calcular_juros_compostos(capital_inicial: float, taxa_juros_anual: float, tempo_anos: int) -> str:
    """
    Calcula o montante final obtido através de juros compostos.
    Use esta função SEMPRE que o usuário solicitar uma simulação de investimento,
    cálculo de juros compostos, projeção de rendimento financeiro ou simulações similares.

    Args:
        capital_inicial: O valor inicial investido em reais (R$) (ex: 1000.0)
        taxa_juros_anual: A taxa de juros anual em porcentagem (ex: 12.5 para 12.5% ao ano)
        tempo_anos: O período do investimento em anos (ex: 5)
    """
    try:
        taxa_decimal = taxa_juros_anual / 100
        montante = capital_inicial * (1 + taxa_decimal) ** tempo_anos
        juros_acumulados = montante - capital_inicial
        
        # Formata o retorno como uma string organizada
        return (
            f"**Cálculo de Juros Compostos Realizado com Sucesso!**\n\n"
            f"- **Capital Inicial:** R$ {capital_inicial:,.2f}\n"
            f"- **Taxa de Juros:** {taxa_juros_anual}% ao ano\n"
            f"- **Tempo:** {tempo_anos} anos\n"
            f"- **Total de Juros Ganhos:** R$ {juros_acumulados:,.2f}\n"
            f"- **Montante Final:** R$ {montante:,.2f}"
        )
    except Exception as e:
        return f"Erro ao calcular juros compostos: {e}"

# Cabeçalho da aplicação
st.markdown('<div class="main-title">🩺 Dr. AfyaPay Assistente</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Seu assistente virtual de relacionamento e educação financeira</div>', unsafe_allow_html=True)

# FAQ Data
faqs = [
    {
        "question": "💡 Como começo a investir com pouco dinheiro?",
        "answer": "Você pode começar com menos de R$ 30,00 no Tesouro Direto ou em CDBs que rendem 100% do CDI com liquidez diária. O importante é a consistência."
    },
    {
        "question": "📊 Qual a diferença entre Renda Fixa e Renda Variável?",
        "answer": "Na Renda Fixa, você conhece as regras de rendimento antes de investir (é mais seguro). Na Renda Variável (como ações), o rendimento oscila de acordo com o mercado (maior risco, mas potencial de maior retorno)."
    },
    {
        "question": "🛡️ O que é uma Reserva de Emergência?",
        "answer": "É um valor guardado em um investimento seguro e de fácil resgate (liquidez diária), equivalente a 3 a 6 meses do seu custo de vida, para cobrir imprevistos cotidianos sem contrair dívidas."
    }
]

# Sidebar com informações do projeto e FAQ de consulta rápida
with st.sidebar:
    st.header("Sobre o Dr. AfyaPay")
    st.info("""
    Este assistente foi desenvolvido como o projeto final do **Bootcamp Afya - Automação de Dados com IA** na plataforma DIO.
    
    Ele combina Inteligência Artificial Generativa com lógica financeira para auxiliar no relacionamento com o cliente.
    """)
    st.write("---")
    st.subheader("💡 Funções Especiais")
    st.markdown("""
    Você pode pedir simulações matemáticas como:
    *   *"Quero simular um investimento de R$ 5000 a 10% ao ano por 5 anos."*
    *   *"Calcule os juros de 2000 reais com taxa de 8.5% ao ano durante 10 anos."*
    """)
    st.write("---")
    st.subheader("Perguntas Frequentes (FAQ)")
    for faq in faqs:
        st.markdown(f"**{faq['question']}**")
        st.write(faq['answer'])
        st.write("---")

# Verificar se a chave API está configurada
api_key = os.getenv("GEMINI_API_KEY") or ""
is_configured = api_key != "" and "YOUR_GEMINI_API_KEY" not in api_key

if not is_configured:
    st.warning("⚠️ **Chave de API do Gemini não configurada!**")
    st.info("""
    Para utilizar a inteligência do assistente, você precisa adicionar sua chave de API do Gemini:
    1. Abra o arquivo `.env` localizado na raiz do projeto.
    2. Substitua `YOUR_GEMINI_API_KEY_HERE` pela sua chave real obtida no Google AI Studio.
    3. Salve o arquivo e atualize esta página.
    """)
    
    st.write("### 📌 Visualize nosso FAQ enquanto configura a API:")
    for faq in faqs:
        st.markdown(f"""
        <div class="faq-card">
            <div class="faq-question">{faq['question']}</div>
            <div class="faq-answer">{faq['answer']}</div>
        </div>
        """, unsafe_allow_html=True)
else:
    # Se a API estiver configurada, inicializa o cliente Gemini
    try:
        client = genai.Client()
    except Exception as e:
        st.error(f"Erro ao inicializar o cliente Gemini: {e}")
        st.stop()

    # Inicializa o histórico de mensagens se não existir
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Olá! Sou o **Dr. AfyaPay Assistente**, seu mentor financeiro digital. Como posso ajudar nas suas decisões financeiras, dúvidas de investimento ou simulações hoje?"}
        ]

    # Exibe o histórico de mensagens
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Entrada do chat
    if prompt := st.chat_input("Digite sua dúvida financeira aqui..."):
        # Adiciona a mensagem do usuário no histórico e exibe
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Prepara a chamada para a API
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("*Pensando...*")
            
            try:
                # Instruções de Persona do Dr. AfyaPay
                system_instruction = (
                    "Você é o Dr. AfyaPay Assistente, um assistente virtual e mentor financeiro inteligente "
                    "criado para ajudar os usuários no relacionamento com finanças. Seu tom de voz é amigável, "
                    "seguro, claro e educado. Utilize sempre formatação rica (markdown, listas, negrito) para estruturar "
                    "suas respostas. Caso o usuário peça simulações matemáticas de juros, use a ferramenta "
                    "calcular_juros_compostos fornecida.\n\n"
                    "Caso o usuário faça perguntas sobre os tópicos de FAQ abaixo, utilize as informações "
                    "para responder de forma alinhada:\n"
                    "1. Investir com pouco: Tesouro Direto ou CDBs de 100% CDI com liquidez diária.\n"
                    "2. Renda Fixa vs Variável: Renda Fixa tem regras definidas e segurança; Renda Variável oscila e tem maior risco.\n"
                    "3. Reserva de Emergência: 3 a 6 meses de custo de vida em local seguro e liquidez diária.\n\n"
                    "Seja direto e encorajador. Evite responder a tópicos totalmente fora do contexto financeiro ou do projeto AfyaPay."
                )

                # Monta a conversa a partir do histórico
                # Traduz roles do Streamlit ('assistant'/'user') para os tipos do SDK ('model'/'user')
                contents = []
                for msg in st.session_state.messages[1:]:  # Pula a primeira de boas-vindas para o modelo
                    role = "user" if msg["role"] == "user" else "model"
                    contents.append(types.Content(
                        role=role,
                        parts=[types.Part.from_text(text=msg["content"])]
                    ))

                # Faz a chamada com suporte a chamada automática de função (Automatic Function Calling)
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        tools=[calcular_juros_compostos],
                        temperature=0.7,
                    )
                )

                response_text = response.text
                message_placeholder.markdown(response_text)
                
                # Salva a resposta no histórico
                st.session_state.messages.append({"role": "assistant", "content": response_text})

            except Exception as e:
                message_placeholder.markdown(f"❌ Desculpe, ocorreu um erro ao processar sua solicitação: {e}")

# Rodapé
st.markdown('<div class="footer">Desenvolvido com ❤️ no Bootcamp Afya & DIO</div>', unsafe_allow_html=True)
