// Entry point for the JavaScript validation and calculator project
import { validateCPF } from './scripts/validateCPF.js';
import { validateEmail } from './scripts/validateEmail.js';
import { add, subtract, multiply, divide } from './scripts/calculator.js';

// Example usage
const cpf = '123.456.789-09';
const email = 'example@example.com';

console.log(`Is the CPF valid? ${validateCPF(cpf)}`);
console.log(`Is the email valid? ${validateEmail(email)}`);

const num1 = 10;
const num2 = 5;

console.log(`Addition: ${add(num1, num2)}`);
console.log(`Subtraction: ${subtract(num1, num2)}`);
console.log(`Multiplication: ${multiply(num1, num2)}`);
console.log(`Division: ${divide(num1, num2)}`);