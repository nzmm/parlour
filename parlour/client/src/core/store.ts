import { writable } from 'svelte/store';
import { Views } from './enums/Views';

export const currentView = writable(Views.Artists);

export const artists = writable({ready: false, data: []});
export const albums = writable({ready: false, data: []});