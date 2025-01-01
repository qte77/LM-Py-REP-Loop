# LLM-REPL Pipeline

An API for generating, evaluating, and refactoring Python code using Large Language Models (LLMs) and a Python REPL.

![Version](https://img.shields.io/badge/version-0.0.0-8A2BE2)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/LM-Py-REP-Loop/badge)](https://www.codefactor.io/repository/github/qte77/LM-Py-REP-Loop)
[![CodeQL](https://github.com/qte77/LM-Py-REP-Loop/actions/workflows/codeql.yaml/badge.svg)](https://github.com/qte77/LM-Py-REP-Loop/actions/workflows/codeql.yaml)
[![ruff](https://github.com/qte77/LM-Py-REP-Loop/actions/workflows/ruff.yaml/badge.svg)](https://github.com/qte77/LM-Py-REP-Loop/actions/workflows/ruff.yaml)
[![pytest](https://github.com/pdq21/SF-quant-temp/actions/workflows/pytest.yaml/badge.svg)](https://github.com/pdq21/SF-quant-temp/actions/workflows/pytest.yaml)
[![Link Checker](https://github.com/qte77/LM-Py-REP-Loop/actions/workflows/links-fail-fast.yaml/badge.svg)](https://github.com/qte77/LM-Py-REP-Loop/actions/workflows/links-fail-fast.yaml)
[![Deploy Docs](https://github.com/qte77/LM-Py-REP-Loop/actions/workflows/generate-deploy-mkdocs-ghpages.yaml/badge.svg)](https://github.com/qte77/LM-Py-REP-Loop/actions/workflows/generate-deploy-mkdocs-ghpages.yaml)
[![vscode.dev](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=vscode.dev&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://vscode.dev/github/qte77/LM-Py-REP-Loop)

## Status

(DRAFT) (WIP) ----> Not fully implemented yet

For version history have a look at the [CHANGELOG](CHANGELOG.md).

## TOC

- [LLM-REPL Pipeline](#)

## Overview

The LLM-REPL Pipeline is a system designed to automate the process of code generation, evaluation, and refactoring using Large Language Models (LLMs) and a Python REPL.
This pipeline aims to enhance developer productivity by providing real-time feedback and iterative code improvement.

**Goals:**

- Automate code generation from user prompts or requests.
- Provide immediate feedback on code correctness and efficiency.
- Enable iterative code refinement through a feedback loop.
- Ensure code quality through continuous testing and refactoring.

[↑](#toc)

## Key Features

- **Code Generation:** Use LLMs to generate Python code based on user prompts.
- **Code Execution:** Execute generated code in a Python REPL to capture output and errors.
- **Code Evaluation:** Evaluate code for correctness, efficiency, and adherence to best practices.
- **Code Refactoring:** Refactor code based on feedback from the evaluation step.
- **Feedback Loop:** Implement a loop where code is generated, evaluated, and refactored until it meets predefined criteria.
- **Version Control:** Integrate with Git for tracking code changes.
- **CI/CD Pipeline:** Automate testing and deployment of code iterations.
- **Security and Compliance:** Ensure generated code adheres to security standards and compliance requirements.

[↑](#toc)

## User Stories

- **As a developer**, I want to input a prompt or request, so that the system can generate code that meets my requirements.
- **As a developer**, I want the system to execute the generated code and provide feedback, so I can understand if the code works as expected.
- **As a developer**, I want the system to refactor the code based on feedback, so I can improve the code quality iteratively.
- **As a developer**, I want to see the history of code changes, so I can track the evolution of the solution.

[↑](#toc)

## Technical Requirements

- **LLM Integration:** Use models like Qwen/Qwen2.5-Coder-32B-Instruct, DeepSeek-Coder-V2-Instruct, etc., from Hugging Face or Ollama.
- **Python REPL:** Use LangChain Python REPL tool or a custom REPL like "pai".
- **CI/CD Pipeline:** Implement using tools like Jenkins, GitLab CI, or GitHub Actions.
- **Security:** Integrate security scanning tools within the CI/CD pipeline.
- **Documentation:** Use arc42 for structuring architectural decisions.

[↑](#toc)

## Non-Functional Requirements

- **Performance:** The system should respond within 5 seconds for code generation and evaluation.

[↑](#toc)

## Assumptions

- Users have basic knowledge of Python programming.
- The LLMs used are capable of generating Python code with high accuracy.

[↑](#toc)

## Constraints

- The system must run on a local machine or within a containerized environment.
- The LLMs must be accessible either through an API or locally.

[↑](#toc)

## Future Enhancements

- Explore techniques like conversational feedback loops to enhance the quality and speed of code generation.
- **Scalability:** The pipeline should be able to handle multiple concurrent users.
- **Reliability:** The system should have a 99.9% uptime.

[↑](#toc)

## Documentation

- **Project DSL**: See `[docs/project_dsl.txt](docs/project_dsl.txt)` for a high-level overview of the project structure and functionality.
- **PRD**: See `[docs/PRD.md](docs/PRD.md)` for detailed product requirements.
- **OpenAPI specification**: `docs/openapi.yaml`
  - Outlines the endpoints for code generation, evaluation, and refactoring, along with the expected request and response structures.
  - It can be processed with Swagger Codegen to generate client libraries or server stubs for various programming languages.

[↑](#toc)

### Architecture

<img src="assets/images/c4-arch.dark.png#gh-dark-mode-only" alt="C4-Arch" title="C4-Arch" width="60%" />
<img src="assets/images/c4-arch.light.png#gh-light-mode-only" alt="C4-Arch" title="C4-Arch" width="60%" />

[↑](#toc)

## Project Structure

```sh
/
├─ app/
│  ├─ __init__.py
│  ├─ __main__.py
│  └─ __version__.py
├─ tests/
├─ docs/
│  ├─ project_dsl.txt
│  ├─ PRD.md
│  └─ architecture/
│     └─ c4_diagram.md
├─ Dockerfile
├─ README.md
└─ pyproject.toml
```

[↑](#toc)

<!--
## TODO

[↑](#toc)
-->

[↑](#toc)

## Usage

```sh
git clone https://github.com/your-username/llm-repl-pipeline.git
cd llm-repl-pipeline
uv install
```

2. **Run the application:**

`uvicorn src.main:app --reload`

2. **Access the API documentation:**

- Open your browser and navigate to `http://localhost:8000/docs` to view the Swagger UI for the API.

### swagger-client

An API for generating, evaluating, and refactoring Python code using Large Language Models (LLMs) and a Python REPL.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

[↑](#toc)

## Further reading

- [Python REPL](https://python.langchain.com/docs/integrations/tools/python/)
- [The Python Standard REPL: Try Out Code and Ideas Quickly](https://realpython.com/python-repl/)
- [Using a Feedback Loop for LLM-based Infrastructure as Code Generation](https://zeet.co/blog/cicd-pipeline-best-practices)
- [LLM-Repl](https://github.com/Phat3/LLM-Repl?tab=readme-ov-file)
- [Building LLMs for Code Repair](https://blog.replit.com/code-repair)
- [IntelliExplain: Enhancing Conversational Code Generation for Non-Professional Programmers](https://arxiv.org/abs/2405.10250)
- [IMPROVE CODE GENERATION WITH FEEDBACK](https://openreview.net/pdf/45b1c77b752c593af18289d98a16a1b1ed1ed0bc.pdf)
- [Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models | 2310](https://arxiv.org/abs/2310.04406)
- [Code for paper "LEVER: Learning to Verifiy Language-to-Code Generation with Execution" (ICML'23)](https://github.com/niansong1996/lever)
- [LEVER: Learning to Verify Language-to-Code Generation with Execution](https://arxiv.org/abs/2302.08468)

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE.md) file for details. Third-party licenses might also apply.

[↑](#toc)

