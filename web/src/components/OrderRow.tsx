import type { Order } from '../api/orders';
import { PriceTag } from './PriceTag';
import { StatusBadge } from './StatusBadge';

export function OrderRow({ order }: { order: Order }) {
  return <tr><td>{order.id}</td><td><StatusBadge status={order.status} /></td><td><PriceTag value={order.total} /></td></tr>;
}
