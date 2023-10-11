# Random Boolean network
A random Boolean network is a mathematical model used to study the dynamics of complex systems, particularly in fields such as biology and physics. It consists of a collection of binary variables (nodes) time steps based on predefined rule that is called boolean function.

The update of the states is done by synchronous update. In synchronous update, all the nodes are updated synchronously (simultaneously) so the result state is always same. When nodes are updated, the state of each node is determined by the states of its neighboring nodes, which are typically defined by a fixed connectivity structure called boolean function.

In this project, we use RBNs to simulate and analyze the dynamic behaviors, such as 2 point attractor networks (symbolizing 1 cell) showing relationship of barrier to noise and basin difference.

- Task1: Generate 100 random Boolean networks of 2 point attractor network and plot the barrier to noise and basin difference of each network. In 2 point attractor network, we can see how the basin difference affect noise barrier.
- Task2: Generate the noise trajectory of one random Boolean network and measure the degree distribution that shows relationship between number of links (k) and the number of states that correspond to that number of links. We can figure out how internal network of the cell influence the mRNA level of the cell when the genetically identical cells' networks (2-state switch) are subjected to the noise. 
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Contact Information](#contact-information)

## Installation

The code requires Python 3.7.
- Install openpyxl (pip install openpyxl)
- Install pandas

System requirements
- macOS 11

Step-by-step installation instructions.
How to download or clone the project's repository.
How to install dependencies (e.g., using package managers like npm, pip, or composer).
Configuration files that need to be edited, if any.
Any environment variables that need to be set.

## Usage

Explain how to use your project. Provide examples or code snippets to illustrate its functionality. Include any relevant command-line options, configuration settings, or usage patterns. If your project has a user interface, describe its various components and how to interact with them.

## Configuration

If your project requires configuration, explain how to set it up. Specify the configuration files or variables users need to modify and explain their purpose. Provide default values or examples to guide users in configuring your project.

## Features

List and describe the main features and functionalities of your project. This section helps users understand what your project can do and its unique selling points.

## Contributing

If you welcome contributions from others, provide guidelines on how they can contribute to your project. Explain the process for submitting bug reports, feature requests, or pull requests. Specify any coding standards, style guides, or guidelines for branch management.

## License

Specify the license under which your project is released. Include the full text of the license or a link to its location in your repository.

## Credits

Acknowledge and attribute any external resources, libraries, or contributors that have influenced or supported your project. Provide links to their websites or repositories.

## Contact Information

Provide your contact details or a link to your preferred communication channel so that users or potential collaborators can reach out to you with questions, feedback, or inquiries.