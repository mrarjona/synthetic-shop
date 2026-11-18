import { Table } from '@shop/ui-kit';
import { OrderRow } from './OrderRow';

export function OrderTable() { return <Table><OrderRow order={{ id: 'ord_1', status: 'new', total: '10' }} /></Table>; }
