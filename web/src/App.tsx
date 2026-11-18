import { Admin } from './pages/Admin';
import { Customers } from './pages/Customers';
import { Home } from './pages/Home';
import { OldCheckout } from './pages/OldCheckout';
import { OrderDetail } from './pages/OrderDetail';
import { Orders } from './pages/Orders';
import { Header } from './components/Header';

export function App() {
  return <><Header /><Home /><Orders /><OrderDetail id="ord_1" /><OldCheckout /><Customers /><Admin /></>;
}
