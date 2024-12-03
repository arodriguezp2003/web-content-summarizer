# Deep Dive into LLM Engineering: Web Content Summarizer

This repository is part of the **Deep Dive into LLM Engineering** series published on [alerodriguez.dev](https://alerodriguez.dev). The series shares my journey into the world of AI, focusing on building practical applications with Large Language Models (LLMs).

## About This Project

This project demonstrates how to create a web content summarizer using OpenAI's API. It takes a URL as input, extracts relevant content, and generates a concise summary using an LLM. While simple, this program lays the foundation for more advanced AI-powered tools.

## Features

- Extracts clean and relevant text from a webpage.
- Crafts effective prompts to guide the AI.
- Summarizes webpage content using OpenAI's GPT models.

## Installation

To run the project, ensure you have Python 3.8+ installed and follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/arodriguezp2003/web-content-summarizer.git
   cd web-content-summarizer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the program:
   ```bash
   python main.py
   ```

## Example Usage

Input a URL and get a concise summary. For example:

```bash
python main.py
```

Example output for [https://alerodriguez.dev](https://alerodriguez.dev):

> "Alejandro Rodriguez’s personal blog focuses on tech insights......."

## Part of a Larger Journey

This project is not just a standalone tool but a chapter in a broader narrative about exploring AI. If you’re curious about the process, challenges, and lessons behind this and other projects, check out the full story at [alerodriguez.dev](https://alerodriguez.dev).

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Stay Connected

For updates and new chapters in the **Deep Dive into LLM Engineering** series, visit [alerodriguez.dev](https://alerodriguez.dev). Let’s learn and build together! 🚀
