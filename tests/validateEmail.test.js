import { validateEmail } from '../src/scripts/validateEmail';

describe('validateEmail', () => {
    test('valid email addresses', () => {
        expect(validateEmail('test@example.com')).toBe(true);
        expect(validateEmail('user.name+tag+sorting@example.com')).toBe(true);
        expect(validateEmail('user@example.co.in')).toBe(true);
    });

    test('invalid email addresses', () => {
        expect(validateEmail('plainaddress')).toBe(false);
        expect(validateEmail('@missingusername.com')).toBe(false);
        expect(validateEmail('username@.com')).toBe(false);
        expect(validateEmail('username@com.')).toBe(false);
        expect(validateEmail('username@.com.')).toBe(false);
    });
});