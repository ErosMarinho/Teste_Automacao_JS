# teste-Projeto-Automação Java Script
# js-validation-calculator-project

This project is a simple JavaScript application that includes scripts for validating Brazilian CPF numbers and email addresses using regular expressions, as well as basic arithmetic operations through a calculator module. The project is designed to run in a web environment and includes tests written with Jest to ensure the functionality of each component.

## Features

- **CPF Validation**: Validates Brazilian CPF numbers using regex.
- **Email Validation**: Validates email addresses using regex.
- **Calculator**: Performs basic arithmetic operations: addition, subtraction, multiplication, and division.
- **Testing**: Comprehensive tests for all functionalities using Jest.

## Project Structure

```
js-validation-calculator-project
├── src
│   ├── scripts
│   │   ├── validateCPF.js
│   │   ├── validateEmail.js
│   │   └── calculator.js
│   ├── index.js
│   └── utils
│       └── helpers.js
├── tests
│   ├── validateCPF.test.js
│   ├── validateEmail.test.js
│   └── calculator.test.js
├── package.json
├── jest.config.js
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd js-validation-calculator-project
   ```
3. Install the dependencies:
   ```
   npm install
   ```

## Usage

- To validate a CPF number:
  ```javascript
  import { validateCPF } from './src/scripts/validateCPF';
  console.log(validateCPF('123.456.789-09')); // true or false
  ```

- To validate an email address:
  ```javascript
  import { validateEmail } from './src/scripts/validateEmail';
  console.log(validateEmail('example@example.com')); // true or false
  ```

- To perform calculations:
  ```javascript
  import { add, subtract, multiply, divide } from './src/scripts/calculator';
  console.log(add(5, 3)); // 8
  ```

## Running Tests

To run the tests, use the following command:
```
npm test
```

This will execute all the tests defined in the `tests` directory using Jest.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.