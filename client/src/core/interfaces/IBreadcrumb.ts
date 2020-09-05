import type { ToplevelViews } from "../enums/ToplevelViews";

export interface IBreadcrumb {
    label: string;
    navigateTo?(): void;
}
