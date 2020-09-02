import { playerState, currentTrack, queue } from '../store';
import { getDownload } from '../api/queries';
import { PlaybackState } from '../enums/PlaybackState';
import type { ITrack } from '../interfaces/ITrack';

const TIMER_INTERVAL = 1000;
const ms = (sec: number) => sec * 1000;


export class AudioPlayer {

    private _player = new Audio();
    private _queue: ITrack[];
    private _state: PlaybackState = PlaybackState.Stopped;

    private _timer = 0;
    private _track_id = 0;

    constructor() {
        queue.subscribe(value => this._queue = value.data);
        playerState.subscribe(value => this._state = value.state);

        this.initEvents(this._player, this._queue);
    }

    private initEvents(player: HTMLAudioElement, playlist: ITrack[]) {

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
        if (this._queue.length) {
            this.playNext();
        } else {
            this.setStopped();
        }
    }

    public playNext() {
        const track = this._queue.shift();
        this.play(track);
        queue.set({ ready: true, data: this._queue });
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

    async play(track: ITrack) {
        if (!track.id) {
            return;
        }

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

    toggle() {
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