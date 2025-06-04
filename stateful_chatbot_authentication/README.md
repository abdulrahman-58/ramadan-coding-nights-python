# 🧠 Stateful Chatbot with GitHub Authentication

A **stateful question-answering chatbot** built using **Python**, **Chainlit**, and **UV**, featuring **GitHub OAuth authentication** and integration with **Google Gemini**. The chatbot remembers previous user messages to provide context-aware responses.

---

## 🚀 Features

* 🔐 GitHub OAuth login
* 🧠 Stateful chat (memory of previous interactions)
* 🤖 Powered by Google Gemini LLM
* ⚙️ Built with UV and Chainlit
* 🌐 Interactive web-based UI

---

## 📦 Getting Started

Follow these steps to install, configure, and run the chatbot locally.

---

### 1️⃣ Install UV

#### On macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### On Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Verify Installation:

```bash
uv --version
```

---

### 2️⃣ Initialize a New Project

```bash
uv init stateful_chatbot_authentication
cd stateful_chatbot_authentication
```

---

### 3️⃣ Install Dependencies

```bash
uv add chainlit google-generativeai python-dotenv
```

---

### 4️⃣ Activate the Virtual Environment

#### On Windows:

```bash
.venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source .venv/bin/activate
```

---

### 5️⃣ Verify Chainlit Installation

Test with the built-in hello app:

```bash
chainlit hello
```

Visit in your browser:

```
http://localhost:8000
```

You should see:

> "Your name is: \[Your Name]"
> ✅ Chainlit installation is working!

---

### 6️⃣ Create `.env` File

Create a `.env` file in your project root and add the following:

```env
GEMINI_API_KEY=your_gemini_api_key
OAUTH_GITHUB_CLIENT_ID=your_github_client_id
OAUTH_GITHUB_CLIENT_SECRET=your_github_client_secret
CHAINLIT_AUTH_SECRET=your_chainlit_auth_secret
```

#### 🔑 Get the credentials:

* [Google Gemini API Key](https://aistudio.google.com/app/apikey)
* [GitHub OAuth App Credentials](https://github.com/settings/developers)
* Generate Chainlit auth secret:

```bash
chainlit create-secret
```

Paste the generated secret into your `.env` file.

---

### 7️⃣ Create `chainlit.yaml` Configuration File

Create a file named `chainlit.yaml` in the root of your project. Configure it based on your app’s needs (authentication, UI options, project name, etc.).

---

### 8️⃣ Run the Authenticated Chatbot

Launch your chatbot with:

```bash
chainlit run main.py -w
```

Visit:

```
http://localhost:8000
```

✅ Log in using GitHub → ask questions → enjoy a memory-enabled, intelligent chatbot experience!

---

## 🎉 That’s It!
