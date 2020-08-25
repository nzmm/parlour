import { writable } from 'svelte/store';
import { ToplevelViews } from './enums/ToplevelViews';
import type { ITrack } from './interfaces/ITrack';
import type { ITrackArray } from './interfaces/ITrackArray';
import type { IAlbumArray } from './interfaces/IAlbumArray';
import type { IView } from './interfaces/IView';
import { PlaybackState } from './enums/PlaybackState';

const getInitialView = () => {
    const view = parseInt(sessionStorage.getItem("view"));
    return ToplevelViews[view] != null ? view : ToplevelViews.Library;
}

const toplevel = getInitialView();
console.log(toplevel);
export const currentView = writable<IView>({ toplevel });

export const artists = writable({ready: false, data: []});
export const albums = writable<IAlbumArray>({ready: false, data: []});
export const songs = writable<ITrackArray>({ready: false, data: []});
export const queue = writable<ITrackArray>({ready: true, data: []});

export const playerState = writable({
    state: PlaybackState.Stopped,
    length: 0,
    position: 0
});

export const currentTrack = writable<ITrack>({
    id: 0,
    number: '',
    name: '',
    artist_credit: '',
    release_name: '',
    length_display: '',
    thumbnail: '',
    liked: false
});