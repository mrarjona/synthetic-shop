import { Admin } from './pages/Admin';
import { Checkout } from './pages/Checkout';
import { Customers } from './pages/Customers';
import { Home } from './pages/Home';
import { OrderDetail } from './pages/OrderDetail';
import { Orders } from './pages/Orders';
import { Header } from './components/Header';

export function App() {
  return <><Header /><Home /><Orders /><OrderDetail id="ord_1" /><Checkout /><Customers /><Admin /></>;
}
