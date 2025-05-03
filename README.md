# AI-Assisted Test Case Generator

This project leverages the power of AutoGen and OpenAI models to automatically generate comprehensive test cases for software applications.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

The AI-Assisted Test Case Generator is a tool designed to help software development teams create high-quality test cases with minimal effort. By combining AutoGen's agent-based framework with OpenAI's language models, this tool can analyze code, understand functionality, and generate appropriate test cases across multiple testing levels.

## Features

- **Automatic Test Case Generation**: Generate unit, integration, and end-to-end test cases from source code
- **Intelligent Code Analysis**: Analyzes code structure, dependencies, and edge cases
- **Multiple Testing Frameworks Support**: Generates test cases for popular frameworks like pytest, Jest, JUnit, etc.
- **Natural Language Interface**: Describe functionality in plain English and get corresponding test cases
- **Customizable Templates**: Adjust testing patterns to match your team's standards
- **Continuous Integration Ready**: Easily integrates with CI/CD pipelines

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-test-case-generator.git
cd ai-test-case-generator

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Setup

1. **API Keys**: Create a `.env` file in the project root with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

2. **Configure AutoGen**: Set up necessary configurations for AutoGen agents in `config.json`:

```json
{
  "agents": {
    "code_analyzer": {
      "model": "gpt-4",
      "temperature": 0.2
    },
    "test_generator": {
      "model": "gpt-4",
      "temperature": 0.7
    }
  }
}
```

## Usage

### Basic Usage

```python
from ai_test_generator import TestGenerator

# Initialize the generator
generator = TestGenerator()

# Generate tests from a single file
tests = generator.generate_from_file("path/to/your/file.py")

# Save generated tests
generator.save_tests(tests, "path/to/output/test_file.py")
```

### Command Line Interface

```bash
# Generate tests for a file
python -m ai_test_generator generate --file path/to/your/file.py --output path/to/output/test_file.py

# Generate tests for a directory
python -m ai_test_generator generate --directory path/to/your/project --output path/to/output/directory

# Generate tests with specific framework
python -m ai_test_generator generate --file path/to/your/file.py --framework pytest --output path/to/output/test_file.py
```

## Configuration

The tool can be configured through a `config.json` file:

```json
{
  "openai": {
    "model": "gpt-4",
    "temperature": 0.5,
    "max_tokens": 4000
  },
  "autogen": {
    "agents": ["code_analyzer", "test_generator", "test_validator"],
    "max_iterations": 3
  },
  "testing": {
    "default_framework": "pytest",
    "coverage_threshold": 80,
    "generate_fixtures": true,
    "include_docstrings": true
  }
}
```


### Generating Tests from Natural Language

```bash
python -m ai_test_generator generate-from-description --description "A user authentication system that validates email and password, with password requirements of at least 8 characters, one uppercase letter, one number, and one special character."
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Architecture

The AI-Assisted Test Case Generator uses a multi-agent system powered by AutoGen:

1. **Code Analyzer Agent**: Parses and analyzes source code to understand functionality
2. **Test Generator Agent**: Creates test cases based on code analysis
3. **Test Validator Agent**: Validates generated tests for correctness and coverage

The system uses OpenAI models to power these agents, allowing them to understand code semantics and generate appropriate test cases.

```
Source Code → Code Analyzer → Test Generator → Test Validator → Final Test Cases
```

## Dependencies

- Python 3.8+
- AutoGen 0.2.0+
- OpenAI API
- pytest (for running the generator's own tests)
- Various language-specific testing frameworks (depending on your project)

## FAQ

**Q: How does the system handle complex dependencies?**
A: The Code Analyzer Agent identifies dependencies and creates appropriate mocks or fixtures to isolate the component being tested.

**Q: Can I use this with my existing test suite?**
A: Yes, the tool can analyze existing tests and generate complementary tests to improve coverage.

**Q: Which programming languages are supported?**
A: Currently, the tool supports Python, JavaScript, Java, and C#. Support for additional languages is planned for future releases.
