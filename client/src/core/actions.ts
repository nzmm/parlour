import { push } from 'svelte-spa-router';
import { currentTrack, libraryFilter, library, queue } from './store';
import { setLiked } from '../core/api/commands';
import type { IAlbum, ILibraryAlbum } from './interfaces/IAlbum';
import type { ITrack } from "./interfaces/ITrack";


export const likeTrack = async (track: ITrack) => {
    const track_id = track.id;
    const liked = !track.liked;
    const res = await setLiked(track_id, liked);
    const data = await res.json();

    if (!data.success) {
        return;
    }

    currentTrack.update(cur => {
        cur.liked = liked;
        return cur;
    });

    library.update(lib => {
        for (const r of lib) {
            for (const t of r.tracks) {
                if (t.id === track_id) {
                    t.liked = liked;
                    return lib;
                }
            }
        }
        return lib;
    });

    queue.update(qu => {
        for (const t of qu) {
            if (t.id === track_id) {
                t.liked = liked;
                return qu;
            }
        }
        return qu;
    });
}

export const setArtistBreadcrumbs = (artist_id: number, artist_name: string) => {
    return libraryFilter.set({
        breadcrumbs: [
            {label: "Library", navigateTo: () => push('/')},
            {label: "Artists", navigateTo: () => push('/artists')},
            {label: artist_name}
        ]
    });
}

export const setAlbumBradcrumbs = (release_id: number, release_name: string) => {
    return libraryFilter.set({
        breadcrumbs: [
            {label: "Library", navigateTo: () => push('/')},
            {label: "Albums", navigateTo: () => push('/albums')},
            {label: release_name}
        ]
    });
}

export const pickRandom = (library: ILibraryAlbum[]) => {
    console.log('Picking random track from...', library.length);
    const rndRelease = library[Math.floor(Math.random() * library.length)];
    return rndRelease.tracks[Math.floor(Math.random() * rndRelease.tracks.length)];
}