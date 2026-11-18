import { get } from './client';

export const fetchCharges = () => get<string[]>('/charges');
