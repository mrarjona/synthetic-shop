import { theme } from './theme';

export function Input(props: { children?: unknown }) {
  return <div className="ui-input" style={{ borderRadius: theme.radius }}>{props.children}</div>;
}
