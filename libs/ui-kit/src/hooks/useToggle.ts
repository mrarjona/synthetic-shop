import { useState } from 'react';

export function useToggle(initial = false) {
  const [on, set] = useState(initial);
  return [on, () => set(!on)] as const;
}
