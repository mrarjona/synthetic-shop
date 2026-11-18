import { theme } from './theme';

export function Card(props: { children?: unknown }) {
  return <div className="ui-card" style={{ borderRadius: theme.radius }}>{props.children}</div>;
}
