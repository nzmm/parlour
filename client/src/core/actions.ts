import { currentTrack, currentView, libraryFilter, library, queue } from './store';
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
    return libraryFilter.set({ breadcrumbs: null, fn: x => x });
}

const navigateFromBreadcrumb = (toplevel: ToplevelViews) => {
    setToplevel(toplevel);
    unfilterLibrary();
}

export const filterLibraryByArtist = (artist_id: number, artist_name: string, toplevel: ToplevelViews = ToplevelViews.Artists) => {
    return libraryFilter.set({
        breadcrumbs: [
            {label: "Library", navigateTo: () => navigateFromBreadcrumb(ToplevelViews.Songs)},
            {label: "Artists", navigateTo: () => navigateFromBreadcrumb(toplevel)},
            {label: artist_name}
        ],
        fn: x => x.filter(r => r.artist_id === artist_id)
    });
}

export const filterLibraryByAlbum = (release_id: number, release_name: string, toplevel: ToplevelViews = ToplevelViews.Albums) => {
    return libraryFilter.set({
        breadcrumbs: [
            {label: "Library", navigateTo: () => navigateFromBreadcrumb(ToplevelViews.Songs)},
            {label: "Albums", navigateTo: () => navigateFromBreadcrumb(toplevel)},
            {label: release_name}
        ],
        fn: x => x.filter(r => r.id === release_id)
    });
}

export const setToplevel = (view: ToplevelViews, data?: any) => {
    currentView.set({ toplevel: view, data });
    sessionStorage.setItem("view", JSON.stringify({ toplevel: view, data }));
}


export const pickRandom = (library: ILibraryAlbum[]) => {
    console.log('Picking random track from...', library.length);
    const rndRelease = library[Math.floor(Math.random() * library.length)];
    return rndRelease.tracks[Math.floor(Math.random() * rndRelease.tracks.length)];
}