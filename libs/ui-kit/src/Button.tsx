import { theme } from './theme';

export function Button(props: { children?: unknown }) {
  return <div className="ui-button" style={{ borderRadius: theme.radius }}>{props.children}</div>;
}
