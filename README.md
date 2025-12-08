# 🕵️ Fact Checker Agent

> *A no-nonsense AI assistant that verifies your claims and keeps a log of the myths you believed.*

This is a small, practical project built to explore the capabilities of [Google's Agent Development Kit](https://github.com/google/agent-development-kit) (ADK) and the Gemini 2.5 Flash model. I just thought this was an interesting framework and wanted to try it out.

### 🚀 What It Does?

This agent acts as your personal fact-checking assistant. It follows a strict `"Verify Claim → Confirm → Archive"` workflow:

### 🗂️ Technical Workflow
- The `FactCheckerAgent` is a sequential agent that has access to two sub-agents: the `ResearcherAgent` and the `SecretaryAgent`.
- The `ResearcherAgent` is tasked with gathering the claim or fact from the user, then using the built-in `google_search` tool to verify the claim from a credible source.
- The `SecretaryAgent` takes the output from the `ResearcherAgent` and saves the correct fact if the user got it wrong to a file using a custom tool `add_facts_to_notes`.

<img alt="image" src="https://github.com/user-attachments/assets/49950b85-7a7f-4ea0-9790-7b3469b574ef" />

### ⚙️ Installation

If you want to check it out on your own, it's pretty straightforward:
- Clone this repository
- Create a new Python virtual environment
- Run `pip install -r requirements.txt`
- Finally, in the root directory, run `adk web`
- ADK's web interface should pop up in localhost, where you can chat as you usually would

