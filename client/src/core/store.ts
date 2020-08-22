import { writable } from 'svelte/store';
import { Views } from './enums/Views';
import type { ITrack } from './interfaces/ITrack';
import type { ITrackArray } from './interfaces/ITrackArray';
import type { IAlbumArray } from './interfaces/IAlbumArray';
import { PlaybackState } from './enums/PlaybackState';

const initView = parseInt(sessionStorage.getItem("view")) ?? Views.Artists;
export const currentView = writable(initView);

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