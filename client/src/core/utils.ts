function d02(n: number): string {
    return n.toString().padStart(2, '0');
}

export function getHms(ms: number): string {
    const s = Math.floor((ms / 1000) % 60);
    const m = Math.floor((ms / (1000 * 60)) % 60);
    const h = Math.floor((ms / (1000 * 60 * 60)) % 24);
    return h ? `${h}:${d02(m)}:${d02(s)}` : `${m}:${d02(s)}`;
}
