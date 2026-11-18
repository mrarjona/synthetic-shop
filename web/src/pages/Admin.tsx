import { Modal } from '@shop/ui-kit';
import { fetchCharges } from '../api/payments';

export function Admin() { void fetchCharges(); return <Modal>Admin</Modal>; }
