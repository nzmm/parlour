import { GET } from "./requests";

export async function getCurrentUser() {
    return GET("/api/get_current_user");
}

export async function getArtists() {
    return GET("/api/get_artists");
}

export async function getAlbums() {
    return GET("/api/get_albums");
}

export async function getSongs() {
    return GET("/api/get_songs");
}

export async function getLibrary() {
    return GET("/api/get_library");
}

export async function getDownload(id: number) {
    return GET("/api/get_download", { id });
}

export async function getThumbnail(id: number) {
    return GET("/api/get_thumbnail", { id });
}

export async function getArtistDetails(id: number) {
    return GET("/api/get_artist_details", { id });
}

export async function getAlbumDetails(id: number) {
    return GET("/api/get_album_details", { id });
}

export async function getChannels() {
    return GET("/api/get_channels");
}

export async function getChannelTracks(channel_id: string) {
    return GET("/api/get_channel_tracks", { channel_id });
}

export async function search(q: string) {
    return GET("/api/search", { q });
}
