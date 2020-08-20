function queryString(params: any): string {
    return new URLSearchParams(params).toString()
}

export async function GET(url: string, params?: any) {
    const getUrl = params ? `${url}?${queryString(params)}` : url;
    return fetch(getUrl)
        .then(response => {
            return response;
        })
        .catch(error => {
            console.error(error);
            return error;
        });
}
