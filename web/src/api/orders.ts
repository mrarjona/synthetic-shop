import { get } from './client';

export type Order = { id: string; status: string; total: string };
export const fetchOrder = (id: string) => get<Order>(`/orders/${id}`);
