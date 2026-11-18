import { money } from '../utils/format';

export function PriceTag({ value }: { value: string }) { return <span>{money(value)}</span>; }
