# PropagandaAI

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/CogitoNTNU/PropagandaAI/main.yml)
![GitHub top language](https://img.shields.io/github/languages/top/CogitoNTNU/PropagandaAI)
![GitHub language count](https://img.shields.io/github/languages/count/CogitoNTNU/PropagandaAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of contents
1. [Introduction](#Introduction)
2. [Setup](#Setup)
3. [Usage](#Usage)
4. [Tests](#Tests)
5. [Repository structure](#Repository-structure)


## Introduction

**Our goal:** A software application is that allows users to input specific themes or topics for a meme or propaganda poster. Following this input, the application should be capable of autonomously generating relevant imagery and accompanying text. Subsequently, it should seamlessly integrate these elements to produce a cohesive poster

## Setup
To setup the project, one needs to have alle the prerequisites installed. Then one needs to clone the repository, setup a virtual environment, and install the dependencies. This is described in more detail below.

### Prerequisites
Make sure you have Python installed on your machine. This project is developed using Python 3.9 or newer.
### Clone the repository
```bash
git clone https://github.com/CogitoNTNU/PropagandaAI.git
cd PropagandaAI
```

### Setup virtual environment
```bash
pip install virtualenv
```

For windows:
```bash
virtualenv venv
source .\venv\Scripts\activate
```

For Linux / MacOS:
```bash
virtualenv venv
source venv/bin/activate
```

### Install dependencies
Once inside the virtual environment, you can install the required packages:
```bash
pip install -r requirements.txt
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
