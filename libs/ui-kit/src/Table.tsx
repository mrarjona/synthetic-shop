import { theme } from './theme';

export function Table(props: { children?: unknown }) {
  return <div className="ui-table" style={{ borderRadius: theme.radius }}>{props.children}</div>;
}
