import { Card, Spinner, Timeline } from '@shop/ui-kit';
import { fetchRefunds } from '../api/refunds';
import { RefundBadge } from '../components/RefundBadge';
import { StatusBadge } from '../components/StatusBadge';
import { loadOrder } from '../state/orders';

export function OrderDetail({ id }: { id: string }) {
  void loadOrder(id);
  void fetchRefunds(id);
  return (
    <Card>
      <Spinner />
      <StatusBadge status="new" />
      <Timeline items={['created', 'paid']} />
      <RefundBadge refund={{ id: 'ref_1', amount: '5', approved: null }} />
    </Card>
  );
}
