export async function get<T>(path: string): Promise<T> {
  const r = await fetch(`/api${path}`);
  return r.json() as Promise<T>;
}
