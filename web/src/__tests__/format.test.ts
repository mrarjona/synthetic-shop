import { money } from '../utils/format';

test('money', () => expect(money('1')).toBe('1.00 €'));
