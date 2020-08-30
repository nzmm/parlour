import type { ITrack } from "./ITrack";


export interface IAlbum {
    id: number;
    name: string;
    thumbnail: string;
    artist_name?: string;
    year?: number;
    tracks?: ITrack[];
}

export interface ILibraryAlbum {
    id: number;
    name: string;
    thumbnail: string;
    artist_id: number;
    artist_name: string;
    year: number;
    track_count: number;
    tracks: ITrack[];
}