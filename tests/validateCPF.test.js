import { validateCPF } from '../src/scripts/validateCPF.js';

describe('validateCPF', () => {
    test('valid CPF with formatting', () => {
        expect(validateCPF('123.456.789-09')).toBe(true);
    });

    test('invalid CPF with incorrect digits', () => {
        expect(validateCPF('123.456.789-00')).toBe(false);
    });

    test('valid CPF without formatting', () => {
        expect(validateCPF('12345678909')).toBe(true);
    });

    test('invalid CPF with less than 11 digits', () => {
        expect(validateCPF('12345678')).toBe(false);
    });

    test('invalid CPF with more than 11 digits', () => {
        expect(validateCPF('12345678909123')).toBe(false);
    });

    test('invalid CPF with all repeated digits', () => {
        expect(validateCPF('111.111.111-11')).toBe(false);
    });
});