import type { IProvider } from "./IProvider";

export interface IUser {
    username: string;
    first_name: string;
    full_name: string;
    initials: string;
    trackCount: number;
    providers: IProvider[];
}