import type { IArtist } from "./IArtist";
import type { ILibraryAlbum } from "./IAlbum";

export interface ILibrary {
    artists: IArtist[];
    releases: ILibraryAlbum[];
}