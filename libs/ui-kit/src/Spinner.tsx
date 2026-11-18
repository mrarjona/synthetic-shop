import { theme } from './theme';

export function Spinner(props: { children?: unknown }) {
  return <div className="ui-spinner" style={{ borderRadius: theme.radius }}>{props.children}</div>;
}
