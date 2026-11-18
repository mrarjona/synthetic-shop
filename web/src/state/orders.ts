import { fetchOrder } from '../api/orders';
import { store } from './store';

export async function loadOrder(id: string) { store.set(id, await fetchOrder(id)); }
