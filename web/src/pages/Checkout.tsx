import { Button, Card, Input } from '@shop/ui-kit';
import { PriceTag } from '../components/PriceTag';
import { money } from '../utils/format';

type Field = { name: string; label: string };

const FIELDS: Field[] = [
  { name: 'email', label: 'Email' },
  { name: 'street', label: 'Street' },
  { name: 'city', label: 'City' },
  { name: 'country', label: 'Country' },
  { name: 'card', label: 'Card number' },
];

export function Checkout({ total = '0' }: { total?: string }) {
  return (
    <Card>
      <form>
        {FIELDS.map((f) => <label key={f.name}>{f.label}<Input /></label>)}
        <PriceTag value={total} />
        <p>{money(total)} will be charged now.</p>
        <Button>Pay</Button>
      </form>
    </Card>
  );
}
