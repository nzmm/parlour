export interface IUser {
    username: string;
    full_name: string;
    initials: string;
    providers: {provider: string}[];
}