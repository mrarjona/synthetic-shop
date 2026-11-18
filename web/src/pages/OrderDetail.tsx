import { Card, Spinner } from '@shop/ui-kit';
import { StatusBadge } from '../components/StatusBadge';
import { loadOrder } from '../state/orders';

export function OrderDetail({ id }: { id: string }) {
  void loadOrder(id);
  return <Card><Spinner /><StatusBadge status="new" /></Card>;
}
