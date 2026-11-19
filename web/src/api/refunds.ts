import { get } from './client';

export type Refund = { id: string; amount: string; approved: boolean | null };
export const fetchRefunds = (orderId: string) => get<Refund[]>(`/orders/${orderId}/refunds`);
