import { add, subtract, multiply, divide } from '../src/scripts/calculator.js';

describe('Calculator Functions', () => {
    test('adds two numbers', () => {
        expect(add(2, 3)).toBe(5);
    });

    test('subtracts two numbers', () => {
        expect(subtract(5, 3)).toBe(2);
    });

    test('multiplies two numbers', () => {
        expect(multiply(2, 3)).toBe(6);
    });

    test('divides two numbers', () => {
        expect(divide(6, 3)).toBe(2);
    });

    test('divides by zero should throw an error', () => {
        expect(() => divide(10, 0)).toThrow("Cannot divide by zero");
    });
});