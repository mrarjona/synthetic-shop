import { get } from './client';

export const fetchCustomer = (id: string) => get<{ id: string; name: string }>(`/customers/${id}`);
