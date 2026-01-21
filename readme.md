# 🤖 ChatSUAS

ChatSUAS é um chatbot local, desenvolvido em Python, voltado para **Ciências Sociais, Política Social e Sistema Único de Assistência Social (SUAS)**.

O projeto tem como objetivo experimentar o uso de **modelos de linguagem locais (LLM)** para apoio técnico, estudo e prototipagem de ferramentas voltadas à política pública de assistência social.

> ⚠️ Importante: este projeto é **experimental** e foi desenvolvido considerando **limitações reais de hardware**, priorizando transparência técnica e reprodutibilidade.

---

## Objetivos do Projeto

* Explorar o uso de LLMs locais aplicados ao SUAS
* Criar um chatbot especializado em política social brasileira
* Demonstrar integração entre **Python + Streamlit + Ollama**
* Servir como item de portfólio técnico-acadêmico
* Avaliar limites práticos de IA local em máquinas modestas

---

## Escopo Temático

O ChatSUAS foi concebido para responder perguntas relacionadas a:

* Sistema Único de Assistência Social (SUAS)
* LOAS (Lei nº 8.742/1993)
* Política Nacional de Assistência Social (PNAS)
* Proteção Social Básica e Especial
* CRAS, CREAS e serviços socioassistenciais
* Direitos socioassistenciais e garantia de direitos

O chatbot **não** é voltado para saúde, educação ou previdência.

---

## Arquitetura do Projeto

* **Linguagem:** Python 3.11+
* **Interface:** Streamlit
* **Modelo de linguagem:** LLM local via Ollama
* **Modelo utilizado:** `phi3:mini` (leve, experimental)
* **Execução:** Local (offline)

Fluxo simplificado:

```
Usuário → Streamlit (UI) → Python → Ollama (LLM local) → Resposta
```

---

## Requisitos de Sistema

### Mínimo (testado)

* Windows 10/11
* Python 3.11+
* 8 GB de RAM (funciona no limite)
* CPU comum (sem GPU dedicada)

⚠️ Em máquinas com menos memória disponível, o sistema pode apresentar **lentidão ou travamentos**.

---

## Dependências

Instalação das bibliotecas Python:

```bash
pip install streamlit
```

Instalação do Ollama:

* [https://ollama.com](https://ollama.com)

Download do modelo:

```bash
ollama pull phi3:mini
```

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chat-suas.git
cd chat-suas
```

2. Inicie o Streamlit:

```bash
streamlit run main.py
```

3. Acesse no navegador:

```
http://localhost:8501
```

---

## Funcionamento Interno

* As mensagens são gerenciadas via `st.session_state`
* O prompt é **minimalista** para reduzir uso de memória
* Não há persistência de memória longa
* Cada pergunta gera uma chamada direta ao modelo local

Essa abordagem foi adotada para garantir que o sistema rode em hardware limitado.

---

## Limitações Conhecidas

* Respostas podem ser lentas em máquinas com pouca RAM
* Modelos pequenos apresentam limitações conceituais
* Possibilidade de confusão semântica (ex: SUAS × SUS)
* Não indicado para uso institucional ou atendimento real

Este projeto **não substitui profissionais** nem decisões técnicas oficiais.

---

## Motivação Acadêmica e Política

O projeto surge da interseção entre:

* Ciências Sociais
* Política pública
* Tecnologia
* Crítica ao fetichismo tecnológico

A proposta é **experimentar**, não fetichizar a IA, evidenciando seus limites quando aplicada a políticas sociais concretas.

---

## Próximos Passos (Roadmap)

* [ ] Chat normativo baseado em regras (sem LLM)
* [ ] Base de conhecimento estruturada (LOAS, PNAS, NOB)
* [ ] Separação de modos: usuário / trabalhador / gestor
* [ ] Migração para backend leve (FastAPI)
* [ ] Avaliação ética e institucional

---

## Licença

Projeto de caráter educacional e experimental.
Licença: MIT (ou outra, a definir).

---

## Autor

**Chico Alves**
Sociólogo | Analista de Dados | Pesquisador em Política Social

> Este projeto integra um portfólio técnico-crítico sobre tecnologia e políticas públicas no Brasil.
