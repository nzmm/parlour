import type { IProvider } from "./IProvider";

export interface IUser {
    username: string;
    full_name: string;
    initials: string;
    providers: IProvider[];
}