import { readable, writable } from 'svelte/store';
import type { IArtist } from './interfaces/IArtist';
import type { ITrack } from './interfaces/ITrack';
import type { ILibraryAlbum } from './interfaces/IAlbum';
import type { IBreadcrumb } from './interfaces/IBreadcrumb';
import type { IChannel } from './interfaces/IChannel';
import type { IUser } from './interfaces/IUser';
import { PlaybackState } from './enums/PlaybackState';
import { ShuffleMode } from './enums/ShuffleMode';
import { RepeatMode } from './enums/RepeatMode';

export const user = writable<IUser>(null);
export const artists = writable<IArtist[]>([]);
export const library = writable<ILibraryAlbum[]>([]);
export const queue = writable<ITrack[]>([]);
export const history = writable<ITrack[]>([]);

export const liked = readable([], function start(set) {
    library.subscribe(lib => {
        set(lib.reduce((acc, cur) => {
            return acc.concat(cur.tracks.filter(t => t.liked));
        }, []));
    });
	return function stop() {};
});

export const artistFilter = writable<{ fn: (x: IArtist[]) => IArtist[] }>({ fn: x => x });
export const breadcrumbs = writable<IBreadcrumb[]>([]);

export const playerState = writable({
    state: PlaybackState.Stopped,
    length: 0,
    position: 0
});

export const playbackMode = writable({
    shuffle: ShuffleMode.None,
    repeat: RepeatMode.None
})

export const currentTrack = writable<ITrack>({
    id: 0,
    number: '',
    name: '',
    artist_credit: '',
    release_name: '',
    length: 0,
    length_display: '',
    thumbnail: '',
    liked: false
});

export const channels = writable<IChannel[]>([]);