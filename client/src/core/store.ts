import { writable } from 'svelte/store';
import { Views } from './enums/Views';
import type { ITrack } from './interfaces/ITrack';

export const currentView = writable(Views.Songs);

export const artists = writable({ready: false, data: []});
export const albums = writable({ready: false, data: []});
export const songs = writable({ready: false, data: []});

export const playerState = writable({
    loaded: false,
    playing: false,
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