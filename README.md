# MarketingAI
<div align="center">

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/CogitoNTNU/MarketingAI/main.yml)
![GitHub top language](https://img.shields.io/github/languages/top/CogitoNTNU/MarketingAI)
![GitHub language count](https://img.shields.io/github/languages/count/CogitoNTNU/MarketingAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Version](https://img.shields.io/badge/version-1.0.0-blue)](https://img.shields.io/badge/version-1.0.0-blue)

<img src="docs/img/MarketingAILogo.png" width="50%" alt="Cogito Image" style="display: block; margin-left: auto; margin-right: auto;">

</div>

## Table of contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Tests](#tests)
5. [Repository Structure](#repository-structure)
6. [Contributors](#contributors)


## Introduction
MarketingAI is a sophisticated software application designed to empower users in creating impactful marketing materials. MarketingAI caters to marketers, content creators, and anyone looking for an automated, creative solution for their advertising needs.

**Our goal:** A software application is that allows users to input specific themes or topics for a meme or Marketing poster. Following this input, the application should be capable of autonomously generating relevant imagery and accompanying text. Subsequently, it should seamlessly integrate these elements to produce a cohesive poster

## Setup
To setup the project, one needs to have all the prerequisites installed. Then one needs to clone the repository, setup a virtual environment, and install the dependencies. This is described in more detail below.

### Prerequisites
- Ensure Python 3.9 or newer is installed on your machine. [Download Python](https://www.python.org/downloads/)
- Familiarity with basic Python package management and virtual environments is beneficial.

### Clone the repository
```bash
git clone https://github.com/CogitoNTNU/MarketingAI.git
cd MarketingAI
```

### Virtual Environment (Recommended)

<details> 
<summary><strong>🚀 A better way to set up repositories </strong></summary>

A virtual environment in Python is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. Using a virtual environment for your project ensures that the project's dependencies are isolated from the system-wide Python and other Python projects. This is especially useful when working on multiple projects with differing dependencies, as it prevents potential conflicts between packages and allows for easy management of requirements.

1. **To set up and use a virtual environment for MarketingAI:**
    First, install the virtualenv package using pip. This tool helps create isolated Python environments.
    ```bash
    pip install virtualenv
    ```

2. **Create virtual environment**
    Next, create a new virtual environment in the project directory. This environment is a directory containing a complete Python environment (interpreter and other necessary files).
    ```bash
    python -m venv venv
    ```

4. **Activate virtual environment**
    To activate the environment, run the following command:
    * For windows:
        ```bash
        ./venv/Scripts/activate
        ```

    * For Linux / MacOS:
        ```bash
        source venv/bin/activate
        ```


### Settup VSCode with virtual environment (Optional for VSCode users)
With VSCode opened press ```Ctrl+Shift+P``` and search for ```python: Select Interpreter``` and click on it

Then select the relevant virtual environment as shown

![Vscode setup](/docs/img/vscodeSettup.png)

Now you can utilize all the installed goodies from the environment ;)
</details>

### Install dependencies
With the virtual environment activated, install the project dependencies:
```bash
pip install -r requirements.txt
```
The requirements.txt file contains a list of packages necessary to run MarketingAI. Installing them in an activated virtual environment ensures they are available to the project without affecting other Python projects or system settings.

### Create a .env file
For secure and efficient management of environment-specific variables, MarketingAI utilizes a `.env` file. This file is used to store sensitive information, such as API keys, which should not be hard-coded into the source code or shared publicly. The `.env` file is particularly crucial for maintaining the confidentiality of your API keys and other sensitive data.

**Important:** The `.env` file should never be committed to version control (e.g., GitHub). Always include `.env` in your `.gitignore` file to prevent accidental upload of sensitive information.

#### Steps to Create and Configure the .env File:

1. **Create the .env File:**
   In the root directory of the project, create a new file named `.env`. This file will be used to store environment variables.
   ```bash
    touch .env
    ```

2. **Add Environment Variables:**
    ```bash
    echo "API_KEY=YOUR_API_KEY" > .env # Remember to change YOUR_API_KEY to your actual API key
    ```

3. **Obtaining an API Key:**
    If you don't have an API key from OpenAI, you can obtain one by visiting [OpenAI API Keys](https://platform.openai.com/api-keys). Follow their instructions to generate a new API key.

    By following these steps, you'll ensure that your application has all the necessary environment-specific configurations, while keeping sensitive data secure and out of version control.

## Usage
To run MarketingAI, navigate to the project's root directory in your command line interface and execute the following command:
```bash
python main.py
```

## Tests
To run the full test suit, run the following command:
```bash
pytest
```

To run all tests except api tests, run the following command:
```bash
pytest -m "not apitest"
```

## Repository structure
* **docs/:** Store all your documentation here. Architectural diagrams, architectural decisions reasoning, and API references.

* **src/:** Main source code directory.
  * **assembler/:** Code that takes the generated text and image and assembles the picture.
  * **fine_tuning/:** Code for fine-tuning the GPT model, and data used for it.
  * **function_calling/:** All code for letting agents call the functions and agent chains.
  * **gpt/:** Code related to chat Completion.
  * **image_generation/:** Code for generating images from prompts.
* **tests/:** Unit tests, integration tests, and any other testing code.
* **images/:** All images created by the program both raw images and the assembled images.

## Contributors
<table>
  <tr>
    <td align="center">
        <a href="https://github.com/Spiderpig02">
            <img src="https://github.com/Spiderpig02.png?size=100" width="100px;" alt="Daniel Neukirch Hansen"/><br />
            <sub><b>Daniel Neukirch Hansen</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Eduard-Prokhorikhin">
            <img src="https://github.com/Eduard-Prokhorikhin.png?size=100" width="100px;" alt="Eduard Prokhorikhin"/><br />
            <sub><b>Eduard Prokhorikhin</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/HFossdal">
            <img src="https://github.com/HFossdal.png?size=100" width="100px;" alt="Håvard Fossdal"/><br />
            <sub><b>Håvard Fossdal</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/JHJORE">
            <img src="https://github.com/JHJORE.png?size=100" width="100px;" alt="Jørgen Haugdal Jore"/><br />
            <sub><b>Jørgen Haugdal Jore</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Knolaisen">
            <img src="https://github.com/Knolaisen.png?size=100" width="100px;" alt="Kristoffer Nohr Olaisen"/><br />
            <sub><b>Kristoffer Nohr Olaisen</b></sub>
        </a>
    </td>
    <!-- More contributors... -->
    <td align="center">
        <a href="https://github.com/olavsl">
            <img src="https://github.com/olavsl.png?size=100" width="100px;" alt="Olav Selnes Lorentzen"/><br />
            <sub><b>Olav Selnes Lorentzen</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/svemyh">
            <img src="https://github.com/svemyh.png?size=100" width="100px;" alt="Sveinung Myhre"/><br />
            <sub><b>Sveinung Myhre</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/SverreNystad">
            <img src="https://github.com/SverreNystad.png?size=100" width="100px;"/><br />
            <sub><b>Sverre Nystad</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/sandviklee">
            <img src="https://github.com/sandviklee.png?size=100" width="100px;" alt="Simon Sandvik Lee"/><br />
            <sub><b>Simon Sandvik Lee</b></sub>
        </a>
    </td>
  
  </tr>
</table>

This project could not have been possible without all of the wonderful contributors. Thank you all for your hard work!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Get Involved!
### 🌟 Try MarketingAI Today!
Dive into a new era of marketing creativity! Download MarketingAI now and start crafting compelling marketing materials with ease.

### 💡 Feedback & Suggestions
Your thoughts and experiences are invaluable to us. If you have any feedback or suggestions, please open an issue or a discussion. We're excited to hear your ideas on how we can improve MarketingAI!

### 🤝 Contribute to MarketingAI
Join our vibrant community of contributors! Whether you're fixing bugs, adding features, or improving documentation, your contributions are warmly welcomed. Check out our Contributing Guidelines for more information on how to get started.

### 🔔 Stay Updated
Follow us on GitHub to stay updated with the latest releases, features, and updates. Star us to show your support and keep track of our progress!

### 📢 Spread the Word
Love MarketingAI? Share your experiences on social media and with your network. Your support helps us grow and improve!

Thank you for exploring MarketingAI - where creativity meets automation in marketing!
