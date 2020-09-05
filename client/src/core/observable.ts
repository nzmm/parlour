import type { IAlbum } from "./interfaces/IAlbum";


interface ILazyLoaderProps<T> {
    root: HTMLElement;
    selector: string;
    data: T[];
    onIntersection: (e: HTMLElement) => void;
    resolve: (observer: IntersectionObserver) => void;
    reject: () => void;
}


function initIntersectionObservable<T>({ root, selector, data, onIntersection, resolve, reject }: ILazyLoaderProps<T>) {
    const elements = root?.querySelectorAll(selector);

    if (!elements?.length) {
        return reject();
    }
    if (elements.length !== data.length) {
        setTimeout(() => initIntersectionObservable({ root, selector, data, onIntersection, resolve, reject }), 200);
        return;
    }

    console.log(data.length, elements?.length);

    const options: IntersectionObserverInit = {
        root,
        rootMargin: '0px',
        threshold: 0.0
    }

    const callback: IntersectionObserverCallback = entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const elem = entry.target as HTMLElement;
                onIntersection(elem);
            }
        });
    }

    const observer = new IntersectionObserver(callback, options);
    elements.forEach(s => observer.observe(s));
    resolve(observer);
}


export function intersectionObservable<T>(root: HTMLElement, selector: string, data: T[], onIntersection: (e: HTMLElement) => void): Promise<IntersectionObserver> {
    return new Promise((resolve, reject) => {
        setTimeout(() => initIntersectionObservable<T>({
            root,
            selector,
            data,
            onIntersection,
            resolve,
            reject
        }), 100);
    });
}
