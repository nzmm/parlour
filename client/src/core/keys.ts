export const registerGlobalKeyUpHandler = (key: string, handler: (event?: KeyboardEvent) => void) => {

    const onKeyboardEvent = (ev: KeyboardEvent) => {
        if (ev.key !== key || (ev.target as HTMLElement).localName == "input") {
            return;
        }

        handler(ev);
    };

    document.addEventListener("keyup", onKeyboardEvent);
    return () => document.removeEventListener("keyup", onKeyboardEvent);
}