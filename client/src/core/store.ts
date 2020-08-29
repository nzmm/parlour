import { writable } from 'svelte/store';
import { ToplevelViews } from './enums/ToplevelViews';
import type { IArtist } from './interfaces/IArtist';
import type { ITrack } from './interfaces/ITrack';
import type { ITrackArray } from './interfaces/ITrackArray';
import type { ILibraryAlbum } from './interfaces/IAlbum';
import type { IView } from './interfaces/IView';
import { PlaybackState } from './enums/PlaybackState';

const getInitialView = () => {
    const view = parseInt(sessionStorage.getItem("view"));
    return ToplevelViews[view] != null ? view : ToplevelViews.Library;
}

const toplevel = getInitialView();
export const currentView = writable<IView>({ toplevel });

export const artists = writable<IArtist[]>([]);
export const library = writable<ILibraryAlbum[]>([]);
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