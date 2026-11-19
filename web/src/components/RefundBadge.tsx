import { Badge } from '@shop/ui-kit';
import type { Refund } from '../api/refunds';

export function RefundBadge({ refund }: { refund: Refund }) {
  return <Badge>{refund.approved === null ? 'pending' : refund.approved ? 'refunded' : 'rejected'}</Badge>;
}
