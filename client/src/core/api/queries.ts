import { GET } from "./requests";

export async function getArtists() {
    return GET("/providers/get_artists");
}

export async function getAlbums() {
    return GET("/providers/get_albums");
}

export async function getSongs() {
    return GET("/providers/get_songs");
}

export async function getDownload(id: number) {
    return GET("/providers/get_download", { id });
}

export async function getThumbnail(id: number) {
    return GET("/providers/get_thumbnail", { id });
}

export async function getArtistDetails(id: number) {
    return GET("/providers/get_artist_details", { id });
}

export async function getAlbumDetails(id: number) {
    return GET("/providers/get_album_details", { id });
}

export async function search(q: string) {
    return GET("/providers/search", { q });
}
