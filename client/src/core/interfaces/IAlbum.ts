import type { ITrack } from "./ITrack";

export interface IAlbum {
    id: number;
    name: string;
    thumbnail: string;
    artist_name?: string;
    year?: number;
    tracks?: ITrack[];
}