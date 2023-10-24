# MarketingAI
<div align="center">

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/CogitoNTNU/MarketingAI/main.yml)
![GitHub top language](https://img.shields.io/github/languages/top/CogitoNTNU/MarketingAI)
![GitHub language count](https://img.shields.io/github/languages/count/CogitoNTNU/MarketingAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Version](https://img.shields.io/badge/version-1.0.0-blue)](https://img.shields.io/badge/version-1.0.0-blue)

<img src="https://www.cogito-ntnu.no/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FCogitoBrain1.b7615fb0.webp&w=1920&q=75" width="50%" alt="Cogito Image" style="display: block; margin-left: auto; margin-right: auto;">

</div>

## Table of contents
1. [Introduction](#Introduction)
2. [Setup](#Setup)
3. [Usage](#Usage)
4. [Tests](#Tests)
5. [Repository structure](#Repository-structure)


## Introduction
<div align="center">

![HelloMarketingAI](data/assembled_images/HelloMarketingAI.png)

</div>

**Our goal:** A software application is that allows users to input specific themes or topics for a meme or Marketing poster. Following this input, the application should be capable of autonomously generating relevant imagery and accompanying text. Subsequently, it should seamlessly integrate these elements to produce a cohesive poster

## Setup
To setup the project, one needs to have alle the prerequisites installed. Then one needs to clone the repository, setup a virtual environment, and install the dependencies. This is described in more detail below.

### Prerequisites
Make sure you have Python installed on your machine. This project is developed using Python 3.9 or newer.
### Clone the repository
```bash
git clone https://github.com/CogitoNTNU/MarketingAI.git
cd MarketingAI
```

### Setup virtual environment
```bash
pip install virtualenv
```

### Create virtual environment
```bash
python -m venv venv
```

For windows:
```bash
source ./venv/Scripts/activate
```

For Linux / MacOS:
```bash
source venv/bin/activate
```

### Install dependencies
Once inside the virtual environment, you can install the required packages:
```bash
pip install -r requirements.txt
```

### Settup VSCode with virtual environment
With VSCode opened press ```Ctrl+Shift+P``` and search for ```python: Select Interpreter``` and click on it

Then select the relevant virtual environment as shown

![img](/docs/img/vscodeSettup.png)

Now you can utilize all the installed goodies form the environment ;)

### Create a .env file
Create a file called `.env` in the root of the project. This file should contain the following:
* API_KEY: The API key for the OpenAI API.

NOTE: Never Commit .env to Version Control. The .env file should be kept private and never be committed to public repositories as it contains secretes like API keys.
  
```bash
touch .env
echo "API_KEY=YOUR_API_KEY" > .env # Remember to change YOUR_API_KEY to your actual API key
```



## Usage



## Tests
To run the full test suit, run the following command:
```bash
pytest
```

## Repository structure
* **docs/:** Store all your documentation here. Architectural diagrams, architectural decisions reasoning, and API references.

* **src/:** Main source code directory.
  * **gpt/:** Code related to finetuning and utilizing the GPT model.
  * **image_generation/:** Code for generating images from prompts.
  * **assembler/:** Code that takes the generated text and image and assembles the picture.
* **tests/:** Unit tests, integration tests, and any other testing code.

* **models/:** If you have any pre-trained models or model checkpoints, they can be stored here.
* **data/:** All training data, test data, and any other data used in the project should be stored here. This does not include configuration files.


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
