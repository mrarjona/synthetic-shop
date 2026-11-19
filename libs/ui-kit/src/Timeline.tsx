import { theme } from './theme';

export function Timeline({ items }: { items: string[] }) {
  return <ol style={{ gap: theme.gap }}>{items.map((i) => <li key={i}>{i}</li>)}</ol>;
}
