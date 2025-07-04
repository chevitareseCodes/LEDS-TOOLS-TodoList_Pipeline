
# 🚀 Capeta

Repositório central do workflow de desenvolvimento utilizando as ferramentas **Andes**, **Spark**, **Made** e **Code-Wise**, criado durante a disciplina *Projeto de Sistemas* ministrada pelo Prof. Paulo Sérgio.

O repositório integra automaticamente essas ferramentas a partir de um único ponto de entrada: o commit de um arquivo `.andes`.

---

## 🧰 Ferramentas Integradas

### 🟠 Andes
Define um arquivo `.andes` e, com base nele, gera:
- `.spark` (entrada para o Spark)
- `.made` (entrada para o Made)
- Documentação em `.md`

**Uso**:
```bash
npm install andes-leds-tools@latest
npx andes-cli generate caminho/do/arquivo.andes
```

---

### 🔥 Spark
Com base em um `.spark`, o Spark gera o projeto completo com:
- **Frontend**: Vue + Tailwind
- **Backend**: 
  - Python + Django (MVC)
  - C# com .NET (MinimalAPI ou Clean Architecture)
  - Java com Spring Boot

**Uso**:
```bash
npm install spark-leds-beta@latest
npx spark-cli generate caminho/do/arquivo.spark
```

---

### 🛠️ Made
Com o `.made`, gera automaticamente issues no GitHub conforme a modelagem definida.

> **Necessário configurar variáveis de ambiente para autenticação no GitHub.**

**Uso**:
```bash
npm install made-beta
npx made-cli github caminho/do/arquivo.made
```

---

### 🧠 Code-Wise
Ferramenta escrita em Python que analisa os commits realizados e sugere melhorias com base nos pushes para o repositório.

**Instalação**:
```bash
pip install code-wise
```

---

## 🔁 Workflow Automatizado

O repositório está configurado com um fluxo de trabalho automatizado via GitHub Actions:

1. O usuário **commita um arquivo `.andes` na branch `main`**
2. O pipeline executa automaticamente:
    - `andes-cli` → gera `.spark`, `.made` e documentação
    - `spark-cli` → gera o projeto completo
    - `made-cli` → publica as issues no repositório
3. As alterações são commitadas de volta ao repositório.

---

## 📂 Estrutura do Repositório

```text
Capeta/
├── .github
   ├── workflows/                         # Automação via GitHub Actions  
      └── generate-artifacts.yml          # Pipeline que executa Andes, Spark e Made
├── artifacts/                            # Arquivos gerados pelo workflow
├── arquivo.andes                         # Ponto de partida do workflow
└── README.md
```

---

## 🚀 Execução Manual (Opcional)

Você pode executar manualmente os comandos das ferramentas com os exemplos descritos acima, se preferir não utilizar o pipeline automatizado.

---

## 📜 Licença

Este repositório é de uso educacional e foi desenvolvido como parte da disciplina Projeto de Sistemas.

---

## 👥 Agradecimentos

- Professor **Paulo Sérgio** pela condução da disciplina  
- Todos os times envolvidos no desenvolvimento das ferramentas  
- À integração colaborativa que tornou possível este workflow

---

## 💬 Contato

Abra uma *Issue* para dúvidas, sugestões ou melhorias!
