﻿[MAINTENANCE_BADGE]: https://img.shields.io/badge/Maintained%3F-yes-green.svg
[PYTHON_BADGE]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[LICENSE_BADGE]: https://img.shields.io/pypi/l/ansicolortags.svg


<h1 align="center"> AI Chat PDF Assistant LOBITO</h1>

![PYTHON][PYTHON_BADGE]
![LICENSE][LICENSE_BADGE]


`Content:`
<ul>
  <li><a href="#about">About</a></li>
  <li><a href="#features">Project Features</a></li>
  <li><a href="#gettingStarted">Getting Started</a></li>
    <ul>
      <li><a href="#technologiesUsed">Technologies Used</a></li>
      <li><a href="#preRequisites">Prerequisites</a></li>
    </ul>
  <li><a href="#howToRun">How To Run</a></li>
  <li><a href="#results">Results</a></li>
  <li><a href="#projectVideo">Project Video</a></li>
  <li><a href="#collaborators">Collaborators</a></li>
</ul>

LOBITO is a virtual assistant designed to help customers of a banking app understand the contracts for the services offered by the bank. Using Langchain and Python, LOBITO provides quick and interactive access to information contained in PDF contracts, as if customers were listening to an expert.


<p align="center">
    <img src="./assets/images/" alt="Image Example" width="400px">
</p>

<h2 id="about">📌 About</h2>
The goal of LOBITO is to facilitate the understanding of banking contracts for customers, making the information more accessible and comprehensible. For example, for a 90-day term deposit service, customers can interact with the chat to clarify doubts about the contract, without the need to read the entire document.

<h2 id="features">✔ Project Features</h2>

- <strong>Simple and Fast Interaction:</strong> Intuitive chat interface for customer interaction.
- <strong>Access to PDF Contracts:</strong> Ability to extract and present information from banking contract PDFs.
- <strong>Specialized Responses:</strong> Detailed and accurate responses, as if provided by an expert.
- <strong>Keyword Search:</strong> Allows keyword searches within documents for quick and specific answers.


  - <strong>Example questions:</strong>

        "What this document talk about?"
        "What i?"

- <strong>Immediate Responses:</strong> Using AI, the application provides immediate answers based on questions asked by users.

<h2 id="gettingStarted">🚀 Getting Started</h2>

This section describes how to run the project locally.


<h3 id="technologiesUsed">Technologies Used</h3>

- <strong>Langchain:</strong> Library for building language chains and natural language processing.
- <strong>Streamlit:</strong> Framework used to build the interactive web interface in a simple and fast way.
- <strong>Python:</strong>Main language of the project, used to integrate Langchain and Streamlit and to manipulate CSV data.

<h3 id="preRequisites">Prerequisites</h3>

Ensure you have the following prerequisites installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Streamlit](https://docs.streamlit.io/)
- [Langchain](https://python.langchain.com/v0.2/docs/introduction/)
- OpenAI API Key

<h2 id="howToRun">How to Run</h2>

- Clone the project repository from GitHub:

```bash
git clone https://github.com/EriveltoSilva/ai-chat-pdf-assistent-LOBITO.git
```

Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.\.venv\Scripts\activate  # For Windows
```


- Navigate to the project directory and install the required dependencies. 
```bash
pip install -r requirements.txt
```

- Then start the Streamlit app:

```bash
streamlit run main.py
```

- Access the user interface in your browser:

```text
http://localhost:8501
```

- Upload the contract PDF and interact with the virtual assistant to get the necessary information.

<h2 id="results">🤝 Results</h2>

<p align="center">
    <img src="./assets/images/rh-assistant1.PNG" alt="Image Example" />
</p>


<h2 id="projectVideo">▶ Project Video</h2>

<a href="#">
See a short video of how project works on my LinkedIn
</a>

<h2 id="collaborators">🤝 Collaborators</h2>

Special thanks to the project contributor:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/125351173?v=4" width="100px;" alt="Fernanda Kipper Profile Picture"/><br>
        <sub>
          <b>Erivelto Silva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2 id="contribute">📫 Contribute</h2>

To contribute to this project, follow these steps:

1. `git clone https://github.com/EriveltoSilva/ai-chat-pdf-assistent-LOBITO.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made. If applicable, include screenshots of visual modifications and wait for the review!

<h2 id="contribute">📫 License</h2>

This project is licensed under the MIT License. See the <a href="./LICENSE.txt">LICENSE file</a> for more information.