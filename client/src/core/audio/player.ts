import { playerState, currentTrack, queue, history, library, playbackMode } from '../store';
import { getDownload } from '../api/queries';
import { PlaybackState } from '../enums/PlaybackState';
import { pickRandom } from '../actions';
import { ShuffleMode } from '../enums/ShuffleMode';
import { RepeatMode } from '../enums/RepeatMode';
import type { ITrack } from '../interfaces/ITrack';
import type { ILibraryAlbum } from '../interfaces/IAlbum';

const TIMER_INTERVAL = 1000;
const ms = (sec: number) => sec * 1000;


export class AudioPlayer {

    private _queue: ITrack[];
    private _library: ILibraryAlbum[];
    private _state: PlaybackState = PlaybackState.Stopped;
    private _shuffle: ShuffleMode = ShuffleMode.None;
    private _repeat: RepeatMode = RepeatMode.None;

    private _player = new Audio();
    private _timer = 0;
    private _track_id = 0;

    constructor() {
        queue.subscribe(value => this._queue = value);
        library.subscribe(value => this._library = value);
        playerState.subscribe(value => this._state = value.state);
        playbackMode.subscribe(({ shuffle, repeat }) => {
            this._shuffle = shuffle;
            this._repeat = repeat;
        })

        this.initEvents(this._player);
    }

    private initEvents(player: HTMLAudioElement) {

        player.addEventListener("loadedmetadata", () => {
            playerState.update(cur => ({
                ...cur,
                length: ms(this._player.duration),
                position: ms(this._player.currentTime)
            }));
        });

        player.addEventListener("canplaythrough", () => {
            this.setPlaying();
        });

        player.addEventListener("ended", () => {
            this.onEnded();
        });

        player.addEventListener("error", () => {
            this.onEnded();
        });

    }

    private onEnded() {
        this.playNext();
    }

    public playNext() {
        let track: ITrack;

        if (this._queue.length) {
            track = this._queue.shift();
            queue.set(this._queue);
        } else {
            track = pickRandom(this._library);
        }

        if (track) {
            this.play(track);
            history.update(hist => {
                hist.push(track);
                return hist;
            });
        } else {
            this.setStopped();
        }
    }

    private updateProgress() {
        if (this._player.paused) {
            clearTimeout(this._timer);
            return;
        }

        playerState.update(cur => {
            cur.position = ms(this._player.currentTime);
            return cur;
        });
        this.newTimeout();
    }

    private newTimeout() {
        this._timer = setTimeout(() => this.updateProgress(), TIMER_INTERVAL);
    }

    private setPlaying() {
        playerState.update(cur => ({ ...cur, state: PlaybackState.Playing }));
        this._player.play();
        this.newTimeout();
    }

    private setPaused() {
        if (!this._player.paused) {
            this._player.pause();
        }

        clearTimeout(this._timer);

        playerState.update(cur => (
                { ...cur, state: PlaybackState.Paused }));
    }

    private setStopped() {
        if (!this._player.paused) {
            this._player.pause();
        }

        clearTimeout(this._timer);

        playerState.update(cur => (
            { ...cur, state: PlaybackState.Stopped, position: ms(this._player.duration) }));
    }

    public get state(): PlaybackState {
        return this._state;
    }

    public get queue(): ITrack[] {
        return this._queue;
    }

    public get element(): HTMLAudioElement {
        return this._player;
    }

    public get shuffle(): ShuffleMode {
        return this._shuffle;
    }

    public get repeat(): RepeatMode {
        return this._repeat;
    }

    public toggleShuffle() {
        const shuffle = ShuffleMode[ShuffleMode[this._shuffle + 1]] ?? ShuffleMode.None;
        playbackMode.update(cur => ({...cur, shuffle}));
    }

    public toggleRepeat() {
        const repeat = RepeatMode[RepeatMode[this._repeat + 1]] ?? RepeatMode.None;
        playbackMode.update(cur => ({...cur, repeat}));
    }

    public async play(track: ITrack) {
        if (!track.id) {
            return;
        }

        playerState.update(cur => ({...cur, state: PlaybackState.Loading}));

        this._track_id = track.id;
        currentTrack.set(track);

        const res = await getDownload(track.id);
        const data = await res.json();

        this._player.src = data.download;
        this._player.load();

        if (!navigator.mediaSession) {
            return;
        }

        navigator.mediaSession.metadata = new MediaMetadata({
            title: track.name,
            artist: track.artist_credit,
            album: track.release_name,
            artwork: [{src: track.thumbnail}]
        });
    }

    public toggle() {
        if (!this._track_id) {
            return;
        }
        if (this._player.paused) {
            this.setPlaying();
        } else {
            this.setPaused();
        }
    }
}