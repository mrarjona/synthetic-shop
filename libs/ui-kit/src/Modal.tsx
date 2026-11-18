import { theme } from './theme';
import { useToggle } from './hooks/useToggle';

export function Modal(props: { children?: unknown }) {
  return <div className="ui-modal" style={{ borderRadius: theme.radius }}>{props.children}</div>;
}
