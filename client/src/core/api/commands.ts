import { POST } from './requests';


export async function setLiked(id: number, liked: boolean) {
    return POST("/api/set_liked", { id, liked });
}

export async function createChannel(name: string, description: string, is_public: boolean) {
    return POST("/api/create_channel", { name, description, public: is_public });
}

export async function createChannelTrack(channel_id: string, track_id: number) {
    return POST("/api/create_channel_track", { channel_id, track_id });
}