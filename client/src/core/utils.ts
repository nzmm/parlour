function d02(n: number): string {
    return n.toString().padStart(2, '0');
}

export function getHms(ms: number): [string, string] {
    const s = Math.floor((ms / 1000) % 60);
    const m = Math.floor((ms / (1000 * 60)) % 60);
    const h = Math.floor((ms / (1000 * 60 * 60)) % 24);
    return h
        ? [`${h}:${d02(m)}:${d02(s)}`, h !== 1 ? 'hours' : 'hour']
        : [`${m}:${d02(s)}`, m !== 1 ? 'mins' : 'min'];
}

export function createDebouncer(timeout: number = 500) {
    let timer: number;
    return (func: VoidFunction) => {
        clearTimeout(timer);
        timer = setTimeout(() => {
            func();
        }, timeout);
	}
}
