# PropagandaAI

## Table of contents

## Introduction

**Our goal:** A software application is that allows users to input specific themes or topics for a meme or propaganda poster. Following this input, the application should be capable of autonomously generating relevant imagery and accompanying text. Subsequently, it should seamlessly integrate these elements to produce a cohesive poster

## Setup
To setup the project, one needs to have alle the prerequisites installed. Then one needs to clone the repository, setup a virtual environment, and install the dependencies. This is described in more detail below.

### Prerequisites
Make sure you have Python installed on your machine. This project is developed using Python 3.9 or newer.
### Clone the repository
```bash
git clone https://github.com/SverreNystad/PropagandaAI.git
cd PropagandaAI
```

### Setup virtual environment
```bash
pip install virtualenv
```

For windows:
```bash
virtualenv venv
.\venv\Scripts\activate
```

For Linux / MacOS:
```bash
virtualenv venv
source venv/Scripts/activate
```

### Install dependencies
Once inside the virtual environment, you can install the required packages:
```bash
pip install -r requirements.txt
```

## Usage



## Repository structure
* **docs/:** Store all your documentation here. Architectural diagrams, architectural decisions reasoning, and API references.

* **src/:** Main source code directory.
  * **gpt/:** Code related to finetuning and utilizing the GPT model.
  * **image_generation/:** Code for generating images from prompts.
  * **assembler/:** Code that takes the generated text and image and assembles the picture.
* **tests/:** Unit tests, integration tests, and any other testing code.

* **models/:** If you have any pre-trained models or model checkpoints, they can be stored here.
