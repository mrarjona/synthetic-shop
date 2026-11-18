import { theme } from './theme';

export function Badge(props: { children?: unknown }) {
  return <div className="ui-badge" style={{ borderRadius: theme.radius }}>{props.children}</div>;
}
