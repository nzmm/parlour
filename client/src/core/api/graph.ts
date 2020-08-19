import { GET } from "./requests";
export async function getArtists() {
    return GET("/providers/graph_get_albums");
}

export async function getAlbums() {
    return GET("/providers/graph_get_albums");
}
