import { currentTrack, currentView, libraryFilter, library } from './store';
import { setLiked } from '../core/api/commands';
import { SublevelViews } from './enums/SublevelViews';
import { ToplevelViews } from './enums/ToplevelViews';
import type { IArtist } from './interfaces/IArtist';
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
}

const setDetailsView = (toplevel: ToplevelViews, sublevel: SublevelViews, data: any) => {
    console.log(toplevel, sublevel, data);
    currentView.update(() => ({
        toplevel,
        sublevel,
        data
    }));
}

export const goBack = () => {
    currentView.update(cur => ({
        ...cur,
        sublevel: null,
        data: null
    }));
};

export const setArtistDetailsView = (data: IArtist) => {
    return setDetailsView(ToplevelViews.Artists, SublevelViews.ArtistDetails, data);
}

export const setAlbumDetailsView = (data: IAlbum) => {
    return setDetailsView(ToplevelViews.Albums, SublevelViews.AlbumDetails, data);
}

export const unfilterLibrary = () => {
    return libraryFilter.set({ key: null, fn: x => x });
}

export const filterLibraryByArtist = (artist_id: number) => {
    return libraryFilter.set({
        key: `artist:${artist_id}`,
        fn: x => x.filter(r => r.artist_id === artist_id)
    });
}

export const filterLibraryByAlbum = (release_id: number) => {
    return libraryFilter.set({
        key: `album:${release_id}`,
        fn: x => x.filter(r => r.id === release_id)
    });
}

export const setToplevel = (view: ToplevelViews) => {
    currentView.set({ toplevel: view });
    sessionStorage.setItem("view", view.toString());
}

export const pickRandom = (library: ILibraryAlbum[]) => {
    console.log('Picking random track from...', library.length);
    const rndRelease = library[Math.floor(Math.random() * library.length)];
    return rndRelease.tracks[Math.floor(Math.random() * rndRelease.tracks.length)];
}