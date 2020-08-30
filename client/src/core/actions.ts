import { queue, currentTrack, currentView, library, libraryFilter } from './store';
import { setLiked } from '../core/api/commands';
import { PlaybackState } from "./enums/PlaybackState";
import { SublevelViews } from './enums/SublevelViews';
import { ToplevelViews } from './enums/ToplevelViews';
import type { IArtist } from './interfaces/IArtist';
import type { IAlbum, ILibraryAlbum } from './interfaces/IAlbum';
import type { ITrack } from "./interfaces/ITrack";
import type { AudioPlayer } from "./audio/player";


const enqueueWithMethod = (player: AudioPlayer, track: ITrack, method: (data: ITrack[]) => void) => {
    if (player.state === PlaybackState.Stopped) {
        player.play(track);
    } else {
        queue.update(q => {
            method(q.data);
            return q;
        });
    }
}

export const enqueue = (player: AudioPlayer, track: ITrack) => {
    enqueueWithMethod(player, track, data => data.push(track));
}

export const enqueueNext = (player: AudioPlayer, track: ITrack) => {
    enqueueWithMethod(player, track, data => data.splice(0, 0, track));
}

export const playNow = (player: AudioPlayer, track: ITrack) => {
    player.play(track);
}

export const likeTrack = async (track: ITrack) => {
    const liked = !track.liked;
    const res = await setLiked(track.id, liked);
    const data = await res.json();

    if (!data.success) {
        return;
    }

    currentTrack.update(cur => {
        cur.liked = liked;
        return cur;
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


export const libUnfilter = () => {
    return libraryFilter.set({ fn: lib => lib });
}


export const libFilterByArtist = (artist_id: number) => {
    return libraryFilter.set({ fn: lib => lib.filter(r => r.artist_id === artist_id) });
}